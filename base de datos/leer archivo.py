infile =open('bd.sql', 'r')
print('>>> Lectura del fichero línea a línea')

for line in infile:
    print(line)
# Cerramos el fichero.
infile.close()
