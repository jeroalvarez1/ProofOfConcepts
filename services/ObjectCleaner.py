import pandas as pd
from functools import reduce
from services.ToolsObject import ToolsObject


class ObjectCleaner:

    def __init__(self, csv_list):
        self.df_list = ToolsObject.convertCsvToDF(csv_list)

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

        if external_id_name is not None:
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

        for col_name in result_df.columns:
            result_df = ToolsObject.convertColumToString(result_df, col_name)

        return result_df

