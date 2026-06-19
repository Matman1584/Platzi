
ARCHIVO_PEDIDOS = "pedidos.txt"

def ver_historial():
    try:
        print("\n Historial de pedidos")
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
    except FileNotFoundError:
        print("\n Todavía no existe un historial de pedidos")
        