mercado = ["Arroz", "Pasta", "Crema de leche", "Plátano"]
print("Tus productos actuales:", mercado)

activar = True

while activar:
    print("\n--- MENÚ DE MERCADO ---")
    print("1. Agregar un producto")
    print("2. Observar los productos")
    print("3. Eliminar producto")
    print("4. Salir del sistema")

    opcion = input("Ingresa la opción que quieras escoger: ")

    if opcion == "1":
        edadid = input("Ingresa tu edad: ")
        edadR = int(edadid)
        if edadR >= 18:
            print("Sí tienes la edad mayor para agregar un producto")
            agregarp = input("Agrega el producto: ")
            mercado.append(agregarp)
            print("La actualización quedó:", mercado)
        else:
            print("No puedes agregar, no eres mayor de edad")
    elif opcion == "2":
        print("Esta es tu lista de mercado:", mercado)
    elif opcion == "3":
        eliminar = input("¿Qué producto deseas eliminar? ")
        if eliminar in mercado:
            mercado.remove(eliminar)
            print("Ahora tu lista está así:", mercado)
        else:
            print("Ese producto no está en la lista")
    elif opcion == "4":
        print("Gracias por usar nuestro sistema")
        activar = False
    else:
        print("Opción inválida")