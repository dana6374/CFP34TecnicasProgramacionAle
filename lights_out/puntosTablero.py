import conversorCoordenadas
import tablero

#coordenadasOriginales= conversorCoordenadas(coordenadas)
"""
PRE: recibe una tupla con las coordenadas validas del usuario traducidasd a nuestra estructura

"""
def generarPuntos(coordenada,tablero):

    print(coordenada[0], coordenada[1])


    punto1 = coordenada[0], coordenada[1] - 1

    if punto1[0] >0 and punto1[0] <= len(tablero):
        if punto1[1] >0 and punto1[1]<= (len(tablero[0])-1):
            print(punto1)
            print("punto valido")

    punto2 = coordenada[0]-1, coordenada[1]
    print(punto2)

    punto3 = coordenada[0]+1,  coordenada[1]
    print(punto3)

    punto4 = coordenada[0], coordenada[1] + 1
    if punto4[0] >0 and punto4[0] <= len(tablero):
        if punto4[1] >=0 and punto4[1]<= (len(tablero[0])-1):
            print(punto4)
            print("punto valido")
        else:
            print("punto inválido")



