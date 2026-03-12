from validaciones import pedir_numero,pedir_texto

def menu_principal_usuario():
    while True:
        print("\n------- AXON -------")
        print("-" * 25)
        print("1. Gestión de productos")
        print("2. Ventas")
        print("3. Salir")
        print("-" * 25)
        opcion = input("Seleccione una opción: ")
        print("-" * 25)

        if opcion == "1":
            print("Módulo de productos (en construcción)")
        elif opcion == "2":
            print("Módulo de ventas (en construcción)")
        elif opcion == "3":
            print("Saliendo de Axon...")
            break
        else:
            print("Opción inválida")
 
      
def menu_agregar_colaborador():
    
    while True:
        
        print("\nBienvenido denuevo")
        print("\n----Panel Admin-----")
        print("1. Agregar colaborador")
        print("2. Salir")
        
        opcion = pedir_numero("Selecciona una opción: ")
        
        if opcion == 1:
            
            user = pedir_texto("Nuevo colaborador: ")
            password = pedir_texto("Asignar una contraseña: ")
            rol = "colaborador"
            
            while True:
                
                if password.strip() == "":
                    print("\nNo se puede dejar en blanco")
                else:
                    break
            
            with open("admin/usuarios.txt","a") as archivo:
                archivo.write(f"{user},{password},{rol}\n")
                print("\nSe agrego un nuevo colaborador exitosamente")
                
        elif opcion == 2:
            break
        
