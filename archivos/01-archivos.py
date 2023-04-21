
from pathlib import Path
from time import ctime

archivo = Path("archivo-prueba.txt")
# archivo.exists()
# archivo.rename()
# archivo.unlink()

# print(archivo.stat())

print('acceso', ctime(archivo.stat().st_atime))
print('Creación', ctime(archivo.stat().st_ctime))
print('Modificación', ctime(archivo.stat().st_mtime))
