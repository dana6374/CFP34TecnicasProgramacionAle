import coordenadas
import puntosTablero

def jugar():

    print("Jugando en modo predeterminado !")

    coordenadasDelUsuario = coordenadas.solicitarCoordenadas()
    print("LA COORDENADA FUE VALIDA !!!! ", coordenadasDelUsuario)
    puntosTablero.generarPuntos(coordenadasDelUsuario)
    """El jugador"""

    #todo juego