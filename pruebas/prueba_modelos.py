from modelos.pedido import Pedido
from modelos.prenda import Prenda
from pruebas.comprobar import comprobar
from excepciones import ErrorValidacion


def ejecutar():
    p = Prenda("Camiseta", "M", "azul", 2)
    pedido = Pedido("Q-001", "Ana Pérez", "2026-10-23", "2026-10-25", [p])
    datos = pedido.a_diccionario()
    recuperado = Pedido.desde_diccionario(datos)
    comprobar("crear pedido y prenda", pedido.codigo == "Q-001" and len(pedido.prendas) == 1)
    comprobar("serialización y reconstrucción", recuperado.cliente == pedido.cliente and recuperado.prendas[0].cantidad == 2)
    comprobar("historial inicial creado", len(pedido.historial) == 1)
    try:
        Pedido("Q-002", "Cliente", "2026-10-23", "2026-10-25", [])
        sin_prendas_rechazado = False
    except ErrorValidacion:
        sin_prendas_rechazado = True
    comprobar("rechaza pedido sin prendas", sin_prendas_rechazado)
