import menu
import validacion



print(" ")
print("Binevenido al juego LIGHTS OUT")
print(" ")

modo = input(str("Elija el modo de juego (1 = Aleatorio, 2 = Nivel 1, 3 = Salir): "))

menu.mostrarMenu(modo)

coordenadas = input(str("ingrese la posición del tablero (coordenadas. 1 Letra para columna y 1 nro para fila) : "))
if validacion.esCoordenadaValida(coordenadas):
    print(coordenadas)
    #TODO en este punto que ya se que es valida llamo a convertirCoordenada
else:
    print ("la coordenada ingresada no es válida")

menu.mostrarMenu(modo)








