#%%
class Register:
    num_usuarios = 0
    def __init__(self, nomusuario:str, contraseña:str ) -> None:
        self.nomusuario = nomusuario
        self.contraseña = contraseña
        
        self.conectar = False
        self.intento = 3
        
        
        Register.num_usuarios+=1

        
    def iniciarsesion(self):
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

# %%
class Buscador:
    def __init__(self, opcion:int):
        self.opcion = opcion

# %%
class Menu(Buscador):
    def __init__(self, opcion) -> None:
        super().__init__(Buscador)
    
    def Buscar(self):
        while(True):
            print("* -Menú- * ")
            print("1- Mostrar libros")
            print("2- Buscar por titulo")
            print("3- Buscar por categoría")
            print("4- Ver recomendaciones")
            print("5- Agregar a Libros Leídos")
            print("6- Agregar a Quiero Leer")
            print("7- Salir del menú")
            opcion1=int(input("Escoja una opción: "))
        
            if opcion1==1:
                print("*** LISTA DE LIBROS ***")
                with open("libros1.txt") as archivo:
                    print(archivo.readlines())
                print("\n")

            elif opcion1==2:
                ...

            elif opcion1==3:
                ...

            elif opcion1==4:
                ...
            
            elif opcion1==5:
                print("Agregar libro a Estante Leídos")
                librosleidos = []
                nuevolibro = input("¿Desea añadir un libro a leídos: 1)Si o 2)No")
                while nuevolibro == "1":
                    librousuario = input("Ingrese el título: ")
                    librosleidos.append(librousuario)
                    nuevolibro = input("¿Desea añadir más libros: 1)Si , 2)No")
                
                print(librosleidos)

            elif opcion1==6:
                print("Agregar libro a Estante Quiero Leer")
                wanttoread = []
                nuevlibro = input("¿Desea añadir un libro a Quiero Leer: 1)Si , 2)No")
                while nuevlibro == "1":
                    libro_usuario = input("Ingrese título: ")
                    wanttoread.append(libro_usuario)
                    nuevlibro = input("¿Desea añadir más libros: 1)Si , 2)No")
                print(wanttoread)

            elif opcion1==7:
                break

            else:
                print("Opción no válida")
            

            
search = Menu("")
search.Buscar()

