from Registro import Usuario


class App:
    def __init__(self, Opcion: int):
        self.Opcion = Opcion


class Menu_principal(App):
    def __init__(self, Opcion):
        super().__init__(Opcion)

    def menu_principal(self):
        while (True):
            print("--------------------------------------------")
            print("                   BOOKS                    ")
            print("1- Iniciar Sesión")
            print("2- Nuevo Registro")
            print("3- Salir")
            Opcion = int(input("Escoja una opción: "))
            if Opcion == 1:
                usuario = Usuario()
                usuario.Verifica_login()

            elif Opcion == 2:
                usuario = Usuario()
                usuario.Registro()

            elif Opcion == 3:
                break

            else:
                raise TypeError
