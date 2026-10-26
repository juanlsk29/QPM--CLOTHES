from validaciones.validar_prenda import validar_tipo, validar_talla, validar_color, validar_cantidad


class Prenda:
    def __init__(self, tipo, talla, color, cantidad):
        self._tipo = validar_tipo(tipo)
        self._talla = validar_talla(talla)
        self._color = validar_color(color)
        self._cantidad = validar_cantidad(cantidad)

    @property
    def tipo(self):
        return self._tipo

    @property
    def talla(self):
        return self._talla

    @property
    def color(self):
        return self._color

    @property
    def cantidad(self):
        return self._cantidad

    def a_diccionario(self):
        return {"tipo": self.tipo, "talla": self.talla, "color": self.color, "cantidad": self.cantidad}

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["tipo"], datos["talla"], datos["color"], datos["cantidad"])

    def __str__(self):
        return f"{self.tipo} | Talla {self.talla} | {self.color} | Cantidad: {self.cantidad}"
