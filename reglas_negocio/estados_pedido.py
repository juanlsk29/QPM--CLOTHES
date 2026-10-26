from configuracion import ESTADOS_FINALES
from excepciones import ErrorReglaNegocio

TRANSICIONES = {
    "Recibido": ("En preparacion", "Cancelado"),
    "En preparacion": ("Listo", "Cancelado"),
    "Listo": ("Entregado", "Cancelado"),
    "Entregado": (),
    "Cancelado": ()
}


def validar_transicion(estado_actual, estado_nuevo):
    permitidos = TRANSICIONES.get(estado_actual, ())
    if estado_nuevo not in permitidos:
        raise ErrorReglaNegocio(f"No se permite cambiar de '{estado_actual}' a '{estado_nuevo}'.")
    return True


def permite_edicion(estado):
    return estado in ("Recibido", "En preparacion")
