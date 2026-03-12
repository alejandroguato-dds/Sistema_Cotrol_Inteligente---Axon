from login import login
from menus import menu_principal_usuario,menu_agregar_colaborador
def main():   
    
    while True:
        
        rol = login()
        
        if rol == "admin":
            menu_agregar_colaborador()
            
        elif rol == "colaborador":
            menu_principal_usuario()

        elif rol == "salir":
            print("Gracias por usar Axon")
            break
    
if __name__=="__main__":
    main()
