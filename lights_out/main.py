import menu
import tablero


print(" ")
print("Binevenido al juego LIGHTS OUT")
print(" ")

modo = input(str("Elija el modo de juego (1 = Aleatorio, 2 = Nivel 1, 3 = Salir): "))

menu.mostrarMenu(modo)

tablero.imprimirTablero()






