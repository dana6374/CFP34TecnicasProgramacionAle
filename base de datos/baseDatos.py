import sqlite3

baseDeDatos = None

def inicializarBaseDeDatos():

    global baseDeDatos

    baseDeDatos = sqlite3.connect('pi2.db')

    cursorBaseDeDatos = baseDeDatos.cursor()

    archivoSql = open('bd.sql', 'r')

    for linea in archivoSql:
        cursorBaseDeDatos.execute(linea)

    baseDeDatos.commit()
    archivoSql.close()

def getCursorDeBaseDedatos():
    #global baseDeDatos
    return baseDeDatos.cursor()

