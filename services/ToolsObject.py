import pandas as pd


class ToolsObject:

    @classmethod
    def convertColumToString(cls, df, col_name):
        """
        Convierte una columna específica del DataFrame en tipo de datos 'str' (cadena de texto).

        :param df: El DataFrame en el que se realizará la conversión.
        :param col_name: El nombre de la columna que se convertirá.
        :return: El DataFrame con la columna convertida.
        """
        df[col_name] = df[col_name].astype(str) # Convierte la columna a tipo 'str'
        df[col_name] = df[col_name].replace('nan', '') # Reemplaza 'nan' con cadena vacía
        df[col_name] = df[col_name].str.replace(r'\.0$', '', regex=True) # Elimina '.0' al final de los valores
        return df

    @classmethod
    def convertCsvToDF(cls, csv_list):
        """
        Convierte una lista de archivos CSV en una lista de DataFrames.

        :param csv_list: Lista de rutas de archivos CSV.
        :return: Lista de DataFrames correspondientes a los archivos CSV.
        """
        return [pd.read_csv(csv) for csv in csv_list] # Lee cada archivo CSV y lo almacena como DataFrame

    @classmethod
    def convertDFToCsv(cls, route, df):
        """
        Guarda un DataFrame en un archivo CSV en una ruta específica.

        :param route: Ruta del archivo CSV de destino.
        :param df: El DataFrame que se desea guardar.
        """
        try:
            df.to_csv(route, index=False) # Intenta guardar el DataFrame en el archivo CSV
        except Exception as e:
            print(f"Error al guardar CSV: {str(e)}") # Imprime un mensaje de error si se produce una excepción

    @classmethod
    def dropColums(cls, df, colums_name):
        """
        Elimina una o varias columnas de un DataFrame.

        :param df: El DataFrame del que se eliminarán las columnas.
        :param colums: Lista de nombres de columnas que se eliminarán.
        :return: El DataFrame resultante después de eliminar las columnas.
        """
        return df.drop(colums_name, axis=1) # Elimina las columnas especificadas y devuelve el DataFrame resultante