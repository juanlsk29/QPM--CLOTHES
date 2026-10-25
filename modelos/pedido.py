from modelos.prenda import Prenda
from modelos.cambio_estado import CambioEstado
from validaciones.validar_pedido import validar_codigo, validar_cliente, validar_fechas_pedido, validar_estado
from validaciones.validar_fecha import validar_fecha_hora
from configuracion import ESTADO_INICIAL
from excepciones import ErrorValidacion


class Pedido:
    def __init__(self, codigo, cliente, fecha_registro, fecha_entrega, prendas=None, estado=ESTADO_INICIAL,
                 historial=None):
        self._codigo = validar_codigo(codigo)
        self._cliente = validar_cliente(cliente)
        self._fecha_registro, self._fecha_entrega = validar_fechas_pedido(fecha_registro, fecha_entrega)
        self._estado = validar_estado(estado)
        self._prendas = []
        for prenda in (prendas or []):
            self._prendas.append(prenda if isinstance(prenda, Prenda) else Prenda.desde_diccionario(prenda))
        if not self._prendas:
            raise ErrorValidacion("El pedido debe contener al menos una prenda.")
        self._historial = []
        for cambio in (historial or []):
            self._historial.append(cambio if isinstance(cambio, CambioEstado) else CambioEstado.desde_diccionario(cambio))
        if not self._historial:
            self._historial.append(CambioEstado("", self._estado, f"{self._fecha_registro} 00:00"))

    @property
    def codigo(self): return self._codigo
    @property
    def cliente(self): return self._cliente
    @property
    def fecha_registro(self): return self._fecha_registro
    @property
    def fecha_entrega(self): return self._fecha_entrega
    @property
    def estado(self): return self._estado
    @property
    def prendas(self): return list(self._prendas)
    @property
    def historial(self): return list(self._historial)

    def agregar_prenda(self, prenda):
        if not isinstance(prenda, Prenda):
            prenda = Prenda.desde_diccionario(prenda)
        self._prendas.append(prenda)

    def cambiar_estado(self, estado_nuevo, fecha_hora):
        estado_nuevo = validar_estado(estado_nuevo)
        cambio = CambioEstado(self._estado, estado_nuevo, fecha_hora)
        self._historial.append(cambio)
        self._estado = estado_nuevo

    def actualizar_cliente(self, cliente):
        self._cliente = validar_cliente(cliente)

    def reemplazar_prendas(self, prendas):
        nuevas = [p if isinstance(p, Prenda) else Prenda.desde_diccionario(p) for p in prendas]
        if not nuevas:
            raise ErrorValidacion("El pedido debe contener al menos una prenda.")
        self._prendas = nuevas

    def deshacer_ultimo_cambio(self):
        """Revierte el último cambio de estado cuando no se pudo guardar."""
        if len(self._historial) > 1:
            cambio = self._historial.pop()
            self._estado = cambio.estado_anterior

    def actualizar_fecha_entrega(self, fecha_entrega):
        _, fecha_entrega = validar_fechas_pedido(self._fecha_registro, fecha_entrega)
        self._fecha_entrega = fecha_entrega

    def esta_finalizado(self):
        return self._estado in ("Entregado", "Cancelado")

    def a_diccionario(self):
        return {"codigo": self.codigo, "cliente": self.cliente, "fecha_registro": self.fecha_registro,
                "fecha_entrega": self.fecha_entrega, "estado": self.estado,
                "prendas": [p.a_diccionario() for p in self._prendas],
                "historial": [c.a_diccionario() for c in self._historial]}

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["codigo"], datos["cliente"], datos["fecha_registro"], datos["fecha_entrega"],
                   datos.get("prendas", []), datos.get("estado", ESTADO_INICIAL), datos.get("historial", []))

    def __str__(self):
        return f"{self.codigo} | {self.cliente} | Entrega: {self.fecha_entrega} | Estado: {self.estado}"
