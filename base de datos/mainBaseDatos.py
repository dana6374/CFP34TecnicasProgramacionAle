import sqlite3
import menuBaseDatos

base = sqlite3.connect('d:\pi.db')
c = base.cursor()


print(" ")
print("ABMC BD")
print(" ")

menuBaseDatos.mostrarMenu()
