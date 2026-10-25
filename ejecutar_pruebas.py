from pruebas.comprobar import reiniciar, resultados
from pruebas import prueba_modelos, prueba_validaciones, prueba_reglas_negocio, prueba_persistencia, prueba_reportes


def main():
    reiniciar()
    print("=== PRUEBAS DE QPM CLOTHES ===")
    for modulo in (prueba_modelos, prueba_validaciones, prueba_reglas_negocio, prueba_persistencia, prueba_reportes):
        print(f"\n--- {modulo.__name__} ---")
        modulo.ejecutar()
    resultado = resultados()
    print("\n=== RESULTADO FINAL ===")
    print(f"Correctas: {resultado['ok']}")
    print(f"Fallidas: {resultado['fallo']}")
    print("Estado:", "APROBADO" if resultado["fallo"] == 0 else "REVISAR")


if __name__ == "__main__":
    main()
