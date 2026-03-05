
def login():
    
    u = "admin"
    c = "123"
    
    while True:
        
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        
        if usuario == u and contraseña == c:
            print("Login exitoso")
            break
        else: 
            print("Credenciales incorrectas")

login()