from BaseDeDatos import Basededatos
import json


class Recomendar(Basededatos):
    def __init__(self, df1: str):
        super().__init__(df1)

    def Recomendar(self, nomusuario):
        while (True):
            try:
                print("\n-----------------------------------------------------")
                print("                   Descubre                          \n")   
                print("1- Trending books")
                print("2- Recomendación por categoría")
                print("3- Recomendación por autor")
                print("4- Atrás")
                recomendacion = int(input('Escoja una opción: '))

                if recomendacion == 1:
                    print("\n-----------------------------------------------------")
                    print("          Los libros más populares                   ")
                    self.recom_populares()

                elif recomendacion == 2:
                    print("\n-----------------------------------------------------")
                    print("          Recomendación por categoría                ")
                    self.recom_categoria(nomusuario)

                elif recomendacion == 3:
                    print("\n-----------------------------------------------------")
                    print("            Recomendación por autor                  ")
                    self.recom_autor(nomusuario)

                elif recomendacion == 4:
                    break

                else:
                    print(f"\nOpción invalida, por favor vuelva a escoger una opción:\n")
                
            except ValueError as e:
                print(f"\nNo se ingresó ninguna opción.\nError: {e}\n")

    def recom_populares(self):
        """ 
        Recomendación por popularidad. 
        Recomienda al usuario libros que tienen entre 3 y 5 estrellas.
        """
        punt = 0
        self.dfp = self.df1.sort_values('Puntuación', ascending=False)
        self.dfp = self.dfp.drop(
            ['Autor', 'Categoria', 'Año_publicado'], axis=1)

        if punt == 0:
            self.dfp = self.dfp[self.dfp.Puntuación > 3]
            self.dfp = self.dfp[self.dfp.Puntuación <= 5]
        print(self.dfp.head(25))

    def recom_categoria(self, nomusuario):

        """ 
        Recomendación por categoría: 
        Recomienda al usuario libros que tienen misma categoría 
        tomando los libros del archivo de libros leídos.
        """

        # Importar un libro de libros leidos
        try:
            with open("DB/leidos.json", "r") as archivo_leidos:
                libros_leidos = json.load(archivo_leidos)
        except FileNotFoundError:
            print("No se encontró el archivo de libros leídos")
            libros_leidos = {}
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {e}")
            libros_leidos = {}
        except Exception as e:
            print(f"Error inesperado: {e}")
            libros_leidos = {}

        # Obtener la lista de libros leídos por el usuario
        if nomusuario in libros_leidos:
            libros_usuario = libros_leidos[nomusuario]
        else:
            print(f"No se encontraron libros leídos para el usuario {nomusuario}")
            libros_usuario = []

        # Encontrar categoria del libro importado
        df_categorias = self.df1[self.df1['Titulo'].isin(libros_usuario)][['Titulo', 'Categoria']]

        # Contar las ocurrencias de cada categoría
        categoria_counts = df_categorias['Categoria'].value_counts()

        # Encontrar la categoría más frecuente
        if not categoria_counts.empty:
            categoria_mas_frecuente = categoria_counts.idxmax()
        else:
            categoria_mas_frecuente = df_categorias['Categoria'].iloc[0] if not df_categorias.empty else None

        # Almacenar la categoría en self.df2
        self.df2 = categoria_mas_frecuente

        # Se ajustan los datos para obtener un str con el nombre de la categoria
        self.df2 = self.df2.replace("\n", "")
        self.df2 = self.df2.replace(" ", "")

        # Recomendar por categoria y puntuación
        self.df2 = self.df1.loc[self.df1['Categoria'] == self.df2]
        self.df2 = self.df2.sort_values('Puntuación', ascending=False)
        self.df2 = self.df2.drop(['Autor'], axis=1)
        print(self.df2.head(25))

    def recom_autor(self, nomusuario):

        """ 
        Recomendación por autor: 
        Recomienda al usuario libros del mismo autor tomando los 
        del archivo de libros leídos.
        """

        # Importar un libro de libros leidos
        try:
            with open("DB/leidos.json", "r") as archivo_leidos:
                libros_leidos = json.load(archivo_leidos)
        except FileNotFoundError:
            print("No se encontró el archivo de libros leídos")
            libros_leidos = {}
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {e}")
            libros_leidos = {}
        except Exception as e:
            print(f"Error inesperado: {e}")
            libros_leidos = {}

        # Obtener la lista de libros leídos por el usuario
        if nomusuario in libros_leidos:
            libros_usuario = libros_leidos[nomusuario]
        else:
            print(f"No se encontraron libros leídos para el usuario {nomusuario}")
            libros_usuario = []

        # Encontrar autor del libro importado
        df_autores = self.df1[self.df1['Titulo'].isin(libros_usuario)][['Titulo', 'Autor']]

        # Contar las ocurrencias de cada categoría
        autores_counts = df_autores['Autor'].value_counts()

        # Encontrar la categoría más frecuente
        if not autores_counts.empty:
            autor_mas_frecuente = autores_counts.idxmax()
        else:
            autor_mas_frecuente = df_autores['Autor'].iloc[0] if not df_autores.empty else None

        # Almacenar la categoría en self.df2
        self.df2 = autor_mas_frecuente

        # Se ajustan los datos para obtener un str con el nombre del autor
        self.df2 = self.df2.replace("\n", "")
        # Recomendar por autor y puntuación
        self.df2 = self.df1.loc[self.df1['Autor'] == self.df2]
        self.df2 = self.df2.sort_values('Puntuación', ascending=False)
        print(self.df2.head(25))

