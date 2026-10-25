from configuracion import TIPOS_PRENDA, TALLAS
from excepciones import ErrorValidacion


def validar_tipo(tipo):
    tipo = str(tipo).strip()
    for permitido in TIPOS_PRENDA:
        if tipo.lower() == permitido.lower():
            return permitido
    raise ErrorValidacion("Tipo de prenda no válido. Opciones: " + ", ".join(TIPOS_PRENDA))


def validar_talla(talla):
    talla = str(talla).strip().upper()
    for permitida in TALLAS:
        if talla == permitida.upper():
            return permitida
    raise ErrorValidacion("Talla no válida. Opciones: " + ", ".join(TALLAS))


def validar_color(color):
    color = str(color).strip()
    if not color:
        raise ErrorValidacion("El color no puede estar vacío.")
    if len(color) > 40:
        raise ErrorValidacion("El color no puede superar 40 caracteres.")
    for caracter in color:
        if not (caracter.isalpha() or caracter in " -"):
            raise ErrorValidacion("El color solo puede contener letras (sin números ni símbolos).")
    return color.title()

def validar_cantidad(cantidad):
    mensaje = "La cantidad debe ser un número entero."
    if isinstance(cantidad, bool):
        raise ErrorValidacion(mensaje)
    if isinstance(cantidad, float):
        if cantidad != int(cantidad):
            raise ErrorValidacion(mensaje)
        cantidad = int(cantidad)
    try:
        cantidad = int(cantidad)
    except (TypeError, ValueError):
        raise ErrorValidacion(mensaje)
    if cantidad <= 0:
        raise ErrorValidacion("La cantidad debe ser mayor que cero.")
    return cantidad
