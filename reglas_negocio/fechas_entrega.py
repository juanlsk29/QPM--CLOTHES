from validaciones.validar_fecha import fecha_a_tupla
from configuracion import DIAS_VENCIMIENTO, DIAS_POR_MES


def fecha_ordinal(fecha_tupla):
    anio, mes, dia = fecha_tupla
    total = 365 * (anio - 1) + (anio - 1) // 4 - (anio - 1) // 100 + (anio - 1) // 400
    meses = list(DIAS_POR_MES)
    es_bisiesto = anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)
    if es_bisiesto:
        meses[1] = 29
    total += sum(meses[:mes - 1]) + dia
    return total


def dias_hasta_entrega(fecha_hoy, fecha_entrega):
    return fecha_ordinal(fecha_a_tupla(fecha_entrega)) - fecha_ordinal(fecha_a_tupla(fecha_hoy))


def esta_atrasado(pedido, fecha_hoy):
    return (not pedido.esta_finalizado()) and fecha_a_tupla(pedido.fecha_entrega) < fecha_a_tupla(fecha_hoy)


def esta_proximo_a_vencer(pedido, fecha_hoy, dias=DIAS_VENCIMIENTO):
    if pedido.esta_finalizado():
        return False
    return 0 <= dias_hasta_entrega(fecha_hoy, pedido.fecha_entrega) <= dias
