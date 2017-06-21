import baseDatos
import alta
import Baja
import modificación
import facturación

def clearScreen():
    import os
    if os.name == "nt":
       os.system("cls")
    elif os.name == "posix":
         os.system("clear")
    else:
         print("<-No se pudo borrar la pantalla->")

def mostrarMenu():

    print(" ")
    print("Alta Baja Y Modificacion de Base de Datos")
    print(" ")

    modo = input(str("Elija el modo: 1 = ALTA, 2 = BAJA, 3 = MODIFICACION, 4 = CONSULTA, 5 = fACTURACIÓN, 6 = SALIR "))

    if modo == "1":
        print("")
        print("Alta de registros")
        alta.ejec()
    elif modo == "2":
        print("")
        print("baja de registros")
        baja.ejec()
    elif modo == "3":
        print("")
        print("modificacion de registros")
        modifiacion.ejec()
    elif modo == "4":
        print("")
        print("consulta de registros")
        consulta.ejec()

    elif modo == "5":
        print("")
        print("Salir del sistema")
        exit()

    elif modo == "6":
        print("")
        print("Salir del sistema")
        exit()
    else:
        print("")
        print("opción inválida")
        mostrarMenu()