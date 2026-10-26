# QPM Clothes — Plan de pruebas

## 1. Objetivo

Verificar el funcionamiento de QPM Clothes mediante pruebas manuales de ejecución, registro y consulta de pedidos, actualización de estados, validaciones, persistencia JSON y exportación CSV.

## 2. Entorno de pruebas

- Aplicación: QPM Clothes.
- Lenguaje: Python.
- Tipo de aplicación: consola.
- Persistencia: archivos JSON.
- Reportes: archivos CSV.
- Fecha de ejecución: [fecha real].
- Responsable: [integrante].

## 3. Casos de prueba

| ID | Funcionalidad | Datos de entrada | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| PT-01 | Inicio y menú | Ejecución de `main.py` | El programa inicia y permite salir correctamente. | [Completar] | [Completado] |
| PT-02 | Registro de pedido | Cliente Carlos Prueba y datos válidos de una prenda | El pedido se registra y recibe un código. | [Completar] | [Completado] |
| PT-03 | Consulta y búsqueda | Código del pedido registrado | Se encuentra el pedido y se muestran sus datos. | [Completar] | [Completado] |
| PT-04 | Cambio de estado | Código y estado permitido | El cambio válido se guarda y se rechazan transiciones prohibidas. | [Completar] | [Completado] |
| PT-05 | Validaciones | Cantidad `abc`, fecha inválida y opción `99` | El sistema controla los errores y continúa funcionando. | [Completar] | [Completado] |
| PT-06 | Persistencia JSON | Pedido guardado antes de reiniciar | El pedido se recupera con sus datos originales. | [Completar] | [Completado] |
| PT-07 | JSON dañado | Copia de seguridad y archivo temporal inválido | Se detecta el error y no se sobrescriben automáticamente los datos recuperables. | [Completar] | [Completado] |
| PT-08 | Exportación CSV | Pedidos registrados y solicitud de exportación | Se genera un CSV legible con los datos correspondientes. | [Completar] | [Completado] |


## 4. Conclusión

[Describir los resultados reales de las pruebas, las funcionalidades verificadas, los errores encontrados y las correcciones que aún estén pendientes.]

## 6. Evidencias

#PT-01 
 Verificar la ejecución inicial

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 3
Código del pedido: P001

Pedido: P001
Cliente: Eduard
Registro: 2026-10-25
Entrega: 2026-10-25
Estado: Recibido
Prendas:
  - Camiseta | Talla M | Azul | Cantidad: 20

Historial del pedido P001:
  - 2026-10-25 03:37: (inicio) -> Recibido

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 4
Código o nombre del cliente (puede ser una parte): Edua

CÓDIGO | CLIENTE | ENTREGA | ESTADO
----------------------------------------------------------------------
P001 | Eduard | 2026-10-25 | Recibido

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 5
Estados: Recibido, En preparacion, Listo, Entregado, Cancelado
Estado: Recibido

CÓDIGO | CLIENTE | ENTREGA | ESTADO
----------------------------------------------------------------------
P001 | Eduard | 2026-10-25 | Recibido

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 6
Código del pedido: P001

Pedido: P001
Cliente: Eduard
Registro: 2026-10-25
Entrega: 2026-10-25
Estado: Recibido
Prendas:
  - Camiseta | Talla M | Azul | Cantidad: 20

Historial del pedido P001:
  - 2026-10-25 03:37: (inicio) -> Recibido

Deje vacío un campo para conservar el valor actual.
Nuevo cliente (vacío para conservar):
Nueva fecha de entrega AAAA-MM-DD (vacío para conservar): 
¿Reemplazar la lista de prendas? (s/n): n
Pedido P001 actualizado.

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 7
Código del pedido: P001
Estados: Recibido, En preparacion, Listo, Entregado, Cancelado
Estado: En preparacion
Estado actualizado: P001 -> En preparacion

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 9
Código del pedido: P001

Historial del pedido P001:
  - 2026-10-25 03:37: (inicio) -> Recibido
  - 2026-10-25 03:37: Recibido -> En preparacion

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 10
No hay pedidos atrasados.

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 11

CÓDIGO | CLIENTE | ENTREGA | ESTADO | MOTIVO
----------------------------------------------------------------------
P001 | Eduard | 2026-10-25 | En preparacion | Próximo a vencer

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 12
Reporte exportado en: C:\Users\PC\Desktop\QPM--CLOTHES\datos\reportes_csv\pedidos_pendientes.csv

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 15

RESUMEN DE PEDIDOS
Total de pedidos: 1
Clientes distintos: 1
Pedidos atrasados: 0
Pedidos por estado:
  Recibido: 0
  En preparacion: 1
  Listo: 0
  Entregado: 0
  Cancelado: 0

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 0
Gracias por utilizar QPM Clothes.


--------------------------------------------------------------------------------
# PT-02
 Comprobar la operación principal

PS C:\Users\PC\Desktop\QPM--CLOTHES> python main.py

Fecha y hora de trabajo (no se toma automáticamente del sistema).
Ingrese AAAA-MM-DD HH:MM: 2026-10-25 4:07

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 1
Código del pedido: P002
Nombre del cliente: Juan prueba
Fecha de entrega (AAAA-MM-DD): 2026-11-10 
Tipos: Camiseta, Pantalon, Buzo, Chaqueta, Vestido, Falda, Short, Otro
Tipo de prenda: Camiseta
Tallas: XS, S, M, L, XL, XXL, Unica
Talla: M
Color: Azul
Cantidad: 2
¿Agregar otra prenda? (s/n): n
Pedido P002 registrado correctamente.

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 3
Código del pedido: P002

Pedido: P002
Cliente: Juan prueba
Registro: 2026-10-25
Entrega: 2026-11-10
Estado: Recibido
Prendas:
  - Camiseta | Talla M | Azul | Cantidad: 2

Historial del pedido P002:
  - 2026-10-25 04:07: (inicio) -> Recibido

-------------------------------------------------------------------------------------------------
PT-03
 Verificar búsquedas y consultas

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 3
Código del pedido: P002

Pedido: P002
Cliente: Juan prueba
Registro: 2026-10-25
Entrega: 2026-11-10
Estado: Recibido
Prendas:
  - Camiseta | Talla M | Azul | Cantidad: 2

Historial del pedido P002:
  - 2026-10-25 04:07: (inicio) -> Recibido



----------------------------------------------------------------------------------------------------------------------------------------

PT-04
 Comprobar los cambios permitidos

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 7
Código del pedido: P002
Estados: Recibido, En preparacion, Listo, Entregado, Cancelado
Estado: En preparacion
Estado actualizado: P002 -> En preparacion

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 3
Código del pedido: P002

Pedido: P002
Cliente: Juan prueba
Registro: 2026-10-25
Entrega: 2026-11-10
Estado: En preparacion
Prendas:
  - Camiseta | Talla M | Azul | Cantidad: 2

Historial del pedido P002:
  - 2026-10-25 04:07: (inicio) -> Recibido
  - 2026-10-25 04:07: Recibido -> En preparacion

---------------------------------------------------------------------------------

PT-05
 Verificar las validaciones y los errores de entrada


========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 1
Código del pedido: P003
Nombre del cliente: Marco
Fecha de entrega (AAAA-MM-DD): 10-11-2026
Error: El día no existe en ese mes.
Fecha de entrega (AAAA-MM-DD): 10/11/2026
Error: La fecha debe tener formato AAAA-MM-DD.
Fecha de entrega (AAAA-MM-DD): 2026/11/10
Error: La fecha debe tener formato AAAA-MM-DD.
Fecha de entrega (AAAA-MM-DD): 2026-11-10
Tipos: Camiseta, Pantalon, Buzo, Chaqueta, Vestido, Falda, Short, Otro
Tipo de prenda: Pantalon
Tallas: XS, S, M, L, XL, XXL, Unica
Talla: S
Color: Rojo
Cantidad: abc
Error: La cantidad debe ser un número entero.
Cantidad: 5  
¿Agregar otra prenda? (s/n): n
Pedido P003 registrado correctamente.

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 99
Opción no válida. Elija un número del menú.

------------------------------------------------------------------------------------------------------------------

PT-06
 Comprobar que los datos no se pierdan al cerrar

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 1
Código del pedido: P004
Nombre del cliente: Persistencia
Fecha de entrega (AAAA-MM-DD): 2026-10-26
Tipos: Camiseta, Pantalon, Buzo, Chaqueta, Vestido, Falda, Short, Otro
Tipo de prenda: Falda
Tallas: XS, S, M, L, XL, XXL, Unica
Talla: S
Color: Rosa
Cantidad: 4
¿Agregar otra prenda? (s/n): n
Pedido P004 registrado correctamente.

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
10. Consultar pedidos atrasados
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 0
Gracias por utilizar QPM Clothes.

PS C:\Users\PC\Desktop\QPM--CLOTHES> python main.py
========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 4
Código o nombre del cliente (puede ser una parte): P004

CÓDIGO | CLIENTE | ENTREGA | ESTADO
----------------------------------------------------------------------
P004 | Persistencia | 2026-10-26 | Recibido

------------------------------------------------------------------------------------------------------------------------------------------------------------

PT-07
 Comprobar la protección de los datos

 --// El archivo JSON se elimino todo y se intento ejecutar //--
PS C:\Users\PC\Desktop\QPM--CLOTHES> python main.py
No fue posible cargar los datos: El archivo JSON está dañado o no se puede leer: Expecting value: line 1 column 14 (char 13)
El archivo no fue modificado. Corrija o restaure pedidos.json e inicie de nuevo.

 --// Tras regresar el archivo a su estado original y volver a ejecutar el resultado fue una persistencia exitosa //--
Fecha y hora de trabajo (no se toma automáticamente del sistema).
Ingrese AAAA-MM-DD HH:MM: 2026-10-25 4:16

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 4
Código o nombre del cliente (puede ser una parte): P004

CÓDIGO | CLIENTE | ENTREGA | ESTADO
----------------------------------------------------------------------
P004 | Persistencia | 2026-10-26 | Recibido

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PT-08
 Comprobar la generación del reporte
========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 2

CÓDIGO | CLIENTE | ENTREGA | ESTADO
----------------------------------------------------------------------
P001 | Eduard | 2026-10-25 | En preparacion
P002 | Juan prueba | 2026-11-10 | En preparacion
P003 | Marco | 2026-11-10 | Recibido
P004 | Persistencia | 2026-10-26 | Recibido

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 16

Fecha y hora de trabajo (no se toma automáticamente del sistema).
Ingrese AAAA-MM-DD HH:MM: 2026-11-25 4:22
Fecha y hora de trabajo actualizadas.

========== QPM CLOTHES ==========
Gestión y seguimiento de pedidos de ropa
1. Registrar pedido
2. Listar pedidos
3. Consultar detalle de pedido
4. Buscar pedidos por código o cliente
5. Filtrar pedidos por estado
6. Actualizar pedido
7. Cambiar estado
8. Cancelar pedido
9. Ver historial de estados
10. Consultar pedidos atrasados
11. Consultar próximos a vencer
12. Exportar pedidos pendientes a CSV
13. Exportar pedidos entregados a CSV
14. Exportar pedidos atrasados a CSV
15. Ver resumen
16. Actualizar fecha y hora de trabajo
0. Salir
Seleccione una opción: 14
Reporte exportado en: C:\Users\PC\Desktop\QPM--CLOTHES\datos\reportes_csv\pedidos_atrasados.csv

 --// resultado del csv //--

codigo,cliente,fecha_registro,fecha_entrega,estado
P001,Eduard,2026-10-25,2026-10-25,En preparacion
P002,Juan prueba,2026-10-25,2026-11-10,En preparacion
P003,Marco,2026-10-25,2026-11-10,Recibido
P004,Persistencia,2026-10-25,2026-10-26,Recibido

