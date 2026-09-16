mercado = ["Mayonesa", "Tomate", "Arroz", "Manzana"]

def Lista_de_Mercado (Lista):
    Total = len(Lista)
    ListaR = list(Lista)
    print ("Actualmente tienes en tu carrito: ", Total ,"productos")
    print ("Tu lista actual en tu carrito: ", ListaR)
    mercado.sort()
    print ("Para que conozcas mejor el orden de A a la Z son: ", mercado)

Edad_Validar = False

while not Edad_Validar:
    try:
        edad = input("Digite su edad para verificar si cumples con las normativas del sistema: ")
        edadID = int(edad)
        Edad_Validar = True
    except ValueError:
        print ("Incorrecto, solo se permiten caracteres numéricos, vuelva a intentarlo nuevamente")

if edadID >=18:
    Limpio = False
    Activar = True
    print ("Ingresaste correctamente")

    while Activar:
        print("\nBienvenido al sistema")
        print("--- MENÚ DE MERCADO ---")
        print("1. Agregar un producto")
        print("2. Observar los productos")
        print("3. Eliminar producto")
        print("4. Buscar un producto")
        print("5. Limpiar lista")
        print("6. Salir del sistema")


        try:
            opcion = input("Cuál de las opciones deseas elegir: ")
            opciones = int(opcion)
        except ValueError:
             print ("Error: Ingresa solo números enteros del 1 al 6.")
              
        if opcion =="1":
            agregar = input("Qué producto deseas ingresar a tu carrito: ")

            if agregar not in mercado:
                mercado.append(agregar)
                print ("Agregaste el producto", agregar ,"en tu carrito")
                Lista_de_Mercado(mercado)
                Limpio = True
            else:
                  print ("El producto ya se encuentra en la lista")
        elif opcion =="2":
            Lista_de_Mercado(mercado)
            Limpio = True
        elif opcion =="3":
            eliminar = input ("¿Qué producto deseas eliminar de tu carrito?: " )
            if eliminar in mercado:
                mercado.remove(eliminar)
                print ("Has eliminado el producto ", eliminar , "de tu carrito")
                Lista_de_Mercado(mercado)
                Limpio = True
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
            Activar = False
        else:
             print("Ninguna de las opciones es correcta, vuelve a intentarlo")

    if Limpio:
        print("\n--- TU LISTA FINAL LIMPIA ---")
        for mercadoID in mercado:
                    print ("▶", mercadoID)
else:
    print("No cumples con la edad requerida para ingresar")



            








                




    







    

