# Pre: El parámetro "coordenadas" que recibe ésta función es del tipo STRING y mide 2 Caracteres
# Post: Cuando los datos no son válidos se devuelven indices negativos.

def convertirCoordenadas(coordenadas):
    diccionarioColumnas = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}
    diccionarioFilas= {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4}

    if coordenadas[0] in diccionarioColumnas and coordenadas[1] in diccionarioFilas:
        return (diccionarioFilas[coordenadas[1]], diccionarioColumnas[coordenadas[0]])
    else:
        return (-1,-1)
