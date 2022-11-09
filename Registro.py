class Usuario:
    def __init__(self):
        pass
    
    def Registro(self):
        print("Nuevo registro. Introduza sus datos ")
        self.nomusuario = input("Nombre de usuario:")
        self.contraseña = input("Contraseña:")
        self.Registro_usuario()
    
    def Registro_usuario(self):
        usuario_info = self.nomusuario
        contraseña_info = self.contraseña
    
        file = open("usuarios.txt", "w") #CREACION DE ARCHIVO CON "nombre" y "clave"
        file.write(usuario_info + "\n")
        file.write(contraseña_info)
        file.close()

        print("Registro completado con éxito")

    def Iniciarsesion(self ):
        while(True):
            eleccion = int(input(print("1) Iniciar Sesión || 2) Nuevo Registro || 3)Salir")))
            if eleccion == 1:
                self.Verifica_login()
            elif eleccion == 2:
                self.Registro()
            elif eleccion == 3:
                break
            else:
                print("Intente más tarde")
        

    def Verifica_login(self):
        pass
        
        
    
    def exito_login(self):
        print("Ha ingresado con exito")

# "Contraseña incorrecta".
 
    def no_cont(self):
        print("Contraseña incorrecta ")
 
# "Usuario no encontrado".
    def no_usuario(self):
        print("Usuario no encontrado")
# %%
cuenta = Usuario()
cuenta.Iniciarsesion()
