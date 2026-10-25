from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_DATOS = BASE_DIR / "datos"
RUTA_PEDIDOS = RUTA_DATOS / "pedidos.json"
RUTA_BITACORA = RUTA_DATOS / "bitacora.txt"
RUTA_REPORTES = RUTA_DATOS / "reportes_csv"

ESTADOS = ("Recibido", "En preparacion", "Listo", "Entregado", "Cancelado")
ESTADO_INICIAL = "Recibido"
ESTADOS_FINALES = ("Entregado", "Cancelado")
TIPOS_PRENDA = ("Camiseta", "Pantalon", "Buzo", "Chaqueta", "Vestido", "Falda", "Short", "Otro")
TALLAS = ("XS", "S", "M", "L", "XL", "XXL", "Unica")
DIAS_VENCIMIENTO = 2
DIAS_POR_MES = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
