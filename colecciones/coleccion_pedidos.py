from excepciones import ErrorReglaNegocio
from modelos.pedido import Pedido


class ColeccionPedidos:
    def __init__(self):
        self._pedidos = {}

    def agregar(self, pedido):
        if not isinstance(pedido, Pedido):
            raise TypeError("Solo se pueden agregar objetos Pedido.")
        if pedido.codigo in self._pedidos:
            raise ErrorReglaNegocio(f"Ya existe un pedido con código {pedido.codigo}.")
        self._pedidos[pedido.codigo] = pedido

    def buscar(self, codigo):
        return self._pedidos.get(str(codigo).strip().upper())

    def eliminar(self, codigo):
        self._pedidos.pop(str(codigo).strip().upper(), None)

    def buscar_por_codigo_o_cliente(self, texto):
        texto = str(texto).strip().lower()
        return [p for p in self._pedidos.values()
                if texto in p.codigo.lower() or texto in p.cliente.lower()]

    def buscar_por_cliente(self, cliente):
        texto = str(cliente).strip().lower()
        return [p for p in self._pedidos.values() if texto in p.cliente.lower()]

    def filtrar_por_estado(self, estado):
        return [p for p in self._pedidos.values() if p.estado.lower() == str(estado).lower()]

    def obtener_todos(self):
        return list(self._pedidos.values())

    def cantidad(self):
        return len(self._pedidos)

    def a_lista_diccionarios(self):
        return [p.a_diccionario() for p in self._pedidos.values()]

    def cargar_desde_lista(self, datos):
        temporal = {}
        for elemento in datos:
            pedido = Pedido.desde_diccionario(elemento)
            if pedido.codigo in temporal:
                raise ErrorReglaNegocio(f"El archivo contiene el código duplicado {pedido.codigo}.")
            temporal[pedido.codigo] = pedido
        self._pedidos = temporal
