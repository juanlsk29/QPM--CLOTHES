from validaciones.validar_fecha import validar_fecha, validar_hora
from validaciones.validar_prenda import validar_cantidad, validar_talla, validar_tipo
from validaciones.validar_pedido import validar_codigo, validar_estado
from excepciones import ErrorValidacion
from pruebas.comprobar import comprobar


def _falla(funcion, valor):
    try:
        funcion(valor)
        return False
    except ErrorValidacion:
        return True


def ejecutar():
    comprobar("fecha válida", validar_fecha("2024-02-29") == "2024-02-29")
    comprobar("fecha inválida rechazada", _falla(validar_fecha, "2025-02-29"))
    comprobar("hora válida", validar_hora("09:05") == "09:05")
    comprobar("cantidad positiva", validar_cantidad("3") == 3)
    comprobar("cantidad cero rechazada", _falla(validar_cantidad, "0"))
    comprobar("código normalizado", validar_codigo(" q-12 ") == "Q-12")
    comprobar("código vacío rechazado", _falla(validar_codigo, "  "))
    comprobar("cantidad negativa rechazada", _falla(validar_cantidad, "-2"))
    comprobar("cantidad no numérica rechazada", _falla(validar_cantidad, "dos"))
    comprobar("cantidad decimal rechazada", _falla(validar_cantidad, "2.5") and _falla(validar_cantidad, 2.7))
    comprobar("hora inválida rechazada", _falla(validar_hora, "25:00"))
    comprobar("estado inválido rechazado", _falla(validar_estado, "Enviado"))
    comprobar("talla y tipo se normalizan", validar_talla("xl") == "XL" and validar_tipo("camiseta") == "Camiseta")
    comprobar("talla inválida rechazada", _falla(validar_talla, "Z"))
