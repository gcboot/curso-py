
from io import open

# Escritura
# text = 'Hola!'

# archivo = open('hola.txt', 'w')
# archivo.write( text )
# archivo.close()

# Lectura

# archivo = open('hola.txt', 'r')
# text = archivo.read()
# archivo.close()
# print( text )

# Lectura como lista
# archivo = open( 'hola.txt', 'r')
# text = archivo.readline()
# archivo.close()
# print( text )

# with y seek
# with open('hola.txt', 'r') as archivo:
#     print(archivo.readline())
#     archivo.seek(0)
#     for line in archivo:
#         print(line)

# agregar
# archivo = open('hola.txt', 'a+')
# archivo.write('Adios :(')
# archivo.close()

# Lectura y escritura
# with open('hola.txt', 'r+') as archivo:
#     text = archivo.readlines()
#     archivo.seek(0)
#     text[0] = 'Victor'
#     print( text )
#     archivo.writelines( text )
