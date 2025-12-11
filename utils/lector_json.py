import json
from pathlib import Path

def leer_json(ruta_archivo):
    ruta = Path(ruta_archivo)
    with ruta.open("r",encoding="utf-8") as archivo:
        productos = json.load(archivo)
    
    nombres= [productos["nombre"] for productos in productos]
    return nombres