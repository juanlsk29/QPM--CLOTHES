import tempfile, csv
from pathlib import Path
from modelos.pedido import Pedido
from modelos.prenda import Prenda
from reportes.reportes_pedidos import ReportePendientes, ReporteEntregados, ReporteAtrasados
from reportes.exportar_csv import ExportadorCSV
from reportes.resumen_pedidos import calcular_resumen
from pruebas.comprobar import comprobar


def ejecutar():
    p1 = Pedido("Q-1", "Ana", "2026-10-20", "2026-10-22", [Prenda("Camiseta", "S", "blanco", 1)])
    p2 = Pedido("Q-2", "Luis", "2026-10-20", "2026-10-20", [Prenda("Pantalón", "M", "azul", 1)], estado="Entregado")
    comprobar("reporte pendientes", len(ReportePendientes([p1, p2], "2026-10-21").seleccionar()) == 1)
    comprobar("reporte entregados", len(ReporteEntregados([p1, p2], "2026-10-21").seleccionar()) == 1)
    comprobar("reporte atrasados", len(ReporteAtrasados([p1, p2], "2026-10-23").seleccionar()) == 1)
    with tempfile.TemporaryDirectory() as carpeta:
        ruta = ExportadorCSV(carpeta).exportar(ReportePendientes([p1], "2026-10-21"))
        with ruta.open(encoding="utf-8-sig") as archivo:
            filas = list(csv.DictReader(archivo))
        comprobar("CSV tiene encabezados y filas", len(filas) == 1 and "codigo" in filas[0])
    with tempfile.TemporaryDirectory() as carpeta:
        ruta = ExportadorCSV(carpeta).exportar(ReporteEntregados([p1], "2026-10-21"))
        with ruta.open(encoding="utf-8-sig") as archivo:
            lineas = archivo.read().splitlines()
        comprobar("CSV sin pedidos solo trae encabezados",
                  lineas == ["codigo,cliente,fecha_registro,fecha_entrega,estado"])
    vacio = calcular_resumen([], "2026-10-23")
    comprobar("resumen sin pedidos muestra ceros",
              vacio["total_pedidos"] == 0 and vacio["pedidos_atrasados"] == 0 and all(v == 0 for v in vacio["por_estado"].values()))
    resumen = calcular_resumen([p1, p2], "2026-10-23")
    comprobar("resumen cuenta por estado", resumen["por_estado"]["Recibido"] == 1 and resumen["por_estado"]["Entregado"] == 1)
    comprobar("resumen calcula total y atrasados", resumen["total_pedidos"] == 2 and resumen["pedidos_atrasados"] == 1)
