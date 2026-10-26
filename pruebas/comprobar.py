_RESULTADOS = {"ok": 0, "fallo": 0}


def reiniciar():
    _RESULTADOS["ok"] = 0
    _RESULTADOS["fallo"] = 0


def comprobar(descripcion, condicion):
    if condicion:
        _RESULTADOS["ok"] += 1
        print(f"OK: {descripcion}")
    else:
        _RESULTADOS["fallo"] += 1
        print(f"FALLO: {descripcion}")


def resultados():
    return dict(_RESULTADOS)
