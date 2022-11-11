from BaseDeDatos import Basededatos

class Menu(Basededatos):
    def __init__(self, df1: str):
        super().__init__(df1)

    def mostrar_libros(self):
        print(self.df1.head(15))
        while(True):
            print("Desea agregar libros a su estante ")
            print("1)Si || 2)No : ")
            op = int(input("Escoja una opción: \n"))
            if op == 1:
                print("\n1)Estantería LIBROS LEÍDOS || 2)Estantería QUIERO LEER || 3) Atrás  ")
                op2= int(input("Elija una opción : "))
                if op2 == 1: 
                    self.estante_leidos()

                elif op2 == 2:
                    self.estante_quieroleer()
                            
                elif op2 == 3:
                    break

                else:
                    print("Opción inválida")
            elif op == 2:
                break

            else:
                print("Opción inválida")

    def estante_leidos(self):

        print("\n*** Estante LIBROS LEÍDOS ***")
        while (True):
            print("1- Agregar libro a leídos || 2-Ver estante LIBROS LEÍDOS || 3-Atrás")
            opcion2 = int(input("Escoja una opción: "))

            if opcion2 == 1:  
                # apertura del archivo en modo escritura
                archivo_leidos = open("leidos.txt", "w")
                        
                print("* Agregar libro a Estante Leídos *")
                librosleidos = []
                nuevolibro = input(" 1-Añadir libro || 2-Regresar : ")
                while nuevolibro == "1":
                    librousuario = input("Ingrese el título: ")
                    librosleidos.append(librousuario)
                    nuevolibro = input("¿Desea añadir más libros: 1.Si , 2.No :")
                print(librosleidos)

                # recorremos la lista y agregamos cada titulo al archivo
                for leido in librosleidos:
                    print(leido, file=archivo_leidos)
                # cierre del archivo
                archivo_leidos.close()

            elif opcion2 == 2:
                print("* LIBROS LEÍDOS *")
                with open("leidos.txt") as archivo:
                    print(archivo.readlines())
                print("\n")

            elif opcion2 == 3:
                break
            else:
                print("Opción inválida")

    def estante_quieroleer(self):

        print("\n*** Estante QUIERO LEER ***")
        while (True):
            print("1- Agregar libro a Quiero Leer || 2-Ver estante QUIERO LEER || 3-Atrás")
            opcion3 = int(input("Escoja una opción: "))
            if opcion3 == 1:
                # apertura del archivo en modo escritura
                archivo_quieroleer = open("quiero_leer.txt", "w")
                        
                print("Agregar libro a Estante Quiero Leer")
                wanttoread = []
                nuevlibro = input(" 1-Añadir libro || 2-Regresar ")
                while nuevlibro == "1":
                    libro_usuario = input("Ingrese título: ")
                    wanttoread.append(libro_usuario)
                    nuevlibro = input("¿Desea añadir más libros: 1)Si , 2)No")
                print(wanttoread)

                # Recorremos la lista y agregamos cada titulo al archivo
                for want in wanttoread:
                    print(want, file=archivo_quieroleer)
                # cierre del archivo
                archivo_quieroleer.close()

            elif opcion3 == 2:
                print("* QUIERO LEER *")
                with open("quiero_leer.txt") as archivo:
                    print(archivo.readlines())
                print("\n")

            elif opcion3 == 3:
                break

            else:
                print("Opción inválida")

    def Buscar(self):
        print("\n")
        while(True):
            print("- BUSCADOR -")
            print("1- Buscar por título")
            print("2- Buscar por puntuación")
            print("3- Buscar por fecha de publicación")
            print("4- Buscar por categoría")
            print("5- Atrás")
            filtro = int(input("Escoja una opción: "))
            
            if filtro == 1:
                titulo = input("Ingrese título: ")
                self.dfb = self.df1.loc[self.df1['Titulo'] == titulo]
                print(self.dfb.head(10))
            
            elif filtro == 2:
                print("Buscar por puntuación \n")
                self.Buscar_puntuacion()

            elif filtro == 3:
                print("Buscar por fecha de publicación \n")
                self.Buscar_fecha()

            elif filtro == 4:
                print("Buscar Categoria \n")
                self.Buscar_categoria()

            elif filtro == 5:
                break

            else:
                print("Opción no válida")


    def Buscar_puntuacion(self):
        puntaje = int(input('Ingrese un puntaje (1-5): '))
        self.dfe = self.df1.sort_values('Puntuación',ascending=False)
        self.dfe = self.dfe.drop(['Autor','Categoria','Año_publicado'], axis=1)

        if puntaje == 1:
            self.dfe = self.dfe[self.dfe.Puntuación < 2]
            self.dfe = self.dfe[self.dfe.Puntuación >= 1]

        elif puntaje == 2:
            self.dfe = self.dfe[self.dfe.Puntuación < 3]
            self.dfe = self.dfe[self.dfe.Puntuación >= 2]

        elif puntaje == 3:
            self.dfe = self.dfe[self.dfe.Puntuación < 4]
            self.dfe = self.dfe[self.dfe.Puntuación >= 3]

        elif puntaje == 4:
            self.dfe = self.dfe[self.dfe.Puntuación < 5]
            self.dfe = self.dfe[self.dfe.Puntuación >= 4]

        elif puntaje == 5:
            self.dfe = self.dfe[self.dfe.Puntuación == 5]

        elif puntaje == 0:
            self.dfe = self.dfe[self.dfe.Puntuación < 1]
            self.dfe = self.dfe[self.dfe.Puntuación >= 0]

        print(self.dfe.head(10))

    def Buscar_fecha(self):
        print("Escoger orden:  \n")
        print("1- Recientes -> Antiguos")
        print("2- Antiguos -> Recientes")
        orden = int(input('Escoja una opción: '))
        
        self.dff = self.df1.drop(['Autor','Categoria','Puntuación'], axis=1)
        
        if orden == 1:
            self.dff = self.dff.sort_values('Año_publicado',ascending=False)
        
        elif orden== 2:
            self.dff = self.dff.sort_values('Año_publicado')

        print(self.dff.head(10))

    def Buscar_categoria(self):
        print("Escoger categoria:  \n")
        print("1- Ficción ")
        print("2- Policial")
        print("3- Lit.cristiana")
        print("4- Historia")
        print("5- Informativo")
        print("6- Aventura")
        print("7- Romance")
        print("8- Drama")
        print("9- Economia")
        print("10- Literatura")
        print("11- Psicologia")
        print("12- Filosofia")
        print("13- Ciencia")
        print("14- Recreación")
        print("15- Terror")
        categoria = int(input('Escoja una categoría: '))

        if categoria == 1:
            self.dfc=self.df1[self.df1['Categoria']=='Ficción']['Titulo']

        elif categoria == 2:
            self.dfc=self.df1[self.df1['Categoria']=='Policial']['Titulo']

        elif categoria == 3:
            self.dfc=self.df1[self.df1['Categoria']=='Lit.cristiana']['Titulo']

        elif categoria == 4:
            self.dfc=self.df1[self.df1['Categoria']=='Historia']['Titulo']

        elif categoria == 5:
            self.dfc=self.df1[self.df1['Categoria']=='Informativo']['Titulo']

        elif categoria == 6:                                                 
            self.dfc=self.df1[self.df1['Categoria']=='Aventura']['Titulo']

        elif categoria == 7:
            self.dfc=self.df1[self.df1['Categoria']=='Romance']['Titulo']

        elif categoria == 8:
            self.dfc=self.df1[self.df1['Categoria']=='Drama']['Titulo']

        elif categoria == 9:
            self.dfc=self.df1[self.df1['Categoria']=='Economia']['Titulo']

        elif categoria == 10:
            self.dfc=self.df1[self.df1['Categoria']=='Literatura']['Titulo']

        elif categoria == 11:
            self.dfc=self.df1[self.df1['Categoria']=='Psicologia']['Titulo']

        elif categoria == 12:
            self.dfc=self.df1[self.df1['Categoria']=='Filosofia']['Titulo']

        elif categoria == 13:
            self.dfc=self.df1[self.df1['Categoria']=='Ciencia']['Titulo']

        elif categoria == 14:
            self.dfc=self.df1[self.df1['Categoria']=='Recreacion']['Titulo']

        elif categoria == 15:
            self.dfc=self.df1[self.df1['Categoria']=='Terror']['Titulo']
            
        print(self.dfc.head(10))

    def recom_populares(self):
        """ 
        Recomendación por popularidad. 
        Recomienda al usuario libros 
        que tienen entre 3 y 5 estrellas
        """
        punt = 0
        self.dfp = self.df1.sort_values('Puntuación', ascending = False)
        self.dfp = self.dfp.drop(['Autor','Categoria','Año_publicado'], axis=1)

        if punt == 0:
            self.dfp = self.dfp[self.dfp.Puntuación >3]
            self.dfp = self.dfp[self.dfp.Puntuación <= 5]
        print(self.dfp.head(10))

    
    def Recomendar(self):
        while(True):
            print("-- Descubrir -- ")
            print("1- Trending books")
            print("2- Recomendación por categoría")
            print("3- Recomendación por autor")
            print("4- Regresar")
            recomendacion = int(input('Escoja una opción: '))
            
            if recomendacion == 1:
                print("- Los libros más populares -")
                self.recom_populares()

            elif recomendacion == 2:
                print("- Recomendación por categoría -")

                #importar libro de libros leidos
                self.archivo_leidos = open("leidos.txt", "r")
                self.linea = self.archivo_leidos.readline()
                self.archivo_leidos.close()
                self.linea = self.linea.replace("\n", "")  #remplazar el "\n"
                #encontrar categoria teniendo el titulo
                self.df2 = self.df1[self.df1['Titulo']==self.linea]['Categoria']
                self.df2 = self.df2.head(1)
                #Se ajustan los datos para obtener un str con el nombre de la categoria
                self.df2 = self.df2.to_string(index=False)
                self.df2 = self.df2.replace("\n", "")
                self.df2 = self.df2.replace(" ", "")
                #Recomendar por categoria y puntuación
                self.df2 = self.df1.loc[self.df1['Categoria'] == self.df2]
                self.df2 = self.df2.sort_values('Puntuación',ascending=False)
                self.df2 = self.df2.drop(['Autor'], axis=1)
                print(self.df2.head(15))

            elif recomendacion == 3:
                print("- Recomendación por autor -")

                self.archivo_leidos = open("leidos.txt", "r")
                self.linea = self.archivo_leidos.readline()
                self.archivo_leidos.close()
                self.linea = self.linea.replace("\n", "")  #remplazar el "\n"
                #encontrar autor teniendo el titulo
                self.df2 = self.df1[self.df1['Titulo']==self.linea]['Autor']
                self.df2 = self.df2.head(1)
                #Se ajustan los datos para obtener un str con el nombre del autor
                self.df2 = self.df2.to_string(index=False)
                self.df2 = self.df2.replace("\n", "")
                #Recomendar por autor y puntuación
                self.df2 = self.df1.loc[self.df1['Autor'] == self.df2]
                self.df2 = self.df2.sort_values('Puntuación',ascending=False)
                print(self.df2.head(15))
            
            elif recomendacion == 4:
                break

            else:
                raise TypeError
                

    def Menu(self):
        while(True):
            print("\n* -Menú- * ")
            print("1- Mostrar libros")
            print("2- Buscar")
            print("3- Estante Libros Leídos")
            print("4- Estante Quiero Leer")
            print("5- Descubre")
            print("6- Salir del menú")
            opcion1=int(input("Escoja una opción: "))
        
            if opcion1 == 1:
                print("- LIBROS -: \n")
                self.mostrar_libros()

            elif opcion1 == 2:
                print(" - BUSCAR -")
                self.Buscar()

            elif opcion1 == 3:
                self.estante_leidos()
                
            elif opcion1 == 4:
                self.estante_quieroleer()

            elif opcion1 == 5:
                self.Recomendar()
                
            elif opcion1 == 6:
                break

            else:
                print("Opción no válida")

