# QPM Clothes — Cobertura de las historias de usuario (Sprint 2)

Gestión y seguimiento de pedidos de ropa (no inventario ni cotizaciones).

| Código | Historia | Compl. | Dónde se cumple |
|---|---|---|---|
| HU-001 | Registrar un pedido | 5 | Opción 1. Código único, cliente, fecha de registro y de entrega, estado inicial Recibido; rechaza duplicados, datos faltantes, fechas inválidas y pedidos sin prendas. |
| HU-002 | Registrar las prendas solicitadas | 3 | Una o más prendas con tipo, talla, color y cantidad entera positiva. |
| HU-003 | Consultar el listado de pedidos | 2 | Opción 2. Código, cliente, entrega y estado; mensaje si no hay pedidos. |
| HU-004 | Consultar el detalle de un pedido | 2 | Opción 3. Datos generales, prendas, fechas, estado e historial; mensaje si no existe. |
| HU-005 | Actualizar datos permitidos | 3 | Opción 6. Cliente, fecha de entrega y prendas en Recibido o En preparación; si falla, se conservan los datos anteriores. |
| HU-006 | Actualizar el estado | 5 | Opción 7. Transiciones validadas (acepta el estado en mayúsculas o minúsculas) y registro en historial. |
| HU-007 | Cancelar un pedido | 2 | Opciones 8 y 7. Pide confirmación, no borra el pedido, registra el evento. |
| HU-008 | Atrasados y próximos a vencer | 6 | Opciones 10 y 11. Listan código, cliente, fecha, estado y motivo. Ventana: 2 días. |
| HU-009 | Buscar y filtrar | 3 | Opciones 4 y 5. Búsqueda parcial por código o cliente sin distinguir mayúsculas; filtro por estado. El filtro por fecha (opcional) no se implementó. |
| HU-010 | Historial de estados | 3 | Opción 9. Estado anterior, nuevo y fecha/hora; incluye el estado inicial y se persiste. |
| HU-011 | Guardar y recuperar con JSON | 5 | Carga al iniciar, guarda tras cada cambio, archivo ausente = colección vacía, archivo dañado no se sobrescribe. |
| HU-012 | Validar datos y controlar errores | 8 | Validaciones en `validaciones/`, reintento de datos inválidos, opción de menú inválida, errores de archivo, cierre ordenado ante Ctrl+C / Ctrl+D. |
| HU-013 | Exportar reportes CSV | 5 | Opciones 12 a 14. Columnas código, cliente, fecha de registro, fecha de entrega y estado; sin pedidos genera solo encabezados. |
| HU-014 | Menú de consola | 3 | Menú principal con opción inválida y salida ordenada. |
| HU-015 | Resumen de pedidos | 2 | Opción 15. Conteo por estado (con ceros) y atrasados; indica cuando no hay pedidos. |

## Decisiones tomadas (pendientes de confirmar con el cliente)
- HU-005: también se bloquea la edición de pedidos en estado Listo.
- HU-008: ventana de próximos a vencer de 2 días, contando hoy.
- Tipos de prenda y tallas: listas en `configuracion.py`.
- Fecha y hora de trabajo ingresadas manualmente (los laboratorios no incluyen fecha del sistema).
