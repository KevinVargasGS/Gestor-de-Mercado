mercado = ["Arroz", "Pera", "Manzanas", "Galletas"]

total = len (mercado)
mostrar = list(mercado)
print ("Tienes:", total ,"productos en tu carrito")
print ("Para conocer tu lista actual es esta:", mostrar)
mercado.sort()
print ("Para que conozcas mejor el orden de A a la Z son: ", mercado)

edad = input("Digite tu edad para poder ingresar a nuestro sistema: " )
edadid = int(edad)

if edadid >=18:
    print ("Bienvenido a nuestro sistema")
    activar = True
    limpio = False

    while activar:
        print("\nBienvenido al sistema")
        print("--- MENÚ DE MERCADO ---")
        print("1. Agregar un producto")
        print("2. Observar los productos")
        print("3. Eliminar producto")
        print("4. Buscar un producto")
        print("5. Limpiar lista")
        print("6. Salir del sistema")

        opcion = input ("¿Qué elección deseas elegir de nuestro sistema? " )

        if opcion =="1":
            agregar = input("Qué producto deseas ingresar a tu carrito: " )
            if agregar not in mercado:
                mercado.append(agregar)
                print ("Agregaste el producto", agregar ,"en tu carrito")
                mostrar = list(mercado)
                total = len (mercado)
                limpio = True
                print ("Tienes:", total ,"productos en tu carrito")
                print ("Para conocer tu lista actual es esta:", mostrar)
                mercado.sort()
                print ("Para una lista más ordenada: ", mercado )
            else:
                print ("El producto ya se encuentra en la lista")
        elif opcion =="2":
            total = len (mercado)
            mostrar = list(mercado)
            limpio = True
            print ("Tienes:", total ,"productos en tu carrito")
            print ("Para conocer tu lista actual es esta:", mostrar)
            mercado.sort()
            print ("Para una lista más ordenada: ", mercado )
        elif opcion =="3":
            eliminar = input ("¿Qué producto deseas eliminar de tu carrito?: " )
            if eliminar in mercado:
                mercado.remove(eliminar)
                print ("Has eliminado el producto ", eliminar , "de tu carrito")
                total = len (mercado)
                mostrar = list(mercado)
                limpio = True
                print ("Tienes:", total ,"productos en tu carrito")
                print ("Para conocer tu lista actual es esta:", mostrar)
                mercado.sort()
                print ("Para que conozcas mejor el orden de A a la Z son: ", mercado)
            else:
                print("Ese producto no está en la lista")
        elif opcion =="4":
            observar = input ("¿Qué producto deseas observar?: " )
            if observar in mercado:
                print("El producto ", observar ,"se encuentra en la lista")
            else:
                print("El producto no se encuentra en tu lista")
        elif opcion =="5":
            mercado.clear()
            print ("Limpieza hecha", mercado )
        elif opcion =="6":
            print ("Gracias por usar nuestro sistema")
            activar = False
        else:
            print("Ninguna de las opciones es correcta, vuelve a intentarlo")
    if limpio:
        print("\n--- TU LISTA FINAL LIMPIA ---")
        for mercadoID in mercado:
            print ("▶", mercadoID)
else:
    print("No cumples con la edad requerida para ingresar")





                



            






