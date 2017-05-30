
import baseDatos

def ejec():
    modo= input(str("1 = Fabricante, 2 = Articulos, 3 = Cliente, 5= Volver a la opción anterior"))

    opciones = {1: "FABRICANTES",
           2: "ARTICULOS",
           3: "CLIENTES"}

    if modo == "1":
        nombre = 'Ale'
        #TODO: pedirle al usuario que nombre quiere ponerle al fabricante
        baseDatos.getCursorDeBaseDedatos().execute('INSERT INTO FABRICANTES(NOMBRE) VALUES("{}");'.format(nombre))
        baseDatos.baseDeDatos.commit()
    #PUEDE SER QUE LA OPCION DEL USUARIOS ESTÉ EN LA VARIABLE OPC?

    if modo == "2":
        #TODO: pedirle al usuario que nombre quiere ponerle al articulo
        #TODO: pedirle al usuario que precio quiere ponerle al articulo
        #TODO: pedirle al usuario que  ID tiene al articulo

        nombreArticulo = "prueba"
        precioArticulo = 10
        fabricanteId = 10
        baseDatos.getCursorDeBaseDedatos().execute ('INSERT INTO (NOMBRE, PRECIO, FAB) VALUES ("{}", {}, (SELECT ID FROM FABRICANTES WHERE (NOMBRE = "{}")'.format(nombreArticulo, precioArticulo, fabricanteId))
        baseDatos.commit()