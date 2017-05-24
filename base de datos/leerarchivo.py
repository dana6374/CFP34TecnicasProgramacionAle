import sqlite3

base = sqlite3.connect('pi2.db')
c = base.cursor()

infile=open('bd.sql', 'r')
print('>>> Lectura del fichero línea a línea')

for line in infile:
    c.execute(line)
# Cerramos el fichero.
infile.close()
