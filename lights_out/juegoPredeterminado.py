import coordenadas
import validacion
import conversorCoordenadas

def jugar():

    print("Jugando en modo predeterminado !")
    coordenadasDelUsuario = coordenadas.solicitarCoordenadas()

    if validacion.esCoordenadaValida(coordenadasDelUsuario):
        conversorCoordenadas.convertirCoordenadas(coordenadasDelUsuario)
    else:
        jugar()

