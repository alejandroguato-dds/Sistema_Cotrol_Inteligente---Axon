
import getpass
from validaciones import pedir_numero,pedir_texto

# Login apartado solo para el inicio del admin
def login_admin():
    
   while True:
       
       user = pedir_texto("Usuario: ")
       password = getpass.getpass("Contraseña: ")
       
       if password.strip() == "":
           print("No se puede dejar vacio")
           continue
       
       with open("admin/usuarios.txt" , "r") as archivo:
           
           for linea in archivo: 
               
               u, c, rol = linea.strip().split(",")
               
               if user == u and password == c and rol == "admin":
                   print("\nLogin exitoso")
                   return "admin"
        
       print("\nCredenciales incorrectas--")


def login_usuario():
    
    while True:
        
        user = pedir_texto("Usuario: ")
        password = getpass.getpass("Contraseña: ")
        
        if password.strip() == "":
            print("No se puede dejar vacio")
            continue
        
        with open("admin/usuarios.txt", "r") as archivo:
            
            for linea in archivo:
                
                u, c, rol = linea.strip().split(",")
                
                if user == u and password == c and rol == "colaborador":
                    print("Login exitoso")
                    return "colaborador"
                
        print("\nCredenciales incorrectas")
    

def login():
    
    while True:
        
        print("\n------LOGIN AXON-------")
        print("1. Administrador")
        print("2. Usuario")
        print("3. Salir del programa")
        
        opcion = pedir_numero("\nIngrese una opción: ")
        
        if opcion == 1:
            return login_admin()
            
        
        elif opcion == 2:
            return login_usuario()
        
        elif opcion == 3:
            return "salir"
        
        else:
            print("Opción no valida")    

