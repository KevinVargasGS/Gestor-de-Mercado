mercado = ["Arroz", "Manzana", "Naranjas", "Cereal"]

total = len (mercado)
mostrar = list(mercado)
print ("Tienes:", total ,"productos en tu carrito")
print ("Para conocer tu lista actual es esta:", mostrar)

edad = input ("Bienvenido al sistema primero requerimos que ingreses tu edad: ")
edadid= int(edad)

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
        print("5. Salir del sistema")

        opcion = input("Elige cuál de las opciones quieres elegir: ")

        if opcion =="1":
            agregar = input("Qué producto deseas agregar: ")
            if agregar not in mercado:
                mercado.append(agregar)
                print ("Agregaste el producto", agregar ,"en tu carrito")
                total = len (mercado)
                mostrar = list(mercado)
                limpio = True
                print ("Tienes:", total ,"productos en tu carrito")
                print ("Para conocer tu lista actual es esta:", mostrar)
            else:
                print ("El producto ya se encuentra en la lista")               
        elif opcion =="2":
            total = len (mercado)
            mostrar = list(mercado)
            limpio = True
            print ("Tienes:", total ,"productos en tu carrito")      
            print ("Tu lista de productos es la siguiente: ", mercado)
        elif opcion =="3":
            eliminar = input ("¿Qué producto deseas eliminar de tu carrito? " )
            if eliminar in mercado:
                mercado.remove(eliminar)
                print ("Has eliminado el producto ", eliminar , "de tu carrito")
                total = len (mercado)
                mostrar = list(mercado)
                limpio = True
                print ("Tienes:", total ,"productos en tu carrito")
                print ("Para conocer tu lista actual es esta:", mostrar)
            else:
                print("Ese producto no está en la lista")              
        elif opcion =="4":
            observar = input("Qué producto deseas buscar: " )
            if observar in mercado:
                print("El producto ", observar ,"se encuentra en la lista")
            else:
                print ("El producto no se encuentra en tu lista")              
        elif opcion =="5":
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


    

            

