import coordenadas
import puntosTablero
import tablero
import tableroNiveles


def jugar():

    print("Jugando en modo predeterminado !")
    print ("")
    #Tengo que mostrar el tablero del nivel1 Declarar variable y hacer una copia.
    tablero.imprimirTablero(tableroNiveles.estructuraTablero1)


    coordenadasDelUsuario = coordenadas.solicitarCoordenadas()
    print("")
    print("LA COORDENADA Es VALIDA !!!! ", coordenadasDelUsuario)


    # TODO cambiar tableroNiveles.estructuraTablero1 por la copia del tablero del jugador

    puntosTablero.generarPuntos(coordenadasDelUsuario,tableroNiveles.estructuraTablero1)


    #todo juego