import pandas as pd
from functools import reduce


class DataFrameService:

    def __init__(self):
        self.df_list = []

    def convertCsvToDF(self, csv_list):
        self.df_list = [pd.read_csv(csv) for csv in csv_list]

    def mergeRowsOfOneDataFrame(self, df_position, unique_value):
        df = self.df_list[df_position]
        result_df = df.groupby(unique_value, as_index=False).agg({col: 'first' for col in df.columns})
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
        return result_df

    def convertDFToCsv(self, route, df):
        try:
            df.to_csv(route, index=False)
        except Exception as e:
            print(f"Error al guardar CSV: {str(e)}")