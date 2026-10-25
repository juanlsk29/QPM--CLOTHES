import tempfile
from pathlib import Path
from persistencia.archivo_json import ArchivoJSON
from excepciones import ErrorArchivoDatos
from pruebas.comprobar import comprobar


def ejecutar():
    with tempfile.TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / "pedidos.json"
        archivo = ArchivoJSON(ruta)
        comprobar("archivo inexistente produce lista vacía", archivo.cargar() == [])
        archivo.guardar([{"codigo": "Q-1"}])
        comprobar("guardar y cargar JSON", archivo.cargar() == [{"codigo": "Q-1"}])
        ruta.write_text("{json roto", encoding="utf-8")
        contenido = ruta.read_text(encoding="utf-8")
        try:
            archivo.cargar()
            fallo = False
        except ErrorArchivoDatos:
            fallo = True
        comprobar("JSON dañado genera excepción", fallo)
        comprobar("JSON dañado no se modifica", ruta.read_text(encoding="utf-8") == contenido)
