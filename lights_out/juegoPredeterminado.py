import coordenadas
import puntosTablero
import tablero
import tableroNiveles

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


    puntosVecinos = puntosTablero.generarPuntos(coordenadasDelUsuario, miTablero)

    cambiarPuntos(puntosVecinos)

def cambiarPuntos(puntosVecinos):


