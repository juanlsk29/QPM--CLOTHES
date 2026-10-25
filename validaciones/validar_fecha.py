from excepciones import ErrorValidacion
from configuracion import DIAS_POR_MES


def es_bisiesto(anio):
    return anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)


def validar_fecha(fecha):
    if not isinstance(fecha, str):
        raise ErrorValidacion("La fecha debe ser texto con formato AAAA-MM-DD.")
    partes = fecha.strip().split("-")
    if len(partes) != 3 or any(not parte.isdigit() for parte in partes):
        raise ErrorValidacion("La fecha debe tener formato AAAA-MM-DD.")
    anio, mes, dia = (int(parte) for parte in partes)
    if anio < 1 or mes < 1 or mes > 12:
        raise ErrorValidacion("El año o el mes no son válidos.")
    dias_mes = list(DIAS_POR_MES)
    if es_bisiesto(anio):
        dias_mes[1] = 29
    if dia < 1 or dia > dias_mes[mes - 1]:
        raise ErrorValidacion("El día no existe en ese mes.")
    return f"{anio:04d}-{mes:02d}-{dia:02d}"


def validar_hora(hora):
    if not isinstance(hora, str):
        raise ErrorValidacion("La hora debe tener formato HH:MM.")
    partes = hora.strip().split(":")
    if len(partes) != 2 or any(not p.isdigit() for p in partes):
        raise ErrorValidacion("La hora debe tener formato HH:MM.")
    hh, mm = int(partes[0]), int(partes[1])
    if not (0 <= hh <= 23 and 0 <= mm <= 59):
        raise ErrorValidacion("La hora debe estar entre 00:00 y 23:59.")
    return f"{hh:02d}:{mm:02d}"


def validar_fecha_hora(fecha_hora):
    if not isinstance(fecha_hora, str) or " " not in fecha_hora.strip():
        raise ErrorValidacion("Use el formato AAAA-MM-DD HH:MM.")
    fecha, hora = fecha_hora.strip().split(" ", 1)
    return f"{validar_fecha(fecha)} {validar_hora(hora)}"


def fecha_a_tupla(fecha):
    fecha = validar_fecha(fecha)
    return tuple(int(parte) for parte in fecha.split("-"))


def fecha_hora_a_tupla(fecha_hora):
    fecha, hora = validar_fecha_hora(fecha_hora).split(" ")
    hh, mm = hora.split(":")
    return fecha_a_tupla(fecha) + (int(hh), int(mm))
