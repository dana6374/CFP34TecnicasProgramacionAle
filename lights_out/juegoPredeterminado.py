import coordenadas
import puntosTablero
import tablero
import tableroNiveles

def jugar():

    print ("Jugando en modo predeterminado !")
    print ("")
    #Tengo que mostrar el tablero del nivel1 Declarar variable y hacer una copia.
    tablero.imprimirTablero(tableroNiveles.estructuraTablero1)

    coordenadasDelUsuario = coordenadas.solicitarCoordenadas()
    print ("")
    print ("La coordenada: ", coordenadasDelUsuario)
    print ("Es valida")
    print ("")


    puntosVecinos = puntosTablero.generarPuntos(coordenadasDelUsuario,tableroNiveles.estructuraTablero1)

    def cambiarPuntos(puntosVecinos):


