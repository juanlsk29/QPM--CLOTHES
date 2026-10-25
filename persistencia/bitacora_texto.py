from pathlib import Path


class BitacoraTexto:
    def __init__(self, ruta):
        self.ruta = Path(ruta)

    def registrar(self, mensaje):
        self.ruta.parent.mkdir(parents=True, exist_ok=True)
        with self.ruta.open("a", encoding="utf-8") as archivo:
            archivo.write(str(mensaje).strip() + "\n")

    def leer(self):
        if not self.ruta.exists():
            return []
        with self.ruta.open("r", encoding="utf-8") as archivo:
            return archivo.read().splitlines()
