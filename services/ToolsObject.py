import pandas as pd


class ToolsObject:

    @classmethod
    def convertColumToString(cls, df, col_name):
        df[col_name] = df[col_name].astype(str)
        df[col_name] = df[col_name].replace('nan', '')
        df[col_name] = df[col_name].str.replace(r'\.0$', '', regex=True)
        return df

    @classmethod
    def convertCsvToDF(cls, csv_list):
        return [pd.read_csv(csv) for csv in csv_list]

    @classmethod
    def convertDFToCsv(cls, route, df):
        try:
            df.to_csv(route, index=False)
        except Exception as e:
            print(f"Error al guardar CSV: {str(e)}")

    @classmethod
    def dropColums(cls, df, colums):
        return df.drop(colums, axis=1)