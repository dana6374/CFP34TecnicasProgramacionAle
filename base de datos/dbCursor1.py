import psycopg2

baseDeDatos = None

def inicializarBaseDeDatos():
    conn_string = "host='10.1.4.115' dbname='alejandra' user='postgres' password='qvg802'"
    global baseDeDatos

    baseDeDatos = psycopg2.connect(conn_string)

    cursorBaseDeDatos = baseDeDatos.cursor()

    archivoSql = open('bd.sql', 'r')

    for linea in archivoSql:
        cursorBaseDeDatos.execute(linea)

    baseDeDatos.commit()
    archivoSql.close()

def getCursorDeBaseDedatos():
    #global baseDeDatos
    return baseDeDatos.cursor()

