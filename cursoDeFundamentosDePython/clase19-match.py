dia = 1

match dia:
    case 1: # En caso de que dia sea igual a 1 ejecuta esto
        print("Hoy es Lunes")
    case 2:
        print("Hoy es Martes")
    case 3:
        print("Hoy es Miercoles")
    case _:
        print("No se cumplen ninguna de las condiones anteriores")



    # TAREA (Hacer lo mismo de la clase pero con String)
x = "Topoyiyo Rocks"

match x:
    case "Topoyiyo Rocks": # <-- Aquí van dos puntos
        print("A la camita")
    case _:
        print("A la camita no :v")