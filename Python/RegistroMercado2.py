mercado = ["Arroz", "Cereal", "Café", "Chocolate", "Huevos"]
print("Ya has comprado estos productos en la tienda")

edad = input("Antes de ingresar a nuestro sistema, necesitamos que ingreses tu edad: ")
edadid = int(edad)

if edadid >= 18:
    activar = True

    while activar:

        print("\nBienvenido al sistema")
        print("--- MENÚ DE MERCADO ---")
        print("1. Agregar un producto")
        print("2. Observar los productos")
        print("3. Eliminar producto")
        print("4. Salir del sistema")

        opcion = input("Elige una de las opciones que quieres ver: ")

        mostrar = False

        if opcion == "1":
            agregar = input("Agrega un producto que quieres registrar: ")
            mercado.append(agregar)
            print("Has añadido:", agregar, "en tu carrito")
            total = len(mercado)
            print("Ahora tienes:", total, "productos")

        elif opcion == "2":
            print("Tu lista ordenada de los productos que tienes ahora:")
            mostrar = True

        elif opcion == "3":
            eliminar = input("¿Cuál producto deseas eliminar de tu carrito? ")
            if eliminar in mercado:
                mercado.remove(eliminar)
                mostrar = True
                total = len(mercado)
                print("Ahora solo tienes:", total, "productos")
            else:
                print("Ese producto no está en la lista")

        elif opcion == "4":
            print("Gracias por usar nuestro sistema")
            activar = False

        else:
            print("Ninguna de las opciones es correcta, vuelve a intentarlo")

        if mostrar:
            for mercadol in mercado:
                print("▶", mercadol)

else:
    print("No cumples con la edad requerida para ingresar")