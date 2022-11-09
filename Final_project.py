# %%
class Buscador:
    def __init__(self, opcion1:int):
        self.opcion1 = opcion1

# %%
class Menu(Buscador):
    def __init__(self, opcion1) -> None:
        super().__init__(Buscador)

    def buscador(self):
        # try catch except para manejar
        # error la búsqueda
        # iniciando bloque try
        try:
            # apertura del archivo de libros
            # como lectura 
            archivo1_buscar = open("libros.txt", "r")
                
            # ingreso del string (titulo,autor,categoria) que el 
            # usuario desea buscar
            searching = input("Ingrese título, autor o categoría: ")
                
            # lectura del archivo línea por línea
            lines = archivo1_buscar.readlines()
                
            nueva_lista = []
            idx = 0
                
            # looping en cada línea del archivo
            for line in lines:
                # si la línea tiene la palabra ingresada, toma
                # la posición de la línea y la coloca
                # en una nueva lista 
                if searching in line:
                    nueva_lista.insert(idx, line)
                    idx += 1

            # cierre del archivo
            archivo1_buscar.close()
            
            # si el lenght de la nueva lista es 0
            # el input no se encuentra en el archivo 
            if len(nueva_lista)==0:
                print("\n\"" +searching+ "\" no se encuentra en \"" +archivo1_buscar+ "\"!")
            else:
                # visualizar líneas que  
                # contienen el input ingresado
                lineLen = len(nueva_lista)
                print("\n - Buscando \"" +searching+ "\"- \n")
                for i in range(lineLen):
                    print(end=nueva_lista[i])
                print()
                
        # iniciando bloque except 
        except :
            print("\n Error en la búsqueda")
    
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
        while(True):
            print("\n* -Menú- * ")
            print("1- Mostrar libros")
            print("2- Buscador")
            print("3- Ver recomendaciones")
            print("4- Estante Libros Leídos")
            print("5- Agregar a Quiero Leer")
            print("6- Salir del menú")
            opcion1=int(input("Escoja una opción: "))
        
            if opcion1 == 1:
                print("\n*** LISTA DE LIBROS ***")
                with open("libros1.txt") as archivo:
                    print(archivo.readlines())
                print("\n")
                    
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

            elif opcion1 == 2:
                print("*** Buscador ***")
                self.buscador()
            
            elif opcion1 == 3:
                ...

            elif opcion1 == 4:
                self.estante_leidos()

            elif opcion1 == 5:
                self.estante_quieroleer()

            elif opcion1 == 6:
                break

            else:
                print("Opción no válida")
                
