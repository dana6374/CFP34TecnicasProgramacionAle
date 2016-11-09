def longitudValida(coordenadas):
    return len(coordenadas) == 2


def letraValida(letra):
    letrasValidas = ("a", "b", "c", "d", "e")
    return letra in letrasValidas


def numeroValido(numero):
    numerosValidos = ("1", "2", "3", "4", "5")
    return numero in numerosValidos


def esCoordenadaValida(coordenadas):

    if not longitudValida(coordenadas):
        print("la coordenada ingresada no es válida")
        return False


    if not letraValida(coordenadas[0]):
        print("la coordenada ingresada no es válida")
        return False


    if not numeroValido(coordenadas[1]):
        print("la coordenada ingresada no es válida")
        return False


    return True

