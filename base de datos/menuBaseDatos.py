
def mostrarMenu():
    modo = input(str("Elija el modo: 1 = ALTA, 2 = BAJA, 3 = MODIFICACION, 4 = CONSULTA, 5 = SALIR "))

    if modo == "1":
        print("")
        print("Alta de registros")
        alta.consulta()
    elif modo == "2":
        print("")
        print("baja de registros")
        baja.consulta()
    elif modo == "3":
        print("")
        print("modificacion de registros")
    elif modo == "4":
        print("")
        print("consulta de registros")
    elif modo == "5":
        print("")
        print("Salir del sistema")
        exit()
    else:
        print("")
        print("opción inválida")
        mostrarMenu()