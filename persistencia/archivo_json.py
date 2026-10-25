import json
from pathlib import Path
from excepciones import ErrorArchivoDatos


class ArchivoJSON:
    def __init__(self, ruta):
        self.ruta = Path(ruta)

    def cargar(self):
        if not self.ruta.exists():
            return []
        try:
            with self.ruta.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            if not isinstance(datos, list):
                raise ValueError("La raíz del JSON debe ser una lista.")
            return datos
        except (json.JSONDecodeError, UnicodeDecodeError, ValueError, OSError) as error:
            raise ErrorArchivoDatos(f"El archivo JSON está dañado o no se puede leer: {error}")

    def guardar(self, datos):
        try:
            self.ruta.parent.mkdir(parents=True, exist_ok=True)
            temporal = self.ruta.with_suffix(self.ruta.suffix + ".tmp")
            with temporal.open("w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=4)
            temporal.replace(self.ruta)
        except OSError as error:
            raise ErrorArchivoDatos(f"No se pudieron guardar los pedidos: {error}")
