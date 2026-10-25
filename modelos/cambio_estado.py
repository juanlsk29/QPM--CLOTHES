from validaciones.validar_fecha import validar_fecha_hora
from validaciones.validar_pedido import validar_estado


class CambioEstado:
    def __init__(self, estado_anterior, estado_nuevo, fecha_hora):
        self._estado_anterior = validar_estado(estado_anterior) if estado_anterior else ""
        self._estado_nuevo = validar_estado(estado_nuevo)
        self._fecha_hora = validar_fecha_hora(fecha_hora)

    @property
    def estado_anterior(self):
        return self._estado_anterior

    @property
    def estado_nuevo(self):
        return self._estado_nuevo

    @property
    def fecha_hora(self):
        return self._fecha_hora

    def a_diccionario(self):
        return {"estado_anterior": self.estado_anterior, "estado_nuevo": self.estado_nuevo,
                "fecha_hora": self.fecha_hora}

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos.get("estado_anterior", ""), datos["estado_nuevo"], datos["fecha_hora"])
