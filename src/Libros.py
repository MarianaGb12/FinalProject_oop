from BaseDeDatos import Basededatos
import json

class Libros(Basededatos):
    def __init__(self, df1: str):
        super().__init__(df1)

    def mostrar_libros(self, nomusuario):
        # aparecen lista de libros en consola
        print(self.df1.head(30))
        """
        Menú para que el usuario lea 
        o modifique la estantería de libros.
        """
        while(True):
            try:
                print("Desea agregar libros a su estante ")
                op = int(input("1-Si || 2-No : "))
                if op == 1:
                    try:
                        print("\nEscoja la estantantería a la que desea agregar libros: ")
                        op2 = int(input("1) Estantería LIBROS LEÍDOS || 2) Estantería QUIERO LEER || 3) Atrás:  "))
                        if op2 == 1: 
                            self.estante_leidos(nomusuario)

                        elif op2 == 2:
                            self.estante_quieroleer(nomusuario)
                                    
                        elif op2 == 3:
                            break
                        else:
                            print(f"\nOpción inválida, por favor vuelva a escoger una opción:\n")
                    
                    except ValueError as e:
                        print(f"\nNo se ingresó ninguna opción.\nError: {e}\n")

                elif op == 2:
                    break

                else:
                    print(f"\nOpción inválida, por favor vuelva a escoger una opción:\n")
            
            except ValueError as e:
                print(f"\nNo se ingresó ninguna opción.\nError: {e}\n")

    def estante_leidos(self, nomusuario):
        print("\n-----------------------------------------------------")
        print("               Estante LIBROS LEÍDOS                 ")
        username = nomusuario
        while (True):
            try:
                print("\n1) Agregar libro a leídos\n2) Ver estante LIBROS LEÍDOS\n3) Atrás")
                opcion2 = int(input("Escoja una opción: "))

                if opcion2 == 1:  
                    while(True):
                        # Cargar datos existentes de libros leídos
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

                        # Asegurarse de que el usuario tenga una entrada en el diccionario
                        if username not in libros_leidos:
                            libros_leidos[username] = []
                            
                        try:
                            nuevolibro = int(input("\n1-Añadir libro || 2-Regresar : "))
                            if nuevolibro == 1:
                                librousuario = input("Ingrese el título: ")
                                libros_leidos[username].append(librousuario)
                                print("Libro añadido\n")
                            elif nuevolibro == 2:
                                break
                            else:
                                print(f"\nOpción inválida, por favor vuelva a escoger una opción:\n")
                        except ValueError as e:
                            print(f"\nNo se ingresó ninguna opción.\nError: {e}\n")


                        # Guardar los datos actualizados en el archivo JSON
                        with open("DB/leidos.json", "w") as archivo_leidos:
                            json.dump(libros_leidos, archivo_leidos, indent=4)

                elif opcion2 == 2:
                    print("\n-----------------------------------------------------")
                    print("                 LIBROS LEÍDOS                       ")
                    # visualización del estante libros leídos
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

                    # Acceder a la lista de libros del usuario
                    if username in libros_leidos:
                        libros_usuario = libros_leidos[username]
                        for libro in libros_usuario: print(f"- {libro}")
                        print("")
                    else:
                        print(f"No se encontraron libros leídos para el usuario {username}")

                elif opcion2 == 3:
                    break
                else:
                    print(f"\nOpción inválida, por favor vuelva a escoger una opción:\n")

            except ValueError as e:
                print(f"\nNo se ingresó ninguna opción.\nError: {e}\n")

    def estante_quieroleer(self, nomusuario):
        print("\n-----------------------------------------------------")
        print("                Estante QUIERO LEER                  ")
        username = nomusuario
        while (True):
            try:
                print("1- Agregar libro a Quiero Leer || 2-Ver estante QUIERO LEER || 3-Atrás")
                opcion3 = int(input("Escoja una opción: "))

                if opcion3 == 1:  
                        while(True):
                            # Cargar datos existentes de libros leídos
                            try:
                                with open("DB/quieroleer.json", "r") as archivo_quieroleer:
                                    libros_quieroleer = json.load(archivo_quieroleer)
                            except FileNotFoundError:
                                print("No se encontró el archivo de libros leídos")
                                libros_quieroleer = {}
                            except json.JSONDecodeError as e:
                                print(f"Error al decodificar JSON: {e}")
                                libros_quieroleer = {}
                            except Exception as e:
                                print(f"Error inesperado: {e}")
                                libros_quieroleer = {}

                            # Asegurarse de que el usuario tenga una entrada en el diccionario
                            if username not in libros_quieroleer:
                                libros_quieroleer[username] = []
                                
                            try:
                                nuevolibro = int(input("\n1-Añadir libro || 2-Regresar : "))
                                if nuevolibro == 1:
                                    librousuario = input("Ingrese el título: ")
                                    libros_quieroleer[username].append(librousuario)
                                    print("Libro añadido\n")
                                elif nuevolibro == 2:
                                    break
                                else:
                                    print(f"\nOpción inválida, por favor vuelva a escoger una opción:\n")
                            except ValueError as e:
                                print(f"\nNo se ingresó ninguna opción.\nError: {e}\n")


                            # Guardar los datos actualizados en el archivo JSON
                            with open("DB/quieroleer.json", "w") as archivo_quieroleer:
                                json.dump(libros_quieroleer, archivo_quieroleer, indent=4)


                elif opcion3 == 2:
                    print("\n-----------------------------------------------------")
                    print("                  QUIERO LEER                        ")
                    # visualización del estante libros quiero leer
                    try:
                        with open("DB/quieroleer.json", "r") as archivo_quieroleer:
                            libros_quieroleer = json.load(archivo_quieroleer)
                    except FileNotFoundError:
                        print("\nNo se encontró el archivo de libros que quieres leer")
                        libros_quieroleer = {}
                    except json.JSONDecodeError as e:
                        print(f"\nError al decodificar JSON: {e}")
                        libros_quieroleer = {}
                    except Exception as e:
                        print(f"\nError inesperado: {e}")
                        libros_quieroleer = {}

                    # Acceder a la lista de libros del usuario
                    if username in libros_quieroleer:
                        libros_usuario = libros_quieroleer[username]
                        for libro in libros_usuario: print(f"- {libro}")
                        print("")
                    else:
                        print(f"No se encontraron libros leídos para el usuario {username}")


                elif opcion3 == 3:
                    break

                else:
                    print("Opción inválida")
            except ValueError as e:
                print(f"\nNo se ingresó ninguna opción.\nError: {e}\n")
