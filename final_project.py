#%%
class Register:
    num_usuarios = 0
    def _init_(self, nomusuario:str, contraseña:str ) -> None:
        self.nomusuario = nomusuario
        self.contraseña = contraseña
        
        self.conectar = False
        self.intento = 3
        
        
        Register.num_usuarios+=1

        
    def login(self):
        nomusuario1 = input("Ingrese nombre de usuario:")
        contraseña1 = input("Ingrese contraseña:")
        if contraseña1 == self.contraseña and nomusuario1 == self.nomusuario:
            print ("Ingreso con éxito")
            self.conectar = True
        else:
            self.intento-=1
            if self.intento > 0:
              print ("Error.Intentelo nuevamente")
              print("Usuario o contraseña incorrecto")
              self.login()
            else:
              print ("Inténtelo más tarde.")

            
    def close(self):
        if self.conectar:
            print("Salida con éxito")
            self.conectar = False
            
cuenta = Register(input("Ingrese su usuario: "),input("Ingrese constraseña:") )
print(cuenta )
cuenta.login()

class Usuario (Register):
    def _init_(self, nomusuario, contraseña) -> None:
        super().init(nomusuario, contraseña)

