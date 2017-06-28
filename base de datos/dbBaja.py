import dbCursor
import dbMenu

def ejec():
    modo= input(str("Eliminar: 1 = Fabricante, 2 = Articulo y precio, 3 = Cliente, 5 = Volver al menú anterior"))

    opciones = {1: "FABRICANTES",
                2: "ARTICULOS",
                3: "CLIENTES"}

    if modo == "1":
       nombre = input(str("Ingrese el nombre del fabricante a eliminar (no debe poseer ningún artículo)."))
       baseDatos.getCursorDeBaseDedatos().execute('DELETE FROM FABRICANTES(NOMBRE) VALUES("{}");'.format(nombre))
       baseDatos.baseDeDatos.commit()

    elif modo == "2":
         nombre = input(str("Ingrese el nombre del Articulo a eliminar "))
         baseDatos.getCursorDeBaseDedatos().execute('DELETE FROM ARTICULOS(NOMBRE) VALUES("{}");'.format(nombre))
         baseDatos.baseDeDatos.commit()

    elif modo == "3":
         nombre = input(str("Ingrese el nombre del Cliente a eliminar "))
         baseDatos.getCursorDeBaseDedatos().execute('DELETE FROM ARTICULOS(NOMBRE) VALUES("{}");'.format(nombre))
         baseDatos.baseDeDatos.commit()

    else:
        print("")
        print("menú anterior")
        print("")
        menuBaseDatos.clearScreen()
        menuBaseDatos.mostrarMenu()


