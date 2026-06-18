ARCHIVO_PEDIDOS = "pedidos.txt"

def pedir_cafe():
    print("\n Elige el caffe que prefieras: ")
    print("1. Espresso")
    print("2. Cappucino")
    print("3. Latte")
    print("4. Americano")
    print("5. Cafe con Hielo")
    print("6. Mocha")
    print("7. Affogato")
    print("8. Kaffeost")
    print("9. Egg Coffe")
    print("10. Café Turco")
    print("11. Cold Brew")
    print("12. Café Bombón")
    print("13. Buna Etíope")

    opcion = input("Opción: ")

    cafes = {
        "1": "Espresso",
        "2": "Cappuchino",
        "3": "Latte",
        "4": "Americano",
        "5": "Café con Hielo",
        "6": "Mocha",
        "7": "Affogato",
        "8": "Kaffeost",
        "9": "Egg Coffe",
        "10": "Café Turco",
        "11": "Cold Brew",
        "12": "Café Bombón",
        "13": "Buna Etíope"
    }

    if opcion in cafes:
        cafe_elegido = cafes[opcion]
        print("Tu " + cafe_elegido + "Llegará a tu mesa en 5min")

        # Guardamos el café dentro de un archivo para luego tener el historial de los pedidos
        with open(ARCHIVO_PEDIDOS, "a", encoding = "utf-8") as archivo:    # Usamos with para abrir el archivo
            archivo.write(cafe_elegido + "\n")  # El salto de linea es para que cada cafe elegido quede en una linea aparte dentro de un docuemnto llamando pedidos.txt
    else:
        print("La opción no es valida, por favor intenta de nuevo")