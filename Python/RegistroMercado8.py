mercado = {
    "Tomate": 500,
    "Arroz": 2400,
    "Galletas": 5000,
    "Cereal": 4000,
}

def Lista_De_Mercado(Diccionario):
    total = len(Diccionario)
    print("Tienes en la actualidad:", total ,"productos en tu carrito")
    print("------LISTA ACTUAL DE TU MERCADO -----")
    for producto, precio in sorted(Diccionario.items()):
        print ("Tus productos son ▶: ", producto , "---- Precio: ", precio ,"pesos") 
Lista_De_Mercado(mercado)


edad_valida = False

while not edad_valida:
    try:
        edad = input("Para ingresar a nuestro sistema requerimos tu edad. ¿Cuántos años tienes?: ")
        edadId = int(edad)
        edad_valida = True
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
        print("6. Actualizar precio de un producto")
        print("7. Salir del sistema")

        while True:
            try:
                opcion = input ("Cuál de las opciones deseas elegir: ")
                opciones = int(opcion)
                if 1 <= opciones  <= 7:
                    break
                else:
                    print("Error: Debes ingresar un número entero del 1 al 7.")
            except ValueError:
                print ("Error: Ingresa solo números enteros del 1 al 7.")
        if opciones ==1:
            agregar = input("Qué producto deseas ingresar a tu carrito: ")
            if agregar not in mercado:
                while True:
                    try:
                        precio = input ("Ahora ingresa un precio al producto adquirido: ")
                        precioid = int(precio)
                        break
                    except ValueError:
                        print("Error: El precio debe ser un número entero válido.")
                mercado [agregar] = precioid
                print("Agregaste el producto", agregar, "con un valor de", precioid, "pesos")
                Lista_De_Mercado(mercado)
                Limpio = True
            else:
                print ("El producto ya se encuentra en la lista")
        elif opciones ==2:
            Lista_De_Mercado(mercado)
            Limpio=True
        elif opciones ==3:
            eliminar = input("¿Qué producto deseas eliminar de tu carrito?: " )
            if eliminar in mercado:
                mercado.pop(eliminar)
                print ("Has eliminado el producto ", eliminar , "de tu carrito")
                Lista_De_Mercado(mercado)
                Limpio = True
            else: 
                print("Ese producto no está en la lista")
        elif opciones ==4:
            observar = input ("¿Qué producto deseas observar?: " )
            if observar in mercado:
                print("El producto ", observar ,"se encuentra en la lista y su precio es ", mercado[observar] ," pesos")
            else:
                print("El producto no se encuentra en tu lista")
        elif opciones ==5:
            mercado.clear()
            print ("Limpieza hecha", mercado )
        elif opciones ==6:
            actualizarP = input("¿Qué producto deseas actualizar su precio?: ")
            if actualizarP in mercado:
                while True:
                    try:
                        precioActualizado = input("Digite el nuevo precio del producto: " )
                        precioAc = int(precioActualizado)
                        break
                    except ValueError:
                        print ("Error: Ingresa solo números")
                mercado [actualizarP] = precioAc
                print ("El precio del producto ", actualizarP ,"fue actualizado correctamente. Ahora su nuevo valor es ", precioAc ,"pesos")
                Lista_De_Mercado(mercado)
                Limpio = True
            else:
                print("Ese producto no está en la lista. Si deseas ingresarlo, usa la opción 1.")
        elif opciones ==7:
            print ("Gracias por usar nuestro sistema")
            Activar = False

    if Limpio:
        print("\n--- TU LISTA FINAL LIMPIA/INGRESOS ---")
        PrecioSum = 0
        for precio in mercado.values():
            PrecioSum = PrecioSum + precio
        print ("En total tienes que pagar ",PrecioSum, "pesos")
        Lista_De_Mercado(mercado)
else:
    print("No cumples con la edad requerida para ingresar")