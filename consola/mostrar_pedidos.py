from reportes.resumen_pedidos import calcular_resumen


class MostrarPedidos:
    def listar(self, pedidos, mensaje_vacio="No hay pedidos para mostrar."):
        if not pedidos:
            print(mensaje_vacio)
            return
        print("\nCÓDIGO | CLIENTE | ENTREGA | ESTADO")
        print("-" * 70)
        for pedido in pedidos:
            print(f"{pedido.codigo} | {pedido.cliente} | {pedido.fecha_entrega} | {pedido.estado}")

    def alertas(self, pedidos, motivo, mensaje_vacio):
        if not pedidos:
            print(mensaje_vacio)
            return
        print("\nCÓDIGO | CLIENTE | ENTREGA | ESTADO | MOTIVO")
        print("-" * 70)
        for pedido in pedidos:
            print(f"{pedido.codigo} | {pedido.cliente} | {pedido.fecha_entrega} | {pedido.estado} | {motivo}")

    def historial(self, pedido):
        print(f"\nHistorial del pedido {pedido.codigo}:")
        for cambio in pedido.historial:
            anterior = cambio.estado_anterior or "(inicio)"
            print(f"  - {cambio.fecha_hora}: {anterior} -> {cambio.estado_nuevo}")

    def detalle(self, pedido):
        print(f"\nPedido: {pedido.codigo}")
        print(f"Cliente: {pedido.cliente}")
        print(f"Registro: {pedido.fecha_registro}")
        print(f"Entrega: {pedido.fecha_entrega}")
        print(f"Estado: {pedido.estado}")
        print("Prendas:")
        for prenda in pedido.prendas:
            print(f"  - {prenda}")
        self.historial(pedido)

    def resumen(self, pedidos, fecha_hoy):
        datos = calcular_resumen(pedidos, fecha_hoy)
        print("\nRESUMEN DE PEDIDOS")
        if datos["total_pedidos"] == 0:
            print("No hay pedidos registrados.")
        print(f"Total de pedidos: {datos['total_pedidos']}")
        print(f"Clientes distintos: {datos['clientes_distintos']}")
        print(f"Pedidos atrasados: {datos['pedidos_atrasados']}")
        print("Pedidos por estado:")
        for estado, cantidad in datos["por_estado"].items():
            print(f"  {estado}: {cantidad}")
