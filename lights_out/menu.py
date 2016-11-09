import juegoPredeterminado

def mostrarMenu():

    print(" ")
    print("Binevenido al juego LIGHTS OUT")
    print(" ")

    modo = input(str("Elija el modo de juego (1 = Predeterminado, 2 = Aleatorio , 3 = Salir): "))

    if modo=="1":
        print("")
        juegoPredeterminado.jugar()
    elif modo =="2":
        print("Aleatorio")
        #TODO llamar al juego aleatorio
    elif modo =="3":
        print("Ud salió del juego")
        exit()
    else:
        print("opción inválida")
        mostrarMenu()
