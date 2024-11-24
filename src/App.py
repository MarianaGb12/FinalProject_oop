from Registro import Usuario


class App:
    def __init__(self, Opcion: int):
        self.Opcion = Opcion


class Menu_principal(App):
    def __init__(self, Opcion):
        super().__init__(Opcion)

    def menu_principal(self):
        while True:
            try:
                print("\n------------------------------------------------")
                print("                     BOOKS                      ")
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
                    print(f"\nOpción invalida, por favor vuelva a escoger una opción:\n")
                    

            except ValueError as e:
                print(f"\nNo se ingresó ninguna opción.\nError: {e}\n")
                
                    
                
