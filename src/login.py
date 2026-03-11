
import getpass
from menu import menu_principal_usuario
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
                   
                   panel_admin()
                   return
        
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
                    menu_principal_usuario()
                    return
        print("\nCredenciales incorrectas")
    

def agregar_colaboradores():
    
    user = pedir_texto("Nuevo usuario: ")
    password = input("Contraseña: ")
    rol = "colaborador"
    
    while True:
        if password.strip() == "":
            print("No se puede dejar al colaborador sin contraseña asignada")
        else:
            break
        
    with open("admin/usuarios.txt", "a") as archivo:
        archivo.write(f"{user},{password},{rol}\n")
    
    print("\nUsuario agregado correctamente")        


def panel_admin():
    
    while True:
        print("\n----Panel Admin-----")
        print("1. Agregar colaborador")
        print("2. Salir")
        
        opcion = pedir_numero("Selecciona una opción: ")
        
        if opcion == 1:
            agregar_colaboradores()
        elif opcion == 2:
            break
        

def login():
    
    while True:
        
        print("\n------LOGIN AXON-------")
        print("1. Administrador")
        print("2. Usuario")
        
        opcion = pedir_numero("Ingrese una opción: ")
        
        if opcion == 1:
            login_admin()
            
        
        elif opcion == 2:
            login_usuario()
            
        
        else:
            print("Opción no valida")    

login()