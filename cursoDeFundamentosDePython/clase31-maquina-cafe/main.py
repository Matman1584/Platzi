from menu import mostrar_menu
from pedidos import pedir_cafe

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            pedir_cafe()
            pass
        elif opcion == "2":
            # Ver el historial
            pass
        elif opcion == "3":
            print("\n Muchas gracias por haber tomado nuestros ricos cafes")
            break
        else:
            print("Opcion invalida, por favor indique una de las")

if __name__ == "__main__":
    main()