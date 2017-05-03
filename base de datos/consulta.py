def ejec()
    opcion = (input(str("seleccione: 1 = Estructura de Base de datos, 2 = listado de fabricantes, 3= listado de Artículos")))

if opcion == "2":
    c.execute()
if opcion == "2":
   c.execute("SELECT * FROM FABRICANTES")
if opcion == "3":
    c.execute("SELECT * FROM ARTICULOS")
