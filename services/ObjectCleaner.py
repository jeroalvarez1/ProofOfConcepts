from functools import reduce
from services.ToolsObject import ToolsObject


class ObjectCleaner:

    def __init__(self, csv_list):
        """
        Constructor de la clase ObjectCleaner.

        :param csv_list: Una lista de DataFrames en formato CSV.
        """
        self.df_list = ToolsObject.convertCsvToDF(csv_list)  # Convierte la lista de CSV en una lista de DataFrames

    def mergeRowsOfOneDataFrame(self, df_position, unique_value, id_value=None):
        """
        Combina las filas de un DataFrame en función de un valor único y opcionalmente agrega un nuevo ID.

        :param df_position: La posición del DataFrame en la lista df_list.
        :param unique_value: La columna utilizada para combinar filas de manera única.
        :param id_value: La columna que se utilizará como ID, si se requiere convinar.
        :return: Un DataFrame con las filas combinadas.
        """
        df = self.df_list[df_position]  # Obtiene el DataFrame en la posición especificada

        if id_value in df.columns:
            # Si la columna del ID existe, crea un diccionario de agregación
            agg_dict = {
                id_value: list,
                **{col: 'first' for col in df.columns if col != id_value},
            }
        else:
            # Si no existe una columna de ID, agrega todas las columnas al resultado
            agg_dict = {
                col: 'first' for col in df.columns
            }

        result_df = df.groupby(unique_value, as_index=False).agg(agg_dict)  # Combina filas por valor único

        return result_df  # Devuelve el DataFrame resultante

    def mergeRowsOfDataFrames(self, unique_value, external_id_name=None, id_begins='pwc'):
        """
        Combina múltiples DataFrames en la lista df_list en uno solo, utilizando la columna unique_value.

        :param unique_value: La columna utilizada para combinar filas de manera única.
        :param external_id_name: El nombre de la nueva columna de ID externo, si se proporciona.
        :param id_begins: Prefijo para el ID externo, el valor predeterminado es 'pwc'.
        :return: Un DataFrame combinado.
        """
        if not self.df_list:
            return None # Si la lista de DataFrames está vacía, devuelve None
        for i in range(len(self.df_list)):
            self.df_list[i] = self.df_list[i].set_index(unique_value) # Establece la columna unique_value como índice

        result_df = reduce(
            lambda left, right: left.combine_first(right),
            self.df_list
        ) # Combina los DataFrames en la lista utilizando la función combine_first

        result_df.reset_index(inplace=True) # Restablece el índice del DataFrame combinado

        if external_id_name is not None:
            # Si se proporciona un nombre de columna de ID externo, crea esa columna con valores únicos
            result_df[external_id_name] = [id_begins + str(i) for i in range(1, len(result_df) + 1)]

        for col_name in result_df.columns:
            result_df = ToolsObject.convertColumToString(result_df, col_name) # Convierte todas las columnas a tipo string

        return result_df # Devuelve el DataFrame combinado
