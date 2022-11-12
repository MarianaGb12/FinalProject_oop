from BaseDeDatos import Basededatos


class Recomendar(Basededatos):
    def __init__(self, df1: str):
        super().__init__(df1)

    def recom_populares(self):
        """ 
        Recomendación por popularidad. 
        Recomienda al usuario libros 
        que tienen entre 3 y 5 estrellas.
        """
        punt = 0
        self.dfp = self.df1.sort_values('Puntuación', ascending=False)
        self.dfp = self.dfp.drop(
            ['Autor', 'Categoria', 'Año_publicado'], axis=1)

        if punt == 0:
            self.dfp = self.dfp[self.dfp.Puntuación > 3]
            self.dfp = self.dfp[self.dfp.Puntuación <= 5]
        print(self.dfp.head(25))

    def recom_categoria(self):

        # Importar un libro de libros leidos
        self.archivo_leidos = open("leidos.txt", "r")
        self.linea = self.archivo_leidos.readline()
        self.archivo_leidos.close()
        self.linea = self.linea.replace("\n", "")  # remplazar el "\n"
        # Encontrar categoria del libro importado
        self.df2 = self.df1[self.df1['Titulo'] == self.linea]['Categoria']
        self.df2 = self.df2.head(1)
        # Se ajustan los datos para obtener un str con el nombre de la categoria
        self.df2 = self.df2.to_string(index=False)
        self.df2 = self.df2.replace("\n", "")
        self.df2 = self.df2.replace(" ", "")
        # Recomendar por categoria y puntuación
        self.df2 = self.df1.loc[self.df1['Categoria'] == self.df2]
        self.df2 = self.df2.sort_values('Puntuación', ascending=False)
        self.df2 = self.df2.drop(['Autor'], axis=1)
        print(self.df2.head(25))

    def recom_autor(self):

        self.archivo_leidos = open("leidos.txt", "r")
        self.linea = self.archivo_leidos.readline()
        self.archivo_leidos.close()
        self.linea = self.linea.replace("\n", "")  # remplazar el "\n"
        # Encontrar autor del libro importado
        self.df2 = self.df1[self.df1['Titulo'] == self.linea]['Autor']
        self.df2 = self.df2.head(1)
        # Se ajustan los datos para obtener un str con el nombre del autor
        self.df2 = self.df2.to_string(index=False)
        self.df2 = self.df2.replace("\n", "")
        # Recomendar por autor y puntuación
        self.df2 = self.df1.loc[self.df1['Autor'] == self.df2]
        self.df2 = self.df2.sort_values('Puntuación', ascending=False)
        print(self.df2.head(25))

    def Recomendar(self):
        while (True):
            print("-----------------------------------------------------")
            print("                   Descubrir                             ")
            print("1- Trending books")
            print("2- Recomendación por categoría")
            print("3- Recomendación por autor")
            print("4- Atrás")
            recomendacion = int(input('Escoja una opción: '))

            if recomendacion == 1:
                print("-----------------------------------------------------")
                print("          Los libros más populares                   ")
                self.recom_populares()

            elif recomendacion == 2:
                print("-----------------------------------------------------")
                print("          Recomendación por categoría                ")
                self.recom_categoria()

            elif recomendacion == 3:
                print("-----------------------------------------------------")
                print("            Recomendación por autor                  ")
                self.recom_autor()

            elif recomendacion == 4:
                break

            else:
                raise TypeError
