import coordenadas
import puntosTablero
import tablero
import tableroNiveles


def jugar():

    print("Jugando en modo predeterminado !")
#Tengo que mostrar el tablero del nivel1
    tablero.imprimirTablero(tableroNiveles.estructuraTablero1)

    coordenadasDelUsuario = coordenadas.solicitarCoordenadas()
    print("LA COORDENADA FUE VALIDA !!!! ", coordenadasDelUsuario)
    puntosTablero.generarPuntos(coordenadasDelUsuario)


    #todo juego