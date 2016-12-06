import juegoPredeterminado


def nivelCompleto(miTablero):

    for i in miTablero:
        for elemento in i:
             if elemento != ".":
                return False
    return True