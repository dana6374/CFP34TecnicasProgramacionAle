# El parámetro "coordenadas" que recibe ésta función es del tipo STRING y mide 2 Caracteres

def convertirCoordenadas(coordenadas):
    diccionarioColumnas = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}
    diccionarioFilas= {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4}

    for coordenadas[1] in diccionarioColumnas:
        for coordenadas[0] in diccionarioFilas:
            print(diccionarioFilas, diccionarioColumnas)



    return coordenadas