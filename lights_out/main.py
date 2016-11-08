import menu
import accesoTablero



print(" ")
print("Binevenido al juego LIGHTS OUT")
print(" ")

modo = input(str("Elija el modo de juego (1 = Aleatorio, 2 = Nivel 1, 3 = Salir): "))

menu.mostrarMenu(modo)

coordenadas = input(str("ingrese la posición del tablero: "))
resultadoCoordenada = accesoTablero.validarCoordenadas(coordenadas)
print(resultadoCoordenada)
print ("la coordenada ingresada no es válida")
menu.mostrarMenu(modo)








