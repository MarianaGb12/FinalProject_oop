#%%
from basededatos import Basededatos

class Menu(Basededatos):    
    def mostrar_libros(self):
        self.dfm=self.df1
        print(self.dfm.head(10))

    def buscar(self, t:str):
        self.dfb = self.df1.loc[self.df1['Titulo'] == t]
        print(self.dfb.head(10))

    def estrellas(self, x):
        self.dfe = self.df1.sort_values('Puntuación',ascending=False)
        self.dfe = self.dfe.drop(['Autor','Categoria','Año_publicado'], axis=1)
        if x == 1:
            self.dfe = self.dfe[self.dfe.Puntuación < 2]
            self.dfe = self.dfe[self.dfe.Puntuación >= 1]
        elif x == 2:
            self.dfe = self.dfe[self.dfe.Puntuación < 3]
            self.dfe = self.dfe[self.dfe.Puntuación >= 2]
        elif x == 3:
            self.dfe = self.dfe[self.dfe.Puntuación < 4]
            self.dfe = self.dfe[self.dfe.Puntuación >= 3]
        elif x == 4:
            self.dfe = self.dfe[self.dfe.Puntuación < 5]
            self.dfe = self.dfe[self.dfe.Puntuación >= 4]
        elif x == 5:
            self.dfe = self.dfe[self.dfe.Puntuación == 5]
        elif x == 0:
            self.dfe = self.dfe[self.dfe.Puntuación < 1]
            self.dfe = self.dfe[self.dfe.Puntuación >= 0]
        print(self.dfe.head(10))

    def fecha(self, f):
        self.dff = self.df1.drop(['Autor','Categoria','Puntuación'], axis=1)
        if f == 1:
            self.dff = self.dff.sort_values('Año_publicado',ascending=False)
        elif f== 2:
            self.dff = self.dff.sort_values('Año_publicado')
        print(self.dff.head(10))

    def categoria(self, c):
        if c == 1:
            self.dfc=self.df1[self.df1['Categoria']=='Ficción']['Titulo']
        elif c == 2:
            self.dfc=self.df1[self.df1['Categoria']=='Policial']['Titulo']
        elif c == 3:
            self.dfc=self.df1[self.df1['Categoria']=='Lit.cristiana']['Titulo']
        elif c == 4:
            self.dfc=self.df1[self.df1['Categoria']=='Historia']['Titulo']
        elif c == 5:
            self.dfc=self.df1[self.df1['Categoria']=='Informativo']['Titulo']
        elif c == 6:                                                 
            self.dfc=self.df1[self.df1['Categoria']=='Aventura']['Titulo']
        elif c == 7:
            self.dfc=self.df1[self.df1['Categoria']=='Romance']['Titulo']
        elif c == 8:
            self.dfc=self.df1[self.df1['Categoria']=='Drama']['Titulo']
        elif c == 9:
            self.dfc=self.df1[self.df1['Categoria']=='Economia']['Titulo']
        elif c == 10:
            self.dfc=self.df1[self.df1['Categoria']=='Literatura']['Titulo']
        elif c == 11:
            self.dfc=self.df1[self.df1['Categoria']=='Psicologia']['Titulo']
        elif c == 12:
            self.dfc=self.df1[self.df1['Categoria']=='Filosofia']['Titulo']
        elif c == 13:
            self.dfc=self.df1[self.df1['Categoria']=='Ciencia']['Titulo']
        elif c == 14:
            self.dfc=self.df1[self.df1['Categoria']=='Recreacion']['Titulo']
        elif c == 15:
            self.dfc=self.df1[self.df1['Categoria']=='Terror']['Titulo']
            
        print(self.dfc.head(10))

    def leidos(self):
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
                    librousuario = input("Ingrese el título: \n")
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

    def recomendar(self, r):
        
        while (True):
            if r == 1:

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

            elif r == 2:

                self.archivo_leidos = open("leidos.txt", "r")
                self.linea = self.archivo_leidos.readline()
                self.archivo_leidos.close()
                self.linea = self.linea.replace("\n", "")  #remplazar el "\n"
                #encontrar categoria teniendo el titulo
                self.df2 = self.df1[self.df1['Titulo']==self.linea]['Autor']
                self.df2 = self.df2.head(1)
                #Se ajustan los datos para obtener un str con el nombre de la categoria
                self.df2 = self.df2.to_string(index=False)
                self.df2 = self.df2.replace("\n", "")
                #Recomendar por categoria y puntuación
                self.df2 = self.df1.loc[self.df1['Autor'] == self.df2]
                self.df2 = self.df2.sort_values('Puntuación',ascending=False)
            
            else:
                print("Opción inválida")
                print("\n Recomendar por: ")
                print("1- Categoria")
                print("2- Autor")
                r= int(input('Escoja una opción: '))
                
            print(self.df2)


    def menu(self):
        while(True):
            print("\n* -Menú- * ")
            print("1- Mostrar libros")
            print("2- Buscar")
            print("3- Buscar con filtros")
            print("4- Libros Leídos")
            print("5- Ver recomendaciones")
            print("6- Salir del menú")
            opcion1=int(input("Escoja una opción: "))
        
            if opcion1 == 1:
                print("Libros disponibles: \n")
                self.mostrar_libros()

            elif opcion1 == 2:
                t= str(input('Ingrese titulo del libro: '))
                self.buscar(t)

            elif opcion1 == 3:
                print("Escoja un filtro:  \n")
                print("1- Puntuación (Estrellas)")
                print("2- Fecha de publicación")
                print("3- Categoria")
                filtro=int(input("Escoja una opción: "))
                
                if filtro == 1:
                    print("Puntuación \n")
                    x= int(input('Ingrese numero de estrellas: '))
                    self.estrellas(x)

                elif filtro == 2:
                    print("Fecha de publicación \n")
                    print("Escoger orden:  \n")
                    print("1- Antiguos")
                    print("2- Recientes")
                    f= int(input('Escoja una opción: '))
                    self.fecha(f)

                elif filtro == 3:
                    print("Categoria \n")
                    print("Escoger categoria:  \n")
                    print("1- Ficción \n")
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
                    c= int(input('Escoja una opción: '))
                    self.categoria(c)
                else:
                    print("Opción no válida")

            elif opcion1 == 4:
                self.leidos()

            elif opcion1 == 5:
            
                while (True):
                    print("\n Recomendar por: ")
                    print("1- Categoria")
                    print("2- Autor")
                    print("3- Regresar")
                    r= int(input('Escoja una opción: '))
                    if r == 3:
                        break
                    else:
                        return self.recomendar(r)
                
            elif opcion1 == 6:
                break

            else:
                print("Opción no válida")


#%%
muestra= Menu()
muestra.menu()