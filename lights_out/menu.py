import tablero

def mostrarMenu(modo):
    if modo=="1":
        print("Aleatorio")
        tablero.imprimirTablero()
    elif modo =="2":
        print("Nivel")
        tablero.imprimirTablero()
    else:
        if modo=="3":
            print("Ud salió del juego")
            exit()
        else:
            print("opción inválida")
