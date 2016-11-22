fila=[" ", "A", "B", "C", "D", "E"]


def imprimirTablero (tablero):

    todaLaFilaEnteraJuntita = ""
    #todaLaFilaEnteraJuntita = "    A B C D E"

    for letra in fila:
        print(letra)


    print(todaLaFilaEnteraJuntita)


    for i, elemento in enumerate(tablero):
        print(i, "|",  elemento[0][0])

    print("")