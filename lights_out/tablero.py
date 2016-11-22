fila=[" ", "A", "B", "C", "D", "E"]


def imprimirTablero (tablero):

    filaResultado  = " "

    for letra in fila:
        filaResultado = filaResultado + " " + letra

    print(filaResultado)


    for i, elemento in enumerate(tablero):
        print(i+1, "|",  elemento[0][0])

    print("")