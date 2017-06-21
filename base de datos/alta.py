import baseDatos
import menuBaseDatos

def ejec():
    modo= input(str("1 = Fabricante, 2 = Articulo y precio, 3 = Cliente, 4= Volver al menú anterior"))

    opciones = {1: "FABRICANTES",
                2: "ARTICULOS",
                3: "CLIENTES"}

    if modo == "1":
        nombre = input(str("Ingrese el nombre del fabricante. Si existe, no se modifica "))
        baseDatos.getCursorDeBaseDedatos().execute('INSERT INTO FABRICANTES(NOMBRE) VALUES("{}");'.format(nombre))
        baseDatos.baseDeDatos.commit()

    elif modo == "2":
        nombre = input(str("Ingrese el nombre, precio del Articulo. Si existe, no se modifica "))
        baseDatos.getCursorDeBaseDedatos().execute('INSERT INTO ARTICULOS(NOMBRE, PRECIO, ART_FAB) VALUES("{}",{},{});'.format(nombre))
        baseDatos.baseDeDatos.commit()

    elif modo =="3":
        nombre =input(str("ingrere los datos del Cliente (Apellido y Nombre, Dirección, Teléfono, email, CUIL)"))
        baseDatos.getCursorDeBaseDedatos().execute('INSERT INTO CLIENTE (ApellidoNombre, Direccion, telefono, email, CUIL) VALUES ("{}","{}",{},"{}",{});'.format(nombre))
        baseDatos.baseDeDatos.commit()

    else:
        print("")
        print("menú anterior")
        print("")
        menuBaseDatos.clearScreen()
        menuBaseDatos.mostrarMenu()
