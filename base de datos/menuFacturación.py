import baseDatos
import menuBaseDatos

def mostrarMenu():

    print(" ")
    print("Facturación")
    print(" ")

    modo = input(str("Elija el modo: 1 = Generar Factura, Consultar Factura: 21 = Por Número, 22 = por Cliente, 23 = por período,  3= SALIR "))

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
