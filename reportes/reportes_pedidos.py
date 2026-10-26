from reglas_negocio.fechas_entrega import esta_atrasado


class Reporte:
    encabezados = ("codigo", "cliente", "fecha_registro", "fecha_entrega", "estado")

    def __init__(self, pedidos, fecha_hoy):
        self.pedidos = list(pedidos)
        self.fecha_hoy = fecha_hoy

    @property
    def nombre_archivo(self):
        raise NotImplementedError("Cada reporte debe definir su nombre de archivo.")

    def seleccionar(self):
        raise NotImplementedError("Cada reporte debe implementar seleccionar().")

    def filas(self):
        filas = []
        for pedido in self.seleccionar():
            filas.append({
                "codigo": pedido.codigo,
                "cliente": pedido.cliente,
                "fecha_registro": pedido.fecha_registro,
                "fecha_entrega": pedido.fecha_entrega,
                "estado": pedido.estado
            })
        return filas


class ReportePendientes(Reporte):
    @property
    def nombre_archivo(self): return "pedidos_pendientes.csv"
    def seleccionar(self):
        return [p for p in self.pedidos if p.estado not in ("Entregado", "Cancelado")]


class ReporteEntregados(Reporte):
    @property
    def nombre_archivo(self): return "pedidos_entregados.csv"
    def seleccionar(self):
        return [p for p in self.pedidos if p.estado == "Entregado"]


class ReporteAtrasados(Reporte):
    @property
    def nombre_archivo(self): return "pedidos_atrasados.csv"
    def seleccionar(self):
        return [p for p in self.pedidos if esta_atrasado(p, self.fecha_hoy)]
