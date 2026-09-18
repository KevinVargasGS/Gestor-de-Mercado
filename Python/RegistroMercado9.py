mercado = {
    "Manzana": [600, 2],
    "Arroz": [3500, 1],
    "Piña": [5000, 1],
    "Pescado": [8000, 1],
}

def Lista_De_Mercado(Diccionario):
    total = len(mercado)
    print("Actualmente tienes en tu carrito ",total ," productos")
    print("------LISTA ACTUAL DE TU MERCADO -----")
    for producto, (precio, cantidad) in sorted(Diccionario.items()):
        PrecioTotal = precio * cantidad
        print ("Actualmente tu producto ", producto ," su precio actual es: ", PrecioTotal , "pesos con: ", cantidad , " unidades en tu mercado")
Lista_De_Mercado(mercado)

EdadValidacion = False

while not EdadValidacion:
    try:
        edad = input("Para ingresar a nuestro sistema requerimos tu edad. ¿Cuántos años tienes?: ")
        edadid = int(edad)
        EdadValidacion = True
    except ValueError:
        print ("Incorrecto, solo se permiten caracteres numéricos, vuelva a intentarlo nuevamente")

if edadid >=18:
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
        print("7. Cambiar cantidad de un producto")
        print("8. Salir del sistema")

        while True:
            try:
                opcion = input ("Cuál de las opciones deseas elegir: ")
                opciones = int(opcion)
                if 1<= opciones <=8:
                    break
                else:
                    print("Error: Debes ingresar un número entero del 1 al 8.")
            except ValueError:
                print ("Error: Ingresa solo números enteros del 1 al 8.")
        if opciones ==1:
            while True:
                agregar = input("Agrega un producto que quieras añadir en tu carrito: ")
                if agregar.isalpha():
                    break
                else:
                    print ("Error: No se permiten caracteres numéricos ni espacios. Vuelva a intentarlo nuevamente")
            if agregar not in mercado:
                while True:
                    try:
                        precio = input("Ingresa un precio al producto añadido: " )
                        precioId = int(precio)
                        break
                    except ValueError:
                        print("Error: Solo se permiten valores numéricos. Vuelva a intentarlo")
                while True:
                    try:
                        cantidad = input("Ingresa la cantidad que vas a obtener del producto: ")
                        cantidadid = int(cantidad)
                        break
                    except ValueError:
                        print("Error: Solo se permiten valores numéricos. Vuelva a intentarlo")
                mercado [agregar] = [precioId, cantidadid]
                print("Tu producto ", agregar , " ha sido registrado correctamente con un precio de: ", precioId , "con ", cantidadid ," unidades llevadas")
                Lista_De_Mercado(mercado)
                Limpio=True
            else:
                print ("El producto ya se encuentra en la lista")
        elif opciones == 2:
            Lista_De_Mercado(mercado)
            Limpio = True
        elif opciones == 3:
            eliminar = input("¿Qué producto deseas eliminar de tu carrito?: ")
            if eliminar in mercado:
                mercado.pop(eliminar)
                print("Has eliminado el producto ", eliminar ," correctamente")
                Lista_De_Mercado(mercado)
                Limpio = True
            else:
                print("Ese producto no está en la lista")
        elif opciones ==4:
            observar = input("¿Qué producto deseas observar?: ")
            if observar in mercado:
                PrecioObservar = mercado[observar][0]
                CantidadObservar = mercado[observar][1]
                print("El producto ", observar , "se encuenta en nuestra base de datos con un precio ", PrecioObservar , "con ", CantidadObservar ," Unidades")
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
                        precioActualziado = input("Digite el nuevo precio del producto: " )
                        precioAc = int(precioActualziado)
                        break
                    except ValueError:
                        print ("Error: Ingresa solo números")
                mercado [actualizarP][0] = precioAc
                print ("El precio del producto ", actualizarP ,"fue actualizado correctamente. Ahora su nuevo valor es ", precioAc ,"pesos")
                Lista_De_Mercado(mercado)
                Limpio = True
            else:
                print("Ese producto no está en la lista. Si deseas ingresarlo, usa la opción 1.")
        elif opciones ==7:
            CantidadActualizada = input("¿Qué producto deseas actualizar su cantidad?: ")
            if CantidadActualizada in mercado:
                while True:
                    try:
                        CantidadActual = input("Digite la nueva cantidad del producto: ")
                        CantidadAc = int(CantidadActual)
                        break
                    except ValueError:
                        print ("Error: Ingresa solo números")
                mercado [CantidadActualizada] [1] = CantidadAc
                print ("La cantidad del producto ", CantidadActualizada ,"fue actualizado correctamente. Ahora su nueva cantidad es ", CantidadAc ,"unidades")
                Lista_De_Mercado(mercado)
                Limpio = True
            else:
                print("Ese producto no está en la lista. Si deseas ingresarlo, usa la opción 1.")
        elif opciones ==8:
            print ("Gracias por usar nuestro sistema")
            Activar = False

    if Limpio:
        print("\n--- TU LISTA FINAL LIMPIA/INGRESOS ---")
        PrecioSum = 0
        for precio, cantidad in mercado.values():
            PrecioSum = PrecioSum + (precio*cantidad)
        print("En total tienes que pagar", PrecioSum, "pesos")
        Lista_De_Mercado(mercado)
else:
    print("No cumples con la edad requerida para ingresar")
