import coordenadas
import validacion

def jugar():

    print("Jugando en modo predeterminado !")
    coordenadasDelUsuario = coordenadas.solicitarCoordenadas()

    if validacion.esCoordenadaValida(coordenadasDelUsuario):
        print(coordenadasDelUsuario)
        # TODO en este punto que ya se que es valida llamo a convertirCoordenada
    else:
        print("la coordenada ingresada no es válida")
        jugar()

