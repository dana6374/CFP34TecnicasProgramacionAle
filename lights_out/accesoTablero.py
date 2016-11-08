

def letraValida(letra):
    letrasValidas = ("a", "b", "c", "d", "e")
    return letra in letrasValidas


def numeroValido(numero):

    numerosValidos = (1, 2, 3, 4, 5)
    return numero in numerosValidos

def longitudValida(coordenadas):
    return len(coordenadas) == 2

def validarCoordenadas(coordenadas):

    coordenadaInvalida = {"fila":-1,"columna":-1}


    if not longitudValida(coordenadas):
        return coordenadaInvalida

    if not letraValida(coordenadas[0]):
        return coordenadaInvalida

    if not numeroValido(coordenadas[1]):
        return coordenadaInvalida

    return {"fila": 0, "columna": 0}



