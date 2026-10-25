class ErrorAplicacion(Exception):
    """Excepción base para errores controlados de QPM Clothes."""


class ErrorValidacion(ErrorAplicacion):
    """Un dato ingresado no cumple las reglas de validación."""


class ErrorReglaNegocio(ErrorAplicacion):
    """Una operación no está permitida por las reglas del sistema."""


class ErrorArchivoDatos(ErrorAplicacion):
    """No se pudieron leer o escribir los archivos de datos."""
