
import baseDatos

def ejec():
    modo= input(str("1 = Fabricante, 2 = Articulo y precio, 3 = Cliente, 5= Volver a la opción anterior"))

    opciones = {1: "FABRICANTES",
                2: "ARTICULOS",
                3: "CLIENTES"}

    if modo == "1":
        nombre = input(str("Ingrese el nombre del fabricante. Si existe, no se modifica "))
        baseDatos.getCursorDeBaseDedatos().execute('INSERT INTO FABRICANTES(NOMBRE) VALUES("{}");'.format(nombre))
        baseDatos.baseDeDatos.commit()

    if modo == "2":
        nombre = input(str("Ingrese el nombre, precio del Articulo. Si existe, no se modifica "))
        baseDatos.getCursorDeBaseDedatos().execute('INSERT INTO ARTICULOS(NOMBRE) VALUES("{}");'.format(nombre))
        baseDatos.baseDeDatos.commit()

        nombreArticulo = "prueba"
        precioArticulo = 10
        fabricanteId = 10
        baseDatos.getCursorDeBaseDedatos().execute ('INSERT INTO (NOMBRE, PRECIO, FAB) VALUES ("{}", {}, (SELECT ID FROM FABRICANTES WHERE (NOMBRE = "{}")'.format(nombreArticulo, precioArticulo, fabricanteId))
        baseDatos.commit()