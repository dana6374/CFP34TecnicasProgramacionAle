import baseDatos
import menuBaseDatos

def mostrarMenu():

    print(" ")
    print("Facturación")
    print(" ")

    modo = input(str("Elija el modo: 1 = Generar Factura, Consultar Factura: 2.1 = Por Número, 2.2 = por Cliente, 2.3 = por período,  3= SALIR "))


    opciones = {1: "Generar_factura",
                2: "Consultar_Factura_ID",
                3: "Consultar_Factura_Cliente"
                4: "Consultar_Factura_Perido"}


    if modo == "1":
        print("")
        print("Generar Factura")
        FacturaNueva.ejec()

    elif modo == "21":
        print("")
        print("Consulta de Facturación por Número de Factura")
        FacturaConsulta.Numeración()

    elif modo == "22":
        print("")
        print("Consulta de Facturación por Cliente")
        FacturaConsulta.Cliente()

    elif modo == "23":
        print("")
        print("Consulta de Facturación por Rango de Fechas")
        FacturaConsulta.Cliente()
