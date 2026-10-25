# Reglas de negocio — QPM Clothes

1. Cada pedido tiene un código único (se normaliza a mayúsculas).
2. Un pedido debe tener cliente, fecha de registro, fecha de entrega, estado, al menos una prenda e historial.
3. La fecha de entrega no puede ser anterior a la fecha de registro.
4. La cantidad de cada prenda debe ser un entero mayor que cero.
5. El estado inicial es `Recibido`.
6. Transiciones válidas: Recibido → En preparación o Cancelado; En preparación → Listo o Cancelado; Listo → Entregado o Cancelado.
7. Entregado y Cancelado son estados finales.
8. Solo se editan pedidos en estado Recibido o En preparación.
9. Cancelar exige confirmación y nunca borra el pedido.
10. Atrasado: pedido no finalizado con fecha de entrega anterior a la fecha de trabajo.
11. Próximo a vencer: pedido no finalizado con entrega entre hoy y los dos días siguientes.
12. La fecha y hora de trabajo se ingresa manualmente y no puede retroceder antes del último movimiento registrado.
13. El JSON dañado provoca un error controlado y nunca se sobrescribe.
14. Los reportes CSV son exportaciones, no fuente de datos del sistema.
