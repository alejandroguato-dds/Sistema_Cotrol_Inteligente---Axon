def menu_principal():
    while True:
        print("\n------- AXON -------")
        print("1. Gestión de productos")
        print("2. Ventas")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Módulo de productos (en construcción)")
        elif opcion == "2":
            print("Módulo de ventas (en construcción)")
        elif opcion == "3":
            print("Saliendo de Axon...")
            break
        else:
            print("Opción inválida")
