
from pathlib import Path
import json



# # escribir json

# productos = [
#     {'id': 1, 'name': 'Surfboard'},
#     {'id': 2, 'name': 'Bicicleta'},
#     {'id': 3, 'name': 'Skate'}
# ]

# data = json.dumps( productos )

# Path('productos.json').write_text(data)

# Leer Json
data = Path('productos.json').read_text(encoding='UTF-8')
productos = json.loads(data)
print( productos )

# Modificar Json
productos[0]['name'] = "Surfboard"
Path('productos.json').write_text(json.dumps(productos), encoding="UTF-8")
