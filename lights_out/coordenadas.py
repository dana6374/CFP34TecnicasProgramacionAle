import validacion
import conversorCoordenadas

def solicitarCoordenadas():

    coordenadaIngresada = (input(str("ingrese la posición del tablero (Coordenadas: 1 Letra para columna y 1 nro para fila) : "))).lower()

    if validacion.esCoordenadaValida(coordenadaIngresada):
        return conversorCoordenadas.convertirCoordenadas(coordenadaIngresada)
    else:
        solicitarCoordenadas()