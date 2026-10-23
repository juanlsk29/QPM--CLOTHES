# QPM Clothes — Tareas técnicas

## 1. Objetivo

Descomponer el trabajo de las historias de usuario en tareas técnicas
pequeñas que faciliten la asignación, implementación, integración
y verificación de las funcionalidades.

Las tareas pueden modificarse durante el desarrollo cuando el equipo
identifique una dependencia o una necesidad técnica.

## 2. Estructura técnica propuesta

La estructura inicial puede organizarse de la siguiente manera:

    QPM-Clothes/
    ├── docs/
    │   ├── 01_product_goal_y_alcance.md
    │   ├── 02_historias_de_usuario.md
    │   ├── 03_planificacion_sprints.md
    │   ├── 04_tareas_tecnicas.md
    │   ├── 05_definition_of_done.md
    │   └── 06_acuerdos_del_equipo.md
    ├── datos/
    │   └── pedidos.json
    ├── reportes/
    ├── main.py
    ├── menus.py
    ├── pedido.py
    ├── servicio_pedidos.py
    ├── validaciones.py
    ├── persistencia.py
    ├── reportes.py
    └── README.md

Esta estructura es una propuesta de organización. Los archivos de
código y las carpetas se crearán durante la implementación. El equipo
podra ajustar los nombres si mantiene las responsabilidades claras.

## 3. Responsabilidades técnicas de los módulos

| Módulo o archivo | Responsabilidad |
|---|---|
| `main.py` | Iniciar la aplicación y conectar el flujo principal. |
| `menus.py` | Mostrar opciones y gestionar la navegación por consola. |
| `pedido.py` | Representar los datos de un pedido y sus prendas. |
| `servicio_pedidos.py` | Aplicar las reglas para registrar, consultar y actualizar pedidos. |
| `validaciones.py` | Comprobar textos, cantidades, códigos, fechas y entradas. |
| `persistencia.py` | Leer y guardar los pedidos en JSON. |
| `reportes.py` | Realizar búsquedas, filtros y exportaciones CSV, según la implementación. |
| `datos/pedidos.json` | Almacenar los pedidos entre ejecuciones. |
| `reportes/` | Guardar los archivos CSV generados. |
| `README.md` | Documentar requisitos, instalación, ejecución y uso. |

## 4. Convenciones para las tareas

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

## 5. Acuerdo de implementación

El equipo puede distribuir las tareas según sus conocimientos y
disponibilidad. Sin embargo, todos deben colaborar en la integración,
revisión, pruebas y documentación.