from modelos.pedido import Pedido
from modelos.cambio_estado import CambioEstado
from configuracion import ESTADO_INICIAL
from excepciones import ErrorReglaNegocio, ErrorArchivoDatos
from reglas_negocio.estados_pedido import validar_transicion, permite_edicion
from reglas_negocio.fechas_entrega import esta_atrasado, esta_proximo_a_vencer
from validaciones.validar_pedido import (validar_codigo, validar_cliente, validar_fechas_pedido,
                                         validar_estado, validar_texto_busqueda)
from validaciones.validar_fecha import validar_fecha_hora, fecha_hora_a_tupla


class GestorPedidos:
    def __init__(self, coleccion, archivo_json, bitacora=None):
        self.coleccion = coleccion
        self.archivo_json = archivo_json
        self.bitacora = bitacora
        self.fecha_hora_trabajo = None

    # fecha y hora de trabajo
    def _ultimo_movimiento(self):
        ultimo = None
        for pedido in self.coleccion.obtener_todos():
            for cambio in pedido.historial:
                if ultimo is None or fecha_hora_a_tupla(cambio.fecha_hora) > fecha_hora_a_tupla(ultimo):
                    ultimo = cambio.fecha_hora
        return ultimo

    def actualizar_fecha_hora_trabajo(self, fecha_hora):
        fecha_hora = validar_fecha_hora(fecha_hora)
        ultimo = self._ultimo_movimiento()
        if ultimo is not None and fecha_hora_a_tupla(fecha_hora) < fecha_hora_a_tupla(ultimo):
            raise ErrorReglaNegocio(
                f"La fecha y hora de trabajo no puede ser anterior al último movimiento registrado ({ultimo}).")
        self.fecha_hora_trabajo = fecha_hora

    def _ahora(self):
        if self.fecha_hora_trabajo is None:
            raise ErrorReglaNegocio("Primero debe definir la fecha y hora de trabajo.")
        return self.fecha_hora_trabajo

    def _hoy(self):
        return self._ahora().split(" ")[0]

    def _guardar(self):
        try:
            self.archivo_json.guardar(self.coleccion.a_lista_diccionarios())
        except ErrorArchivoDatos as error:
            if self.bitacora:
                self.bitacora.registrar(f"Error de persistencia: {error}")
            raise

    # operaciones
    def registrar_pedido(self, codigo, cliente, fecha_entrega, prendas):
        codigo = validar_codigo(codigo)
        cliente = validar_cliente(cliente)
        ahora = self._ahora()
        fecha_registro = ahora.split(" ")[0]
        validar_fechas_pedido(fecha_registro, fecha_entrega)
        if self.coleccion.buscar(codigo):
            raise ErrorReglaNegocio(f"Ya existe un pedido con código {codigo}.")
        historial = [CambioEstado("", ESTADO_INICIAL, ahora)]
        pedido = Pedido(codigo, cliente, fecha_registro, fecha_entrega, prendas, ESTADO_INICIAL, historial)
        self.coleccion.agregar(pedido)
        try:
            self._guardar()
        except Exception:
            self.coleccion.eliminar(codigo)
            raise
        return pedido

    def obtener_pedido(self, codigo):
        pedido = self.coleccion.buscar(codigo)
        if not pedido:
            raise ErrorReglaNegocio(f"No se encontró el pedido {str(codigo).strip().upper()}.")
        return pedido

    def actualizar_pedido(self, codigo, cliente=None, fecha_entrega=None, prendas=None):
        pedido = self.obtener_pedido(codigo)
        if not permite_edicion(pedido.estado):
            raise ErrorReglaNegocio("Solo se editan pedidos en estado Recibido o En preparación.")
        cliente_anterior = pedido.cliente
        entrega_anterior = pedido.fecha_entrega
        prendas_anteriores = pedido.prendas
        try:
            if cliente is not None:
                pedido.actualizar_cliente(cliente)
            if fecha_entrega is not None:
                pedido.actualizar_fecha_entrega(fecha_entrega)
            if prendas is not None:
                pedido.reemplazar_prendas(prendas)
            self._guardar()
        except Exception:
            pedido.actualizar_cliente(cliente_anterior)
            pedido.actualizar_fecha_entrega(entrega_anterior)
            pedido.reemplazar_prendas(prendas_anteriores)
            raise
        return pedido

    def cambiar_estado(self, codigo, estado_nuevo):
        pedido = self.obtener_pedido(codigo)
        estado_nuevo = validar_estado(estado_nuevo)
        validar_transicion(pedido.estado, estado_nuevo)
        pedido.cambiar_estado(estado_nuevo, self._ahora())
        try:
            self._guardar()
        except Exception:
            pedido.deshacer_ultimo_cambio()
            raise
        return pedido

    def cancelar_pedido(self, codigo):
        return self.cambiar_estado(codigo, "Cancelado")

    # consultas
    def buscar_por_cliente(self, cliente):
        return self.coleccion.buscar_por_cliente(cliente)

    def buscar_por_codigo_o_cliente(self, texto):
        return self.coleccion.buscar_por_codigo_o_cliente(validar_texto_busqueda(texto))

    def filtrar_por_estado(self, estado):
        return self.coleccion.filtrar_por_estado(validar_estado(estado))

    def listar_pedidos(self):
        return self.coleccion.obtener_todos()

    def pedidos_atrasados(self):
        hoy = self._hoy()
        return [p for p in self.listar_pedidos() if esta_atrasado(p, hoy)]

    def pedidos_proximos_a_vencer(self):
        hoy = self._hoy()
        return [p for p in self.listar_pedidos() if esta_proximo_a_vencer(p, hoy)]

    def historial_pedido(self, codigo):
        return self.obtener_pedido(codigo).historial
