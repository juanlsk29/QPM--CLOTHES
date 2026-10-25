from excepciones import ErrorAplicacion, ErrorReglaNegocio
from reportes.reportes_pedidos import ReportePendientes, ReporteEntregados, ReporteAtrasados


class OpcionesMenu:
    def __init__(self, gestor, exportador, mostrar, lectura):
        self.gestor = gestor
        self.exportador = exportador
        self.mostrar = mostrar
        self.lectura = lectura

    def ejecutar_opcion(self, opcion):
        acciones = {
            "1": self.registrar_pedido, "2": self.listar_pedidos, "3": self.consultar_pedido,
            "4": self.buscar_pedido, "5": self.filtrar_estado, "6": self.actualizar_pedido,
            "7": self.cambiar_estado, "8": self.cancelar_pedido, "9": self.ver_historial,
            "10": self.ver_atrasados, "11": self.ver_proximos, "12": self.exportar_pendientes,
            "13": self.exportar_entregados, "14": self.exportar_atrasados, "15": self.ver_resumen,
            "16": self.actualizar_fecha_hora
        }
        if opcion not in acciones:
            print("Opción no válida. Elija un número del menú.")
            return
        try:
            acciones[opcion]()
        except ErrorAplicacion as error:
            print(f"Operación no completada: {error}")
        except OSError as error:
            print(f"Error de archivo: {error}")

    def registrar_pedido(self):
        codigo = self.lectura.leer_codigo()
        cliente = self.lectura.leer_cliente()
        fecha = self.lectura.leer_fecha_entrega()
        prendas = self.lectura.leer_prendas()
        pedido = self.gestor.registrar_pedido(codigo, cliente, fecha, prendas)
        print(f"Pedido {pedido.codigo} registrado correctamente.")

    def listar_pedidos(self):
        self.mostrar.listar(self.gestor.listar_pedidos(), "No hay pedidos registrados.")

    def consultar_pedido(self):
        pedido = self.gestor.obtener_pedido(self.lectura.leer_codigo())
        self.mostrar.detalle(pedido)

    def buscar_pedido(self):
        texto = self.lectura.leer_texto_busqueda()
        self.mostrar.listar(self.gestor.buscar_por_codigo_o_cliente(texto), "No se encontraron resultados.")

    def filtrar_estado(self):
        estado = self.lectura.leer_estado()
        self.mostrar.listar(self.gestor.filtrar_por_estado(estado), "No se encontraron resultados.")

    def actualizar_pedido(self):
        codigo = self.lectura.leer_codigo()
        pedido = self.gestor.obtener_pedido(codigo)
        self.mostrar.detalle(pedido)
        print("\nDeje vacío un campo para conservar el valor actual.")
        cliente = self.lectura.leer_cliente_opcional()
        fecha = self.lectura.leer_fecha_entrega_opcional()
        prendas = None
        if self.lectura.leer_confirmacion("¿Reemplazar la lista de prendas?"):
            prendas = self.lectura.leer_prendas()
        pedido = self.gestor.actualizar_pedido(pedido.codigo, cliente, fecha, prendas)
        print(f"Pedido {pedido.codigo} actualizado.")

    def cambiar_estado(self):
        codigo = self.lectura.leer_codigo()
        estado = self.lectura.leer_estado()
        if estado == "Cancelado":
            self._confirmar_cancelacion(codigo)
        pedido = self.gestor.cambiar_estado(codigo, estado)
        print(f"Estado actualizado: {pedido.codigo} -> {pedido.estado}")

    def cancelar_pedido(self):
        codigo = self.lectura.leer_codigo()
        self._confirmar_cancelacion(codigo)
        pedido = self.gestor.cancelar_pedido(codigo)
        print(f"Pedido {pedido.codigo} cancelado.")

    def _confirmar_cancelacion(self, codigo):
        """Verifica que se pueda cancelar y pide confirmación antes de hacerlo."""
        pedido = self.gestor.obtener_pedido(codigo)
        if pedido.esta_finalizado():
            raise ErrorReglaNegocio(f"El pedido {pedido.codigo} está {pedido.estado} y no puede cancelarse.")
        if not self.lectura.leer_confirmacion(f"¿Confirma cancelar el pedido {pedido.codigo}?"):
            raise ErrorReglaNegocio("Cancelación no realizada; el estado no cambió.")

    def ver_historial(self):
        codigo = self.lectura.leer_codigo()
        pedido = self.gestor.obtener_pedido(codigo)
        self.mostrar.historial(pedido)

    def ver_atrasados(self):
        self.mostrar.alertas(self.gestor.pedidos_atrasados(), "Atrasado", "No hay pedidos atrasados.")

    def ver_proximos(self):
        self.mostrar.alertas(self.gestor.pedidos_proximos_a_vencer(), "Próximo a vencer",
                             "No hay pedidos próximos a vencer.")

    def _exportar(self, clase):
        hoy = self.gestor.fecha_hora_trabajo.split(" ")[0]
        reporte = clase(self.gestor.listar_pedidos(), hoy)
        ruta = self.exportador.exportar(reporte)
        print(f"Reporte exportado en: {ruta}")

    def exportar_pendientes(self): self._exportar(ReportePendientes)
    def exportar_entregados(self): self._exportar(ReporteEntregados)
    def exportar_atrasados(self): self._exportar(ReporteAtrasados)

    def ver_resumen(self):
        self.mostrar.resumen(self.gestor.listar_pedidos(), self.gestor.fecha_hora_trabajo.split(" ")[0])

    def actualizar_fecha_hora(self):
        fecha = self.lectura.leer_fecha_hora_trabajo()
        self.gestor.actualizar_fecha_hora_trabajo(fecha)
        print("Fecha y hora de trabajo actualizadas.")
