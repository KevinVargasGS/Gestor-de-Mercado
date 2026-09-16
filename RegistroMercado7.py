mercado = {
    "Leche": 4000,
    "Arroz": 3400,
    "Cereal": 5000,
    "Pescado": 2000,
}

def Lista_de_Mercado(Diccionario):
    total = len(Diccionario)
    print("Tienes en la actualidad:", total ,"productos en tu carrito")
    print("------LISTA ACTUAL DE TU MERCADO -----")
    for producto, precio in sorted (Diccionario.items()):
        print ("Tus productos son ▶: ", producto , "---- Precio: ", precio ,"pesos") 
Lista_de_Mercado(mercado)

EdadValidacion = False

while not EdadValidacion:
    try:
        edad = input("Para ingresar a nuestro sistema requerimos tu edad. ¿Cuántos años tienes?: ")
        edadId = int(edad)
        EdadValidacion = True
    except ValueError:
        print ("Incorrecto, solo se permiten caracteres numéricos, vuelva a intentarlo nuevamente")

if edadId >=18:
    Activar = True
    Limpio = False

    while Activar:
        print("\nBienvenido al sistema")
        print("--- MENÚ DE MERCADO ---")
        print("1. Agregar un producto")
        print("2. Observar los productos")
        print("3. Eliminar producto")
        print("4. Buscar un producto")
        print("5. Limpiar lista")
        print("6. Salir del sistema")

        while True:
            try:
                opcion = input ("Cuál de las opciones deseas elegir: ")
                opciones = int(opcion)
                break
            except ValueError:
                print ("Error: Ingresa solo números enteros del 1 al 6.")

        if opcion =="1":
            agregar = input("Qué producto deseas ingresar a tu carrito: ")
            if agregar not in mercado:
                while True:
                    try:
                        precio = input ("Ahora ingresa un precio al producto adquirido: ")
                        precioId = int(precio)
                        break
                    except ValueError:
                        print("Error: El precio debe ser un número entero válido.")
                mercado [agregar] = precioId
                print("Agregaste el producto", agregar, "con un valor de", precioId, "pesos")
                Lista_de_Mercado(mercado)
                Limpio = True
            else:
                print ("El producto ya se encuentra en la lista")
        elif opcion =="2":
            Lista_de_Mercado(mercado)
            Limpio = True
        elif opcion =="3":
            eliminar = input("¿Qué producto deseas eliminar de tu carrito?: " )
            if eliminar in mercado:
                mercado.pop(eliminar)
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
        elif opcion == "5":
            mercado.clear()
            print ("Limpieza hecha", mercado )
        elif opcion =="6":
            print ("Gracias por usar nuestro sistema")
            Activar = False
    if Limpio:
        print("\n--- TU LISTA FINAL LIMPIA/INGRESOS ---")
        PrecioTotal = 0
        for precio in mercado.values():
            PrecioTotal = precio + PrecioTotal
        print ("En total tienes que pagar ",PrecioTotal, "pesos")
        Lista_de_Mercado(mercado)
else:
    print("No cumples con la edad requerida para ingresar")

