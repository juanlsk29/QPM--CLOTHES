class MenuPrincipal:
    def __init__(self, opciones):
        self.opciones = opciones

    def ejecutar(self):
        while True:
            print("\n========== QPM CLOTHES ==========")
            print("Gestión y seguimiento de pedidos de ropa")
            print("1. Registrar pedido")
            print("2. Listar pedidos")
            print("3. Consultar detalle de pedido")
            print("4. Buscar pedidos por código o cliente")
            print("5. Filtrar pedidos por estado")
            print("6. Actualizar pedido")
            print("7. Cambiar estado")
            print("8. Cancelar pedido")
            print("9. Ver historial de estados")
            print("10. Consultar pedidos atrasados")
            print("11. Consultar próximos a vencer")
            print("12. Exportar pedidos pendientes a CSV")
            print("13. Exportar pedidos entregados a CSV")
            print("14. Exportar pedidos atrasados a CSV")
            print("15. Ver resumen")
            print("16. Actualizar fecha y hora de trabajo")
            print("0. Salir")
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "0":
                print("Gracias por utilizar QPM Clothes.")
                break
            self.opciones.ejecutar_opcion(opcion)
