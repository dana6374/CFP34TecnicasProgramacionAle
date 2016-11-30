import coordenadas
import puntosTablero
import tablero
import tableroNiveles
import copy

def cambiarPuntos(puntos, tableroACambiar):

    conversorDeSimbolos = {".":"0", "0":"."}

    for i in puntos
    tableroACambiar[puntos[0] puntos[1]] = conversorDeSimbolos[tableroACambiar[puntos[0] puntos[1]]



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






