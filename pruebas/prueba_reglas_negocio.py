import tempfile
from pathlib import Path
from reglas_negocio.estados_pedido import validar_transicion, permite_edicion
from reglas_negocio.fechas_entrega import esta_atrasado, esta_proximo_a_vencer
from reglas_negocio.gestor_pedidos import GestorPedidos
from colecciones.coleccion_pedidos import ColeccionPedidos
from persistencia.archivo_json import ArchivoJSON
from modelos.pedido import Pedido
from modelos.prenda import Prenda
from excepciones import ErrorReglaNegocio, ErrorValidacion
from pruebas.comprobar import comprobar

PRENDA = {"tipo": "Camiseta", "talla": "M", "color": "azul", "cantidad": 2}


def _lanza(excepcion, funcion, *args, **kwargs):
    try:
        funcion(*args, **kwargs)
        return False
    except excepcion:
        return True


def _crear_gestor(carpeta):
    archivo = ArchivoJSON(Path(carpeta) / "pedidos.json")
    gestor = GestorPedidos(ColeccionPedidos(), archivo)
    gestor.actualizar_fecha_hora_trabajo("2026-10-24 10:00")
    return gestor, archivo


def ejecutar():
    comprobar("transición permitida", not _lanza(ErrorReglaNegocio, validar_transicion, "Recibido", "En preparacion"))
    comprobar("transición no permitida rechazada", _lanza(ErrorReglaNegocio, validar_transicion, "Entregado", "Recibido"))
    comprobar("no se salta de Recibido a Listo", _lanza(ErrorReglaNegocio, validar_transicion, "Recibido", "Listo"))
    comprobar("edición solo en Recibido y En preparacion",
              permite_edicion("Recibido") and permite_edicion("En preparacion")
              and not permite_edicion("Listo") and not permite_edicion("Entregado") and not permite_edicion("Cancelado"))

    p = Pedido("Q-10", "Cliente Uno", "2026-10-20", "2026-10-22", [Prenda("Camiseta", "M", "negro", 1)])
    comprobar("pedido próximo a vencer", esta_proximo_a_vencer(p, "2026-10-21"))
    comprobar("pedido atrasado", esta_atrasado(p, "2026-10-23"))
    comprobar("vencimiento fuera de la ventana de 2 días", not esta_proximo_a_vencer(p, "2026-10-19"))
    entregado = Pedido("Q-11", "Cliente Dos", "2026-10-20", "2026-10-21", [Prenda("Camiseta", "M", "negro", 1)],
                       estado="Entregado")
    comprobar("entregado nunca aparece atrasado", not esta_atrasado(entregado, "2026-12-01"))

    with tempfile.TemporaryDirectory() as carpeta:
        gestor, archivo = _crear_gestor(carpeta)
        pedido = gestor.registrar_pedido("q-1", "Ana Pérez", "2026-10-26", [PRENDA])
        comprobar("registrar: código normalizado y estado inicial", pedido.codigo == "Q-1" and pedido.estado == "Recibido")
        comprobar("registrar: historial inicial con fecha y hora de trabajo",
                  pedido.historial[0].fecha_hora == "2026-10-24 10:00" and pedido.historial[0].estado_anterior == "")
        comprobar("registrar: código duplicado rechazado",
                  _lanza(ErrorReglaNegocio, gestor.registrar_pedido, "Q-1", "Otro", "2026-10-26", [PRENDA]))
        comprobar("registrar: sin prendas rechazado y no se crea",
                  _lanza(ErrorValidacion, gestor.registrar_pedido, "Q-2", "Luis", "2026-10-26", [])
                  and gestor.coleccion.buscar("Q-2") is None)
        comprobar("registrar: entrega anterior al registro rechazada",
                  _lanza(ErrorValidacion, gestor.registrar_pedido, "Q-3", "Luis", "2026-10-01", [PRENDA]))
        comprobar("registrar: cantidad inválida rechazada",
                  _lanza(ErrorValidacion, gestor.registrar_pedido, "Q-4", "Luis", "2026-10-26",
                         [{"tipo": "Camiseta", "talla": "M", "color": "azul", "cantidad": 0}]))

        gestor2 = GestorPedidos(ColeccionPedidos(), archivo)
        gestor2.coleccion.cargar_desde_lista(archivo.cargar())
        comprobar("persistencia: pedido e historial se recuperan", len(gestor2.listar_pedidos()) == 1
                  and len(gestor2.obtener_pedido("Q-1").historial) == 1)

        gestor.actualizar_fecha_hora_trabajo("2026-10-24 11:30")
        comprobar("estado escrito en minúsculas se acepta",
                  gestor.cambiar_estado("Q-1", "en preparacion").estado == "En preparacion")
        comprobar("cambio de estado queda en historial con fecha y hora",
                  gestor.historial_pedido("Q-1")[-1].fecha_hora == "2026-10-24 11:30"
                  and gestor.historial_pedido("Q-1")[-1].estado_anterior == "Recibido")
        comprobar("transición inválida conserva el estado",
                  _lanza(ErrorReglaNegocio, gestor.cambiar_estado, "Q-1", "Entregado")
                  and gestor.obtener_pedido("Q-1").estado == "En preparacion")
        comprobar("estado inexistente rechazado", _lanza(ErrorValidacion, gestor.cambiar_estado, "Q-1", "Enviado"))

        editado = gestor.actualizar_pedido("Q-1", cliente="Ana María", fecha_entrega="2026-10-28")
        comprobar("actualizar: cliente y fecha", editado.cliente == "Ana María" and editado.fecha_entrega == "2026-10-28")
        comprobar("actualizar: fecha inválida conserva datos",
                  _lanza(ErrorValidacion, gestor.actualizar_pedido, "Q-1", cliente="Zoe", fecha_entrega="2026-02-30")
                  and gestor.obtener_pedido("Q-1").cliente == "Ana María")
        comprobar("actualizar: lista de prendas vacía rechazada",
                  _lanza(ErrorValidacion, gestor.actualizar_pedido, "Q-1", prendas=[])
                  and len(gestor.obtener_pedido("Q-1").prendas) == 1)
        comprobar("actualizar: pedido inexistente", _lanza(ErrorReglaNegocio, gestor.actualizar_pedido, "Z-9", cliente="Ana"))

        gestor.cambiar_estado("Q-1", "Listo")
        comprobar("actualizar: Listo queda bloqueado", _lanza(ErrorReglaNegocio, gestor.actualizar_pedido, "Q-1", cliente="X Y"))
        gestor.cambiar_estado("Q-1", "Entregado")
        comprobar("actualizar: Entregado queda bloqueado", _lanza(ErrorReglaNegocio, gestor.actualizar_pedido, "Q-1", cliente="X Y"))
        comprobar("cancelar: Entregado rechazado", _lanza(ErrorReglaNegocio, gestor.cancelar_pedido, "Q-1"))

        gestor.registrar_pedido("Q-5", "Luis Gómez", "2026-10-25", [PRENDA])
        cancelado = gestor.cancelar_pedido("q-5")
        comprobar("cancelar: pedido se conserva con estado y historial",
                  cancelado.estado == "Cancelado" and gestor.historial_pedido("Q-5")[-1].estado_nuevo == "Cancelado"
                  and gestor.coleccion.buscar("Q-5") is not None)

        gestor.registrar_pedido("Q-6", "Marta Ríos", "2026-10-24", [PRENDA])
        gestor.registrar_pedido("Q-7", "Pedro Ruiz", "2026-10-30", [PRENDA])
        gestor.actualizar_fecha_hora_trabajo("2026-10-26 08:00")
        atrasados = [x.codigo for x in gestor.pedidos_atrasados()]
        proximos = [x.codigo for x in gestor.pedidos_proximos_a_vencer()]
        comprobar("atrasados: solo no finalizados con fecha pasada", atrasados == ["Q-6"])
        comprobar("próximos a vencer: dentro de 2 días", "Q-6" not in proximos and "Q-7" not in proximos)
        gestor.actualizar_fecha_hora_trabajo("2026-10-28 08:00")
        comprobar("próximos a vencer incluye vencimiento en 2 días",
                  [x.codigo for x in gestor.pedidos_proximos_a_vencer()] == ["Q-7"])

        comprobar("búsqueda parcial por código", [x.codigo for x in gestor.buscar_por_codigo_o_cliente("q-6")] == ["Q-6"])
        comprobar("búsqueda parcial por cliente sin importar mayúsculas",
                  [x.codigo for x in gestor.buscar_por_codigo_o_cliente("RUIZ")] == ["Q-7"])
        comprobar("búsqueda sin coincidencias", gestor.buscar_por_codigo_o_cliente("zzz") == [])
        comprobar("búsqueda vacía rechazada", _lanza(ErrorValidacion, gestor.buscar_por_codigo_o_cliente, "  "))
        comprobar("filtro por estado", [x.codigo for x in gestor.filtrar_por_estado("cancelado")] == ["Q-5"])

        comprobar("fecha de trabajo no puede retroceder antes del último movimiento",
                  _lanza(ErrorReglaNegocio, gestor.actualizar_fecha_hora_trabajo, "2020-01-01 00:00"))
        sin_fecha = GestorPedidos(ColeccionPedidos(), archivo)
        comprobar("sin fecha de trabajo no se puede registrar",
                  _lanza(ErrorReglaNegocio, sin_fecha.registrar_pedido, "Q-8", "Ana", "2026-10-30", [PRENDA]))
