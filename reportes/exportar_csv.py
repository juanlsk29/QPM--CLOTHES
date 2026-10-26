import csv
from pathlib import Path
from excepciones import ErrorArchivoDatos


class ExportadorCSV:
    def __init__(self, carpeta_destino):
        self.carpeta_destino = Path(carpeta_destino)

    def exportar(self, reporte):
        ruta = self.carpeta_destino / reporte.nombre_archivo
        try:
            self.carpeta_destino.mkdir(parents=True, exist_ok=True)
            with ruta.open("w", newline="", encoding="utf-8-sig") as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=reporte.encabezados)
                escritor.writeheader()
                escritor.writerows(reporte.filas())
            return ruta
        except (OSError, csv.Error) as error:
            raise ErrorArchivoDatos(f"No se pudo exportar el reporte CSV: {error}")
