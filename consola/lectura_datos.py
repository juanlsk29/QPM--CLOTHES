from validaciones.validar_fecha import validar_fecha, validar_fecha_hora
from validaciones.validar_prenda import validar_tipo, validar_talla, validar_color, validar_cantidad
from validaciones.validar_pedido import validar_codigo, validar_cliente, validar_estado, validar_texto_busqueda
from excepciones import ErrorAplicacion
from configuracion import TIPOS_PRENDA, TALLAS, ESTADOS


class LecturaDatos:
    def _leer_validado(self, mensaje, funcion):
        while True:
            valor = input(mensaje).strip()
            try:
                return funcion(valor)
            except ErrorAplicacion as error:
                print(f"Error: {error}")

    def _leer_opcional(self, mensaje, funcion):
        """Una respuesta vacía conserva el valor actual y devuelve None."""
        while True:
            valor = input(mensaje).strip()
            if not valor:
                return None
            try:
                return funcion(valor)
            except ErrorAplicacion as error:
                print(f"Error: {error}")

    def leer_fecha_hora_trabajo(self):
        print("\nFecha y hora de trabajo (no se toma automáticamente del sistema).")
        return self._leer_validado("Ingrese AAAA-MM-DD HH:MM: ", validar_fecha_hora)

    def leer_codigo(self):
        return self._leer_validado("Código del pedido: ", validar_codigo)

    def leer_cliente(self):
        return self._leer_validado("Nombre del cliente: ", validar_cliente)

    def leer_cliente_opcional(self):
        return self._leer_opcional("Nuevo cliente (vacío para conservar): ", validar_cliente)

    def leer_fecha_entrega(self):
        return self._leer_validado("Fecha de entrega (AAAA-MM-DD): ", validar_fecha)

    def leer_fecha_entrega_opcional(self):
        return self._leer_opcional("Nueva fecha de entrega AAAA-MM-DD (vacío para conservar): ", validar_fecha)

    def leer_texto_busqueda(self):
        return self._leer_validado("Código o nombre del cliente (puede ser una parte): ", validar_texto_busqueda)

    def leer_estado(self):
        print("Estados:", ", ".join(ESTADOS))
        return self._leer_validado("Estado: ", validar_estado)

    def leer_confirmacion(self, mensaje):
        while True:
            respuesta = input(f"{mensaje} (s/n): ").strip().lower()
            if respuesta in ("s", "n"):
                return respuesta == "s"
            print("Error: responda s o n.")

    def leer_prendas(self):
        prendas = []
        while True:
            print("Tipos:", ", ".join(TIPOS_PRENDA))
            tipo = self._leer_validado("Tipo de prenda: ", validar_tipo)
            print("Tallas:", ", ".join(TALLAS))
            talla = self._leer_validado("Talla: ", validar_talla)
            color = self._leer_validado("Color: ", validar_color)
            cantidad = self._leer_validado("Cantidad: ", validar_cantidad)
            prendas.append({"tipo": tipo, "talla": talla, "color": color, "cantidad": cantidad})
            if not self.leer_confirmacion("¿Agregar otra prenda?"):
                return prendas
