import coordenadas
import puntosTablero
import tablero
import tableroNiveles
import copy
import controlJuego



def cambiarPuntos(puntos, tableroACambiar):

    conversorDeSimbolos = {".":"o", "o":"."}

    for punto in puntos:
        tableroACambiar[punto[0]][punto[1]] = conversorDeSimbolos[tableroACambiar[punto[0]][punto[1]]]



def jugar():

    print ("Jugando en modo predeterminado !")
    print ("")
    print ("movimiento")

    # Tengo que mostrar el tablero del nivel1 Declarar variable y hacer una copia.


    puntaje = 0
    nivel = 1

    miTablero = copy.deepcopy(tableroNiveles.llamarNivel[nivel])
    # donde dice estructuraTablero1, el 1 es una variable para nivel. Ese nro tiene que ser una variable.

    intentos = 15

    while intentos > 0 and not controlJuego.nivelCompleto(miTablero):

        tablero.imprimirTablero(miTablero)

        coordenadasDelUsuario = coordenadas.solicitarCoordenadas()
        print ("")
        print ("La coordenada: ", coordenadasDelUsuario, "es valida")
        print ("")

        puntosACambiar= puntosTablero.generarPuntos(coordenadasDelUsuario, miTablero)

        puntosACambiar.append(coordenadasDelUsuario)

        cambiarPuntos(puntosACambiar, miTablero)

        intentos = intentos-1
        print("Quedan", intentos, "intentos")
        print("")


    if controlJuego.nivelCompleto(miTablero):

        print("nivel ganado")
        print("")
        puntaje = puntaje + 500
        print("Puntaje final: ", puntaje)
        nivel = nivel + 1

    else:
        print("perdí")
        puntaje = punjate - 300
        print ("Puntaje final: ", puntaje)