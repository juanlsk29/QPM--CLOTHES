from configuracion import ESTADOS
from reglas_negocio.fechas_entrega import esta_atrasado


def calcular_resumen(pedidos, fecha_hoy):
    por_estado = {estado: 0 for estado in ESTADOS}
    clientes = set()
    for pedido in pedidos:
        por_estado[pedido.estado] += 1
        clientes.add(pedido.cliente.lower())
    atrasados = sum(1 for pedido in pedidos if esta_atrasado(pedido, fecha_hoy))
    return {
        "total_pedidos": len(pedidos),
        "por_estado": por_estado,
        "pedidos_atrasados": atrasados,
        "clientes_distintos": len(clientes)
    }
