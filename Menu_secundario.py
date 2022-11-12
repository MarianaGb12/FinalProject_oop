from Libros import Libros
from Recomendaciones import Recomendar
from Buscador import Buscador


class Menu_secundario:
    def __init__(self):
        pass

    def Menu(self):
        # Menú para la opciones que se pueden realizar en el programa
        while (True):
            print("-----------------------------------------------------")
            print("                        Menú                       ")
            print("1- Mostrar libros")
            print("2- Buscar")
            print("3- Estante Libros Leídos")
            print("4- Estante Quiero Leer")
            print("5- Descubre")
            print("6- Cerrar Sesión")
            opcion1 = int(input("Escoja una opción: "))

            if opcion1 == 1:
                print(
                    "-----------------------------------------------------------------")
                print(
                    "                           LIBROS                                ")
                mostrar = Libros("")
                mostrar.mostrar_libros()

            elif opcion1 == 2:
                buscar = Buscador("")
                buscar.Buscar()

            elif opcion1 == 3:
                mostrar = Libros("")
                mostrar.estante_leidos()

            elif opcion1 == 4:
                mostrar = Libros("")
                mostrar.estante_quieroleer()

            elif opcion1 == 5:
                recomendar = Recomendar("")
                recomendar.Recomendar()

            elif opcion1 == 6:
                break

            else:
                print("Opción no válida")
