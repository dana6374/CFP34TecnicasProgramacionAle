import coordenadas
import puntosTablero
import tablero
import tableroNiveles
import copy
import controlJuego
import menu


def cambiarPuntos(puntos, tableroACambiar):

    conversorDeSimbolos = {".":"o", "o":"."}

    for punto in puntos:
        tableroACambiar[punto[0]][punto[1]] = conversorDeSimbolos[tableroACambiar[punto[0]][punto[1]]]


print("Jugando en modo predeterminado !")
print("")

def jugar():


    if controlJuego.nivel == 6:
         print("Felicitaciones, Finalizó todos los niveles del modo predeterminado")
         print("")
         print("Puntaje nivel 1: ", controlJuego.puntaje[1])
         print("Puntaje nivel 2: ", controlJuego.puntaje[2])
         print("Puntaje nivel 3: ", controlJuego.puntaje[3])
         print("Puntaje nivel 4: ", controlJuego.puntaje[4])
         print("Puntaje nivel 5: ", controlJuego.puntaje[5])
         puntajeTotal= controlJuego.puntaje[1] + controlJuego.puntaje[2] + controlJuego.puntaje[3] + controlJuego.puntaje[4] + controlJuego.puntaje[5]
         print("")
         print("puntaje total: ", puntajeTotal)
         print("")
         menu.mostrarMenu()
    else:
        miTablero = copy.deepcopy(tableroNiveles.llamarNivel[controlJuego.nivel])


    print ("Usted está ahora en el nivel: ", controlJuego.nivel)
    print("")
    while controlJuego.intentos > 0 and not controlJuego.nivelCompleto(miTablero):

        tablero.imprimirTablero(miTablero)
        coordenadasDelUsuario = coordenadas.solicitarCoordenadas()

        print ("")
        print ("La coordenada: ", coordenadasDelUsuario, "es valida")
        print ("")

        puntosACambiar= puntosTablero.generarPuntos(coordenadasDelUsuario, miTablero)
        puntosACambiar.append(coordenadasDelUsuario)
        cambiarPuntos(puntosACambiar, miTablero)
        controlJuego.intentos = controlJuego.intentos-1

        print("Quedan", controlJuego.intentos, "intentos")
        print("")

    if controlJuego.nivelCompleto(miTablero):

        print("nivel ganado")
        print("")

        controlJuego.puntaje[controlJuego.nivel] = controlJuego.puntaje[controlJuego.nivel] + 500

        print("Puntaje del nivel: ", controlJuego.puntaje[controlJuego.nivel])
        print("")
        print ("Ud finalizó el nivel:", controlJuego.nivel)
        print("")

        controlJuego.nivel = controlJuego.nivel + 1
        controlJuego.intentos = 15
        print("cantidad de intentos para éste nivel: ", controlJuego.intentos)

        jugar()



    else:
        print("Juego Perdido")
        controlJuego.puntaje[controlJuego.nivel] = controlJuego.puntaje[controlJuego.nivel] - 300
        print(" ")
        print("Puntaje nivel 1: ", controlJuego.puntaje[1])
        print("Puntaje nivel 2: ", controlJuego.puntaje[2])
        print("Puntaje nivel 3: ", controlJuego.puntaje[3])
        print("Puntaje nivel 4: ", controlJuego.puntaje[4])
        print("Puntaje nivel 5: ", controlJuego.puntaje[5])
        puntajeTotal = controlJuego.puntaje[1] + controlJuego.puntaje[2] + controlJuego.puntaje[3] + controlJuego.puntaje[4] + controlJuego.puntaje[5]
        print("")
        print("Puntaje total: ", puntajeTotal)
        menu.mostrarMenu()