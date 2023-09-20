import pandas as pd

from services.ToolsObject import ToolsObject


class ObjectJoiner:

    def __init__(self, csv1, csv2, cols_name, ext_id_name):
        """
        Constructor de la clase ObjectJoiner.

        :param csv1: Ruta al primer archivo CSV.
        :param csv2: Ruta al segundo archivo CSV.
        :param cols_name: Lista de nombres de columnas a utilizar para la búsqueda.
        :param ext_id_name: Nombre de la columna que contendrá el ID externo.
        """
        self.df1 = pd.read_csv(csv1) # Lee el primer archivo CSV y lo almacena en self.df1
        self.df2 = pd.read_csv(csv2) # Lee el segundo archivo CSV y lo almacena en self.df2
        self.cols_name = cols_name # Lista de nombres de columnas para la búsqueda
        self.ext_id_name = ext_id_name # Nombre de la columna que contendrá el ID externo

    def searchRows(self, search_value_id, df, col_name):
        """
        Busca filas en un DataFrame que contengan un valor específico en una columna dada.

        :param search_value_id: Valor a buscar en la columna.
        :param df: DataFrame en el que se realizará la búsqueda.
        :param col_name: Nombre de la columna en la que se realizará la búsqueda.
        :return: DataFrame con las filas que cumplen con el criterio de búsqueda.
        """
        return df[df[col_name].apply(lambda x: search_value_id in x if x is not None else False)]

    def getExtId(self, search_value_id=None):
        """
        Obtiene el ID externo buscando en el DataFrame df2 utilizando la lista de columnas cols_name.

        :param search_value_id: Valor a buscar en las columnas.
        :return: El valor de la columna ext_id_name si se encuentra una coincidencia, None en caso contrario.
        """
        for col_name in self.cols_name:
            df2 = ToolsObject.convertColumToString(self.df2, col_name) # Convierte la columna a tipo string
            row = self.searchRows(search_value_id, df2, col_name) # Realiza la búsqueda en el DataFrame df2
            if not row.empty:
                return row[self.ext_id_name].iloc[0] # Devuelve el valor de la columna ext_id_name si se encuentra una coincidencia

    def joinTwoDF(self, fk):
        """
        Realiza una unión entre dos DataFrames utilizando una clave foránea (fk).

        :param fk: Nombre de la columna que servirá como clave foránea.
        :return: El DataFrame resultante de la unión.
        """
        df = self.df1 # Crea una copia del primer DataFrame
        df[fk] = df.apply(lambda row: self.getExtId(search_value_id=str(row[fk])), axis=1) # Aplica la función getExtId a cada fila
        return df # Devuelve el DataFrame resultante de la unión

