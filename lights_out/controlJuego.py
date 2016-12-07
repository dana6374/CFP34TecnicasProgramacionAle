import juegoPredeterminado


#guardar datos del usuario

puntaje = {1:0,2:0,3:0,4:0,5:0}
nivel = 1
intentos = 15

def nivelCompleto(miTablero):

    for i in miTablero:
        for elemento in i:
             if elemento != ".":
                return False
    return True