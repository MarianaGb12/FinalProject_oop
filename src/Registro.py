from Menu_secundario import Menu_secundario


class Usuario:
    def __init__(self):
        pass

    def Registro(self):
        print("\n------------------------------------------------")
        print("Nuevo registro. Introduza sus datos ")
        self.nomusuario = input("Nombre de usuario:")
        self.contraseña = input("Contraseña:")
        self.Registro_usuario()

    def Registro_usuario(self):
        # Lectura de archivo, para verificar que no exista el usuario
        file = open("DB/usuarios.txt", "r")
        info = file.read()
        if self.nomusuario in info:
            print("Usuario ya existe. Por favor intente nuevamente")
        else:
            # CREACION DE Archivo CON "nombre" y "contraseña" del usuario
            file = open("DB/usuarios.txt", "w")
            info = (info + " " + self.nomusuario + " " + self.contraseña)
            file.write(info)
            file.close()
            self.exito_registro()
        file.close()

    def Verifica_login(self):
        print("\nAcceso a la cuenta. Introduza sus datos ")
        self.nomusuario = (input("Nombre de usuario:"))
        self.contraseña = (input("Contraseña:"))

        # CREACION DE ARCHIVO CON "nombre" y "contraseña" en modo lectura
        file = open("DB/usuarios.txt", "r")
        leer = file.read()
        leer = leer.split()

        """
        Se verifica que el usuario se encuentre en el archivo.
        Si es asi, se verifica la contraseña en el mismo. 
        Si esta no es igual, arroja un error para el nombre de 
        usuario o contraseña ingresados. 
        """
        if self.nomusuario in leer:
            index = leer.index(self.nomusuario) + 1
            contraseña_usuario = leer[index]
            if contraseña_usuario == self.contraseña:
                return self.exito_login(self.nomusuario)
            else:
                return self.no_cont()
        else:
            return self.no_usuario()

    # "Inicio de sesión exitoso"
    def exito_login(self, nomusuario):
        print("Ha ingresado con éxito")
        menu = Menu_secundario()
        menu.Menu(nomusuario)

    # "El usuario se ha registrado correctamente"
    def exito_registro(self):
        print("Registro completado con éxito")

    # "Contraseña incorrecta".

    def no_cont(self):
        print("Contraseña incorrecta ")

    # "Usuario no encontrado".
    def no_usuario(self):
        print("Usuario no encontrado")
