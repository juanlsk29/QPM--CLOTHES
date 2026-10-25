from excepciones import ErrorValidacion
from configuracion import ESTADOS
from validaciones.validar_fecha import validar_fecha, fecha_a_tupla


def validar_codigo(codigo):
    codigo = str(codigo).strip().upper()
    if not codigo:
        raise ErrorValidacion("El código del pedido es obligatorio.")
    if len(codigo) > 20 or not codigo.replace("-", "").isalnum():
        raise ErrorValidacion("El código solo puede contener letras, números y guiones.")
    return codigo


def validar_cliente(cliente):
    cliente = str(cliente).strip()
    if len(cliente) < 2:
        raise ErrorValidacion("El nombre del cliente debe tener al menos 2 caracteres.")
    if len(cliente) > 80:
        raise ErrorValidacion("El nombre del cliente no puede superar 80 caracteres.")
    return cliente


def validar_estado(estado):
    for permitido in ESTADOS:
        if str(estado).strip().lower() == permitido.lower():
            return permitido
    raise ErrorValidacion("Estado no válido. Opciones: " + ", ".join(ESTADOS))


def validar_fechas_pedido(fecha_registro, fecha_entrega):
    registro = validar_fecha(fecha_registro)
    entrega = validar_fecha(fecha_entrega)
    if fecha_a_tupla(entrega) < fecha_a_tupla(registro):
        raise ErrorValidacion("La fecha de entrega no puede ser anterior al registro.")
    return registro, entrega


def validar_texto_busqueda(texto):
    texto = str(texto).strip()
    if not texto:
        raise ErrorValidacion("Escriba un código o un nombre de cliente para buscar.")
    return texto
