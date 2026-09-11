mercado = ["Arroz","Pasta","Crema de leche", "Platano"]
print ("Tus productos actuales" ,mercado)

activar = True

while activar:
    print("\n--MENU DE MERCADO --")
    print("1. Agregar un producto")
    print("2. Observar los productos")
    print("3. Eliminar producto")
    print("4. Salir del sistema")

    opcion = input ("Ingresa la opción que quieras escoger " )

    if opcion =="1":
        edadid = input("Ingresa tu edad: ")
        edadR = int(edadid)
        if edadR >=18:
            print ("Si tienes la edad mayor para agregar un producto")
            agregarp = input("Agrega el producto " )
            mercado.append (agregarp)
            print ("La actualización quedo:" ,mercado)
        else:
            print ("No puedes agregar no eres mayor de edad")
    elif opcion == "2":
        print ("Esta es tu lista de mercado: " ,mercado)
    elif opcion == "3":
        eliminar = input ("¿Qué producto deseas eliminar? " )
        if eliminar in mercado:
            mercado.remove(eliminar)
            print ("Ahora tu lista esta asi" , mercado)
        else:
            print("ese prodcuto no esta en la lista")
    elif opcion =="4":
        print ("Gracias por usar nuestro sistema")
        activar = False
    else:
        print ("opción inválida")





