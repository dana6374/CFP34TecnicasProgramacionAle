import coordenadas
import puntosTablero
import tablero
import tableroNiveles
import copy

def cambiarPuntos(puntos, tableroACambiar):

    conversorDeSimbolos = {".":"o", "o":"."}

    for punto in puntos:
        tableroACambiar[punto[0]][punto[1]] = conversorDeSimbolos[tableroACambiar[punto[0]][punto[1]]]



def jugar():

    print ("Jugando en modo predeterminado !")
    print ("")

    miTablero = copy.deepcopy(tableroNiveles.estructuraTablero1)

    #Tengo que mostrar el tablero del nivel1 Declarar variable y hacer una copia.

    tablero.imprimirTablero(miTablero)

    coordenadasDelUsuario = coordenadas.solicitarCoordenadas()
    print ("")
    print ("La coordenada: ", coordenadasDelUsuario)
    print ("Es valida")
    print ("")


    puntosACambiar= puntosTablero.generarPuntos(coordenadasDelUsuario, miTablero)

    puntosACambiar.append(coordenadasDelUsuario)

    cambiarPuntos(puntosACambiar, miTablero)
    tablero.imprimirTablero(miTablero)






