from BaseDeDatos import Basededatos

class Libros(Basededatos):
    def __init__(self, df1: str):
        super().__init__(df1)

    def mostrar_libros(self):
        # aparecen lista de libros en consola
        print(self.df1.head(30))
        """
        Menú para que el usuario lea 
        o modifique la estantería de libros.
        """
        while(True):
            print("Desea agregar libros a su estante ")
            op = int(input("1-Si || 2-No : "))
            if op == 1:
                op2 = int(input("1)Estantería LIBROS LEÍDOS || 2)Estantería QUIERO LEER || 3) Atrás:  "))
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
        print("-----------------------------------------------------")
        print("               Estante LIBROS LEÍDOS                 ")
        while (True):
            print("1- Agregar libro a leídos || 2-Ver estante LIBROS LEÍDOS || 3-Atrás")
            opcion2 = int(input("Escoja una opción: "))

            if opcion2 == 1:  
                # apertura del archivo en modo escritura
                archivo_leidos = open("leidos.txt", "w")
                # se crea lista para libros leídos
                librosleidos = []
                while(True):
                    nuevolibro = int(input(" 1-Añadir libro || 2-Regresar : "))
                    if nuevolibro == 1:
                        librousuario = input("Ingrese el título: ")
                        librosleidos.append(librousuario)
                    elif nuevolibro == 2:
                        break
                    else:
                        return TypeError
                # recorremos la lista y agregamos cada titulo al archivo
                for leido in librosleidos:
                    print(leido, file = archivo_leidos)
                # cierre del archivo
                archivo_leidos.close()

            elif opcion2 == 2:
                print("-----------------------------------------------------")
                print("                 LIBROS LEÍDOS                       ")
                # visualización del estante libros leídos
                with open("leidos.txt") as archivo:
                    print(archivo.readlines())
                print("\n")

            elif opcion2 == 3:
                break
            else:
                print("Opción inválida")

    def estante_quieroleer(self):
        print("-----------------------------------------------------")
        print("                Estante QUIERO LEER                  ")
        while (True):
            print("1- Agregar libro a Quiero Leer || 2-Ver estante QUIERO LEER || 3-Atrás")
            opcion3 = int(input("Escoja una opción: "))
            if opcion3 == 1:
                # apertura del archivo en modo escritura
                archivo_quieroleer = open("quiero_leer.txt", "w")
                # creación de lista quiero leer
                wanttoread = []
                while(True):
                    nuevlibro = int(input(" 1-Añadir libro || 2-Regresar "))
                    if nuevlibro == 1:
                        libro_usuario = input("Ingrese título: ")
                        wanttoread.append(libro_usuario) # se guardan los libros en lista
                    elif nuevlibro == 2:
                        break
                    else:
                        return TypeError

                # Recorremos la lista y agregamos cada titulo al archivo
                for want in wanttoread:
                    print(want, file=archivo_quieroleer)
                # cierre del archivo
                archivo_quieroleer.close()

            elif opcion3 == 2:
                print("-----------------------------------------------------")
                print("                  QUIERO LEER                        ")
                # visualización del estante quiero leer
                with open("quiero_leer.txt") as archivo:
                    print(archivo.readlines())
                print("\n")

            elif opcion3 == 3:
                break

            else:
                print("Opción inválida")
