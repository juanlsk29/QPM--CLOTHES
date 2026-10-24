# QPM Clothes — Tareas técnicas

## 1. Objetivo

Descomponer el trabajo de las historias de usuario en tareas técnicas
pequeñas que faciliten la asignación, implementación, integración
y verificación de las funcionalidades.

Las tareas pueden modificarse durante el desarrollo cuando el equipo
identifique una dependencia o una necesidad técnica.

El detalle de cada carpeta y de cada archivo se encuentra en
`07_estructura_del_proyecto.md`.

## 2. Estructura técnica acordada

    QPM-Clothes/
    ├── main.py
    ├── ejecutar_pruebas.py
    ├── configuracion.py
    ├── excepciones.py
    ├── README.md
    ├── docs/
    ├── datos/
    │   ├── pedidos.json
    │   ├── bitacora.txt
    │   └── reportes_csv/
    ├── consola/
    │   ├── menu_principal.py
    │   ├── opciones_menu.py
    │   ├── lectura_datos.py
    │   └── mostrar_pedidos.py
    ├── modelos/
    │   ├── pedido.py
    │   ├── prenda.py
    │   └── cambio_estado.py
    ├── reglas_negocio/
    │   ├── estados_pedido.py
    │   ├── fechas_entrega.py
    │   └── gestor_pedidos.py
    ├── colecciones/
    │   └── coleccion_pedidos.py
    ├── validaciones/
    │   ├── validar_pedido.py
    │   ├── validar_prenda.py
    │   └── validar_fecha.py
    ├── persistencia/
    │   ├── archivo_json.py
    │   └── bitacora_texto.py
    ├── reportes/
    │   ├── reportes_pedidos.py
    │   ├── exportar_csv.py
    │   └── resumen_pedidos.py
    └── pruebas/
        ├── comprobar.py
        ├── prueba_modelos.py
        ├── prueba_validaciones.py
        ├── prueba_reglas_negocio.py
        ├── prueba_persistencia.py
        └── prueba_reportes.py

Las carpetas `consola`, `modelos`, `reglas_negocio`, `colecciones`,
`validaciones`, `persistencia` y `reportes` corresponden a las siete
separaciones de responsabilidades que exige la actividad. Las carpetas
`datos` y `pruebas` guardan la información de la aplicación y las
comprobaciones.

Los archivos `main.py` y `ejecutar_pruebas.py` están en la raíz para
que las importaciones entre carpetas funcionen al ejecutar los
programas desde esa ubicación.

El equipo podrá ajustar los nombres si mantiene las responsabilidades
claras y actualiza `07_estructura_del_proyecto.md`.

## 3. Responsabilidades técnicas de las carpetas

| Carpeta o archivo | Responsabilidad |
|---|---|
| `main.py` | Crear los objetos de la aplicación, pedir la fecha y hora de trabajo e iniciar el menú. |
| `configuracion.py` | Constantes: estados, tipos de prenda, tallas, días de vencimiento, días por mes y rutas. |
| `excepciones.py` | Excepciones propias de la aplicación. |
| `consola/` | Menú, lectura de datos con reintentos y presentación de resultados. Es la única carpeta que usa `input()` y `print()`. |
| `modelos/` | Clases `Pedido`, `Prenda` y `CambioEstado`. |
| `reglas_negocio/` | Transiciones de estado, reglas de fechas y operaciones sobre pedidos. |
| `colecciones/` | Colección de pedidos: agregar, buscar, filtrar y exportar sus datos. |
| `validaciones/` | Comprobación de textos, códigos, cantidades, estados, fechas y horas. |
| `persistencia/` | Lectura y escritura del JSON y de la bitácora de texto. |
| `reportes/` | Reportes CSV y resumen de pedidos. |
| `datos/` | `pedidos.json`, `bitacora.txt` y la carpeta `reportes_csv/` con los CSV exportados. |
| `pruebas/` | Comprobaciones por capa de la aplicación. |
| `README.md` | Requisitos, ejecución y uso. |

## 4. Tareas técnicas por carpeta

Los identificadores y los responsables iniciales corresponden a los
definidos en el documento de Planificación Scrum.

| Tarea | Archivos principales | Historias | Responsable inicial |
|---|---|---|---|
| T2.1 Crear carpetas y módulos Python | Toda la estructura | — | Parra + Juan |
| T2.2 Menú principal y navegación | `main.py`, `consola/menu_principal.py`, `consola/opciones_menu.py` | HU-014 | Juan + Parra |
| T2.3 Estructura del pedido y sus prendas | `modelos/` | HU-001, HU-002 | Parra + equipo |
| T2.4 Registro de pedidos | `reglas_negocio/gestor_pedidos.py`, `validaciones/` | HU-001, HU-002 | Equipo |
| T2.5 Consulta de lista y detalle | `colecciones/coleccion_pedidos.py`, `consola/mostrar_pedidos.py` | HU-003, HU-004 | Equipo |
| T2.6 Actualización de datos permitidos | `reglas_negocio/gestor_pedidos.py`, `reglas_negocio/estados_pedido.py` | HU-005 | Equipo |
| T2.7 Flujo de estados y cancelación | `reglas_negocio/estados_pedido.py`, `reglas_negocio/gestor_pedidos.py`, `modelos/cambio_estado.py` | HU-006, HU-007 | Equipo |
| T2.8 Fechas, atrasados y próximos a vencer | `reglas_negocio/fechas_entrega.py`, `validaciones/validar_fecha.py` | HU-008 | Marco + equipo |
| T2.9 Lectura y escritura JSON | `persistencia/archivo_json.py`, `colecciones/coleccion_pedidos.py` | HU-011 | Parra + equipo |
| T2.10 Validaciones y manejo de errores | `validaciones/`, `excepciones.py`, `consola/lectura_datos.py` | HU-012 | Todos |
| T2.11 Integración y pruebas por flujo | `main.py`, `pruebas/` | Todas | Todos |
| T2.12 Datos de prueba y README inicial | `datos/pedidos.json`, `README.md` | — | Juan + equipo |
| T3.2 Búsqueda y filtros | `colecciones/coleccion_pedidos.py` | HU-009 | Equipo |
| T3.3 Historial de estados | `modelos/cambio_estado.py`, `modelos/pedido.py`, `consola/mostrar_pedidos.py` | HU-010 | Equipo |
| T3.4 Exportación CSV | `reportes/reportes_pedidos.py`, `reportes/exportar_csv.py` | HU-013 | Parra + equipo |
| T3.5 Resumen de pedidos | `reportes/resumen_pedidos.py` | HU-015 | Equipo |
| T3.6 y T3.7 Pruebas de aceptación y de persistencia | `pruebas/` | P1 y HU-011 | Todos |
| T3.8 README final | `README.md` | — | Juan + equipo |

Las tareas asignadas al "Equipo" no tienen todavía una persona
encargada. De acuerdo con los acuerdos del equipo, cada tarea debe
tener una persona que impulse su avance; esa asignación debe
definirse al iniciar el Sprint 2.

## 5. Convenciones para las tareas

Cada tarea debe contar con:

- Identificador.
- Descripción clara.
- Historia de usuario relacionada, cuando corresponda.
- Persona encargada de impulsarla.
- Estado de avance.
- Resultado verificable.

Los estados de seguimiento recomendados son:

- Por hacer.
- En progreso.
- En revisión o pruebas.
- Terminado.

Una tarea no se considera terminada solamente porque se escribió
el código: debe integrarse y verificarse.

## 6. Acuerdo de implementación

El equipo puede distribuir las tareas según sus conocimientos y
disponibilidad. Sin embargo, todos deben colaborar en la integración,
revisión, pruebas y documentación.

Todo el código debe construirse únicamente con los conceptos y las
herramientas vistas en los cuatro laboratorios de Python. Si una
necesidad no puede resolverse con ellos, se debe consultar al
instructor antes de utilizar otra herramienta.
