# QPM Clothes — Tareas técnicas

## 1. Propósito

Este documento organiza y actualiza el documento anterior .md 04 las tareas técnicas necesarias para construir, integrar, probar y documentar QPM Clothes. Las tareas se agrupan por sprint para facilitar el seguimiento del trabajo y relacionar la planificación con el producto desarrollado.

El sistema es una aplicación de consola escrita en Python para registrar y gestionar pedidos de prendas de vestir. La información se conserva en archivos JSON y los reportes se exportan a CSV. La solución se limita a los conceptos trabajados en los cuatro laboratorios de Python.

## 2. Criterios para ejecutar las tareas

- Mantener la aplicación en terminal; no desarrollar una interfaz web o gráfica.
- No utilizar bases de datos, frameworks, paquetes externos ni servicios de Internet.
- Separar las responsabilidades en módulos y carpetas para facilitar la lectura y el mantenimiento.
- Validar los datos ingresados y manejar los errores previstos mediante las herramientas de Python estudiadas.
- Guardar y recuperar los pedidos mediante JSON.
- Generar archivos CSV para los reportes establecidos en el alcance.
- Actualizar la documentación cuando la implementación real cambie.
- Registrar en GitHub únicamente las tareas, reuniones, decisiones y avances que realmente se hayan realizado.

## 3. Sprint 1 — Planificación y diseño

**Objetivo del sprint:** dejar definido el alcance, la organización del trabajo y la estructura técnica antes de consolidar la implementación.

| Código | Tarea técnica | Resultado esperado |
|---|---|---|
| T1.1 | Definir el objetivo del producto y los límites del alcance. | Alcance acordado y documentado. |
| T1.2 | Organizar las historias de usuario según las necesidades de gestión de pedidos. | Historias identificadas y priorizadas. |
| T1.3 | Definir los sprints y sus objetivos. | Plan de trabajo organizado por etapas. |
| T1.4 | Desglosar las historias en tareas técnicas. | Lista de tareas con códigos y resultados esperados. |
| T1.5 | Establecer la Definition of Done. | Criterios comunes para considerar terminado un elemento. |
| T1.6 | Acordar la forma de trabajo del equipo y la distribución de responsabilidades. | Acuerdos de trabajo documentados. |
| T1.7 | Diseñar la estructura de carpetas y módulos Python. | Estructura técnica definida. |
| T1.8 | Preparar el repositorio y organizar la documentación inicial. | Repositorio con la organización inicial acordada. |

## 4. Sprint 2 — Construcción e integración

**Objetivo del sprint:** implementar las funciones principales de gestión de pedidos e integrar los módulos en una aplicación funcional de consola.

| Código | Tarea técnica | Resultado esperado |
|---|---|---|
| T2.1 | Crear el punto de entrada de la aplicación. | `main.py` inicia el flujo principal. |
| T2.2 | Definir la configuración y los valores fijos del sistema. | Configuración centralizada en el módulo correspondiente. |
| T2.3 | Implementar el inicio y cierre de sesión con credenciales definidas en el código. | Acceso básico antes de utilizar el menú. |
| T2.4 | Construir el menú principal y la lectura de opciones. | El usuario puede seleccionar las operaciones disponibles. |
| T2.5 | Definir los modelos de pedido, prenda y cambio de estado. | Datos representados mediante las clases o estructuras previstas. |
| T2.6 | Implementar el registro de pedidos y sus prendas. | Se pueden ingresar pedidos con los datos requeridos. |
| T2.7 | Implementar las validaciones de pedidos, prendas y fechas. | Los datos inválidos se detectan antes de procesarse. |
| T2.8 | Implementar la colección y gestión de pedidos. | Los pedidos se pueden almacenar y consultar durante la ejecución. |
| T2.9 | Implementar las reglas permitidas para los estados de los pedidos. | Los cambios de estado respetan las reglas definidas. |
| T2.10 | Implementar la consulta del listado y el detalle de un pedido. | Se muestran los pedidos y la información de un pedido seleccionado. |
| T2.11 | Implementar la búsqueda por código o cliente. | Se localizan pedidos mediante los criterios establecidos. |
| T2.12 | Implementar filtros por estado. | Se muestran pedidos que cumplen el filtro elegido. |
| T2.13 | Implementar la actualización y cancelación de pedidos. | Se modifican los datos permitidos y se gestionan las cancelaciones. |
| T2.14 | Implementar la persistencia JSON para guardar y recuperar pedidos. | Los datos pueden recuperarse en ejecuciones posteriores. |
| T2.15 | Integrar los módulos y manejar errores de entrada, archivos y operaciones. | El flujo principal utiliza los módulos y responde de forma controlada ante errores previstos. |

## 5. Sprint 3 — Cierre, validación y entrega

**Objetivo del sprint:** completar las consultas y reportes acordados, verificar el comportamiento del sistema y preparar los materiales de entrega.

| Código | Tarea técnica | Resultado esperado |
|---|---|---|
| T3.1 | Revisar el funcionamiento integrado de los módulos. | Los módulos colaboran desde el menú principal. |
| T3.2 | Corregir defectos detectados durante las pruebas. | Los errores reproducibles identificados quedan corregidos o documentados como pendientes. |
| T3.3 | Verificar la persistencia y el comportamiento ante un archivo JSON inválido. | Se documenta el resultado de las pruebas de guardado, recuperación y archivo dañado. |
| T3.4 | Ejecutar y registrar los casos del plan de pruebas. | Los ocho casos de prueba quedan documentados con sus resultados reales. |
| T3.5 | Actualizar el README y la documentación técnica. | Las instrucciones y los documentos coinciden con el comportamiento real del sistema. |
| T3.6 | Preparar el informe final y los materiales de demostración. | Entrega organizada para revisión y sustentación. |

## 6. Definition of Done aplicada a las tareas

Una tarea puede considerarse terminada cuando corresponda y se compruebe que:

- cumple el resultado esperado y los criterios de aceptación relacionados;
- el código es comprensible y utiliza los conceptos permitidos para el proyecto;
- se ha integrado con el resto de la aplicación cuando necesita integración;
- se han ejecutado las verificaciones pertinentes y sus resultados se registran de forma veraz;
- la documentación describe el comportamiento real;
- los cambios se han guardado en el repositorio según los acuerdos del equipo;
- los integrantes pueden explicar la finalidad y las decisiones principales de la tarea.

No se debe marcar una tarea como terminada únicamente porque estaba planificada. El estado final debe corresponder al trabajo realmente realizado.

## 7. Responsabilidades del equipo

- **Juan Quintero — Scrum Master:** facilita la organización del trabajo y el seguimiento de los acuerdos del equipo.
- **Marco — Product Owner:** orienta el producto hacia el objetivo y las necesidades definidas, y ayuda a priorizar el trabajo.
- **Parra — Developer:** participa en el desarrollo técnico, la integración y la verificación del sistema.


## 8. Seguimiento

Esta lista es la planificación técnica de referencia. Durante la ejecución, el equipo debe actualizar el estado de cada tarea y registrar los cambios de alcance o las adaptaciones que realmente se acuerden. Los códigos T1, T2 y T3 sirven para organizar este documento; no representan números de Issues o Pull Requests de GitHub.
