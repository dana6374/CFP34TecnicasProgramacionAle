import baseDatos

def ejec():
    modo= input(str("1 = Fabricante, 2 = Articulo y precio, 3 = Cliente, 5= Volver a la opción anterior"))

    opciones = {1: "FABRICANTES",
                2: "ARTICULOS",
                3: "CLIENTES"}

    if modo == "1":
        nombre = input(str("Ingrese el nombre del fabricante a eliminar (no debe poseer ningún artículo)."))
        baseDatos.getCursorDeBaseDedatos().execute('DELETE FROM FABRICANTES(NOMBRE) VALUES("{}");'.format(nombre))
        baseDatos.baseDeDatos.commit()

    if modo == "2":
        nombre = input(str("Ingrese el nombre del Articulo a eliminar "))
        baseDatos.getCursorDeBaseDedatos().execute('DELETE FROM ARTICULOS(NOMBRE) VALUES("{}");'.format(nombre))
        baseDatos.baseDeDatos.commit()

