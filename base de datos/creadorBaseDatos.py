import sqlite3

def inicializarBaseDeDatos():

    base = sqlite3.connect('pi2.db')

    cursorBaseDeDatos = base.cursor()

    archivoSql = open('bd.sql', 'r')

    for linea in archivoSql:
        cursorBaseDeDatos.execute(linea)

    archivoSql.close()
