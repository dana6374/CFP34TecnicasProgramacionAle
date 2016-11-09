import validacion
import conversorCoordenadas


def solicitarCoordenadas(coordenadaIngresada):
    coordenadaIngresada= input(str("ingrese la posición del tablero (Coordenadas: 1 Letra para columna y 1 nro para fila) : "))

   if validacion.esCoordenadaValida(coordenadaIngresada):
        conversorCoordenadas.convertirCoordenadas(coordenadaIngresada)
         return coordenadaIngresada
