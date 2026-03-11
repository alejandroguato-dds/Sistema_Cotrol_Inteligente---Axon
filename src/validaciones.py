
def pedir_texto(mensaje):
    
    while True:
        
        dato = input(mensaje).strip()
        
        if dato == "":
            print("\nEs necesario realizar una acción")
        else:
            return dato
        
def pedir_numero(mensaje):
    
    while True:
        
        dato = input(mensaje).strip()
        
        if dato == "":
            print("No se puede dejar vacio")
            continue
        
        if not dato.isdigit():
            print("De ingresar un número")
            continue
        
        return int(dato)
    
    