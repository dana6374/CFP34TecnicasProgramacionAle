import juegoPredeterminado

def mostrarMenu():
    modo = input(str("Elija el modo de juego (1 = Predeterminado, 2 = Aleatorio , 3 = Salir): "))

    if modo=="1":
        print("")
        juegoPredeterminado.jugar()
    elif modo =="2":
        print("")
        print("Aleatorio")
        #TODO llamar al juego aleatorio
    elif modo =="3":
        print("")
        print("Ud salió del juego")
        exit()
    else:
        print("")
        print("opción inválida")
        mostrarMenu()