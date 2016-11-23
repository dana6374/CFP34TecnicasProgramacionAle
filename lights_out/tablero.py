fila=[" ", "A", "B", "C", "D", "E"]


def imprimirTablero (tablero):

    filaResultado  = " "

    for letra in fila:
        filaResultado = filaResultado + " " + letra

    print(filaResultado)


    for i, elemento in enumerate(tablero):
        filaLuz =  " |"

        for led in elemento:
            filaLuz = filaLuz + led + " "
        print (str(i + 1) + " " + filaLuz)
    print("")