import pandas as pd

from services.ToolsObject import ToolsObject


class ObjectJoiner:

    def __init__(self, df1, df2, cols_name, ext_id_name):
        self.df1 = pd.read_csv(df1)
        self.df2 = pd.read_csv(df2)
        self.cols_name = cols_name
        self.ext_id_name = ext_id_name

    def searchRows(self, search_value_id, df, col_name):
        return df[df[col_name].apply(lambda x: search_value_id in x if x is not None else False)]

    def getExtId(self, search_value_id=None):
        for col_name in self.cols_name:
            df2 = ToolsObject.convertColumToString(self.df2, col_name)
            row = self.searchRows(search_value_id, df2, col_name)
            if not row.empty:
                return row[self.ext_id_name].iloc[0]

    def joinTwoDF(self, fk):
        df = self.df1
        df[fk] = df.apply(lambda row: self.getExtId(search_value_id=str(row[fk])), axis=1)
        return df

