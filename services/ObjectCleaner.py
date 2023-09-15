import pandas as pd
from functools import reduce


class ObjectCleaner:

    def __init__(self):
        self.df_list = []

    def convertCsvToDF(self, csv_list):
        self.df_list = [pd.read_csv(csv) for csv in csv_list]

    def mergeRowsOfOneDataFrame(self, df_position, unique_value, id_value=None, external_id_name=None, id_begins='pwc'):
        df = self.df_list[df_position]

        if id_value in df.columns:
            agg_dict = {
                id_value: list,
                **{col: 'first' for col in df.columns if col != id_value},
            }
        else:
            agg_dict = {
                col: 'first' for col in df.columns
            }

        result_df = df.groupby(unique_value, as_index=False).agg(agg_dict)

        if external_id_name != None:
            result_df[external_id_name] = [id_begins + str(i) for i in range(1, len(result_df) + 1)]

        return result_df

    def mergeRowsOfDataFrames(self, unique_value):
        if not self.df_list:
            return None
        for i in range(len(self.df_list)):
            self.df_list[i] = self.df_list[i].set_index(unique_value)

        result_df = reduce(
            lambda left, right: left.combine_first(right),
            self.df_list
        )

        result_df.reset_index(inplace=True)

        for col in result_df.columns:
            result_df[col] = result_df[col].astype(str)
            result_df[col] = result_df[col].replace('nan', '')
            result_df[col] = result_df[col].str.replace(r'\.0$', '', regex=True)

        return result_df

    def convertDFToCsv(self, route, df):
        try:
            df.to_csv(route, index=False)
        except Exception as e:
            print(f"Error al guardar CSV: {str(e)}")
