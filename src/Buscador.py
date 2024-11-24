from BaseDeDatos import Basededatos


class Buscador(Basededatos):
    def __init__(self, df1: str):
        super().__init__(df1)

    def Buscar(self):
        """
        Menú para el buscador de libros.
        Se aplica por diferentes campos, como por:
        - Título
        - Puntuación ingresada por el usuario
        - Fecha de publicación 
        - Categoría
        """
        while (True):
            try:
                print("\n-----------------------------------------------------")
                print("                 - BUSCAR -                          \n")
                print("1- Buscar por título")
                print("2- Buscar por puntuación")
                print("3- Buscar por fecha de publicación")
                print("4- Buscar por categoría")
                print("5- Atrás")
                filtro = int(input("Escoja una opción: "))

                if filtro == 1:
                    print("\n-----------------------------------------------------")
                    print("               Buscar por título                     ")
                    self.Buscar_titulo()

                elif filtro == 2:
                    print("\n-----------------------------------------------------")
                    print("             Buscar por puntuación                   ")
                    self.Buscar_puntuacion()

                elif filtro == 3:
                    print("\n-----------------------------------------------------")
                    print("        Buscar por fecha de publicación              ")
                    self.Buscar_fecha()

                elif filtro == 4:
                    print("\n-----------------------------------------------------")
                    print("               Buscar Categoria                      ")
                    self.Buscar_categoria()

                elif filtro == 5:
                    break

                else:
                    print(f"\nOpción invalida, por favor vuelva a escoger una opción:\n")

            except ValueError as e:
                print(f"\nNo se ingresó ninguna opción.\nError: {e}\n")
        
    def Buscar_titulo(self):
        titulo = input("Ingrese título: ")
        self.dfb = self.df1.loc[self.df1['Titulo'] == titulo]
        print(self.dfb.head(20))
        
    def Buscar_puntuacion(self):
        puntaje = int(input('Ingrese un puntaje (De 0-5): '))
        # se buscan libros dependiendo de la puntuación ingresada
        self.dfe = self.df1.sort_values('Puntuación', ascending=False)
        self.dfe = self.dfe.drop(
            ['Autor', 'Categoria', 'Año_publicado'], axis=1)

        if puntaje == 1:
            print("No hay libros con puntuación de 1")

        elif puntaje == 2:
            self.dfe = self.dfe[self.dfe.Puntuación < 3]
            self.dfe = self.dfe[self.dfe.Puntuación >= 2]
            print(self.dfe.head(10))

        elif puntaje == 3:
            self.dfe = self.dfe[self.dfe.Puntuación < 4]
            self.dfe = self.dfe[self.dfe.Puntuación >= 3]
            print(self.dfe.head(10))

        elif puntaje == 4:
            self.dfe = self.dfe[self.dfe.Puntuación < 5]
            self.dfe = self.dfe[self.dfe.Puntuación >= 4]
            print(self.dfe.head(10))

        elif puntaje == 5:
            self.dfe = self.dfe[self.dfe.Puntuación == 5]
            print(self.dfe.head(10))

        elif puntaje == 0:
            self.dfe = self.dfe[self.dfe.Puntuación < 1]
            self.dfe = self.dfe[self.dfe.Puntuación >= 0]
            print(self.dfe.head(10))

    def Buscar_fecha(self):
        # opción de buscar por más reciente o antiguo.
        print("1- Recientes -> Antiguos")
        print("2- Antiguos -> Recientes")
        orden = int(input('Escoja una opción: '))

        self.dff = self.df1.drop(['Autor', 'Categoria', 'Puntuación'], axis=1)

        if orden == 1:
            self.dff = self.dff.sort_values('Año_publicado', ascending=False)

        elif orden == 2:
            self.dff = self.dff.sort_values('Año_publicado')

        print(self.dff.head(10))

    def Buscar_categoria(self):

        print("1-Ficción     || 2-Policial     || 3-Lit.cristiana || 4- Historia ")
        print("5-Informativo || 6-Aventura     || 7-Romance       || 8-Drama")
        print("9-Economia    || 10-Literatura  || 11-Psicología   || 12-Filosofía")
        print("13-Ciencia    || 14-Recreación  || 15-Terror")
        categoria = int(input('Escoja una categoría: '))

        """
         si la categoria ingresada coincide con la categoria de 
         la base de datos, entonces se muestran los títulos
         pertenecientes a tal categoría.
        """

        if categoria == 1:
            self.dfc = self.df1[self.df1['Categoria'] == 'Ficción']['Titulo']

        elif categoria == 2:
            self.dfc = self.df1[self.df1['Categoria'] == 'Policial']['Titulo']

        elif categoria == 3:
            self.dfc = self.df1[self.df1['Categoria'] == 'Lit.cristiana']['Titulo']

        elif categoria == 4:
            self.dfc = self.df1[self.df1['Categoria'] == 'Historia']['Titulo']

        elif categoria == 5:
            self.dfc = self.df1[self.df1['Categoria'] == 'Informativo']['Titulo']

        elif categoria == 6:
            self.dfc = self.df1[self.df1['Categoria'] == 'Aventura']['Titulo']

        elif categoria == 7:
            self.dfc = self.df1[self.df1['Categoria'] == 'Romance']['Titulo']

        elif categoria == 8:
            self.dfc = self.df1[self.df1['Categoria'] == 'Drama']['Titulo']

        elif categoria == 9:
            self.dfc = self.df1[self.df1['Categoria'] == 'Economia']['Titulo']

        elif categoria == 10:
            self.dfc = self.df1[self.df1['Categoria'] == 'Literatura']['Titulo']

        elif categoria == 11:
            self.dfc = self.df1[self.df1['Categoria'] == 'Psicologia']['Titulo']

        elif categoria == 12:
            self.dfc = self.df1[self.df1['Categoria'] == 'Filosofia']['Titulo']

        elif categoria == 13:
            self.dfc = self.df1[self.df1['Categoria'] == 'Ciencia']['Titulo']

        elif categoria == 14:
            self.dfc = self.df1[self.df1['Categoria'] == 'Recreacion']['Titulo']

        elif categoria == 15:
            self.dfc = self.df1[self.df1['Categoria'] == 'Terror']['Titulo']

        print(self.dfc.head(10))

