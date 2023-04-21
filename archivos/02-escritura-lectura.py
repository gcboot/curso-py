
from pathlib import Path

archivo = Path('archivo-prueba.txt')
text = archivo.read_text('UTF-8').split('\n')
text.insert(0, 'Hola!')
archivo.write_text('\n'.join(text ), 'UTF-8')

print( text )
