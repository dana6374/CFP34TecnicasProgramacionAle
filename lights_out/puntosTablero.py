import conversorCoordenadas

#coordenadasOriginales= conversorCoordenadas(coordenadas)
"""
PRE: recibe una tupla con las coordenadas validas del usuario traducidasd a nuestra estructura

"""
def generarPuntos(coordenada):

    print(coordenada[0])
    print(coordenada[1])


    punto1 = coordenada[0], coordenada[1] - 1
    punto2 = coordenada[0]-1, coordenada[1]
    punto3 = coordenada[0]+1,  coordenada[1]
    punto4 = coordenada[0], coordenada[1] + 1

    print(punto1)
    print(punto2)
    print(punto3)
    print(punto4)



