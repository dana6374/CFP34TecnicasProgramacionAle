def AltaDato():
    modo= input(str("1 = Fabricante, 2 = Articulos, 3 = Cliente, 5= Volver a la opción anterior"))

    opc = {1: "FABRICANTES",
           2: "ARTICULOS",
           3: "CLIENTES"}

    if modo == 1:
        c.execute('INSERT INTO FABRICANTES(NOMBRE) VALUES("{}");'.format(nombre))
        base.commit()
    #PUEDE SER QUE LA OPCION DEL USUARIOS ESTÉ EN LA VARIABLE OPC?

    if modo == 2:
        c.execute ('INSERT INTO (NOMBRE, PRECIO, FAB) VALUES ("{}", {}, (SELECT ID FROM FABRICANTES WHERE (NOMBRE = "{}")'.format(NOMBRE, PRECIO, FABRICANTE))
        base.commit()