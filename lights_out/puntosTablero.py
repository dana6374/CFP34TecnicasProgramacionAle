import conversorCoordenadas
import tablero

#coordenadasOriginales= conversorCoordenadas(coordenadas)
"""
PRE: recibe una tupla con las coordenadas validas del usuario traducidasd a nuestra estructura

"""
def generarPuntos(coordenada,tablero):


    puntosVecinos = []

    punto1 = coordenada[0], coordenada[1] - 1
    punto2 = coordenada[0] + 1, coordenada[1]
    punto3 = coordenada[0] - 1, coordenada[1]
    punto4 = coordenada[0], coordenada[1] + 1

    if punto1[0] >=0 and punto1[0] <= len(tablero)-1:
        if punto1[1] >=0 and punto1[1]<= (len(tablero[0])-1):
           puntosVecinos.append(punto1)


    if punto2[0] >=0 and punto2[0] <= len(tablero)-1:
        if punto2[1] >=0 and punto2[1]<= (len(tablero[0])-1):
           puntosVecinos.append(punto2)


    if punto3[0] >=0 and punto3[0] <= len(tablero)-1:
        if punto3[1] >=0 and punto3[1]<= (len(tablero[0])-1):
           puntosVecinos.append(punto3)


    if punto4[0] >=0 and punto4[0] <= len(tablero)-1:
        if punto4[1] >=0 and punto4[1]<= (len(tablero[0])-1):
            puntosVecinos.append(punto4)

    return puntosVecinos