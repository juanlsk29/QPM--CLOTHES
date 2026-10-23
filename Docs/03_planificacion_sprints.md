# QPM Clothes — Planificación de sprints

## 1. Objetivo

Organizar el trabajo del equipo para construir QPM Clothes por etapas,
priorizando una versión funcional de la aplicación y dejando tiempo
para realizar pruebas, corregir errores y preparar la entrega.

## 2. Calendario de trabajo

| Sprint | Fecha | Objetivo principal |
|---|---|---|
| Sprint 1 | 23 de octubre de 2026 | Planificación y preparación |
| Sprint 2 | 24 de octubre de 2026 | Construcción de la versión mínima funcional |
| Sprint 3 | 25 de octubre de 2026 | Pruebas, estabilización y entrega |

Las duraciones son una organización propuesta para las jornadas
disponibles del equipo

## 3. Sprint 1 — Planificación y preparación

**Fecha:** 23 de octubre de 2026.

### Sprint Goal

Acordar un alcance realizable, un backlog comprensible y un plan técnico
compartido antes de comenzar la construcción principal.

### Actividades

1. Revisar el problema que busca resolver QPM Clothes.
2. Confirmar el objetivo y el alcance del producto.
3. Revisar las 15 historias de usuario.
4. Confirmar las prioridades, estimaciones y dependencias.
5. Definir las reglas de negocio para pedidos, prendas, fechas y estados.
6. Acordar la estructura inicial de archivos Python.
7. Definir cómo se guardarán y recuperarán los datos JSON.
8. Acordar el formato de los reportes CSV.
9. Definir la estrategia de validación y pruebas.
10. Acordar la Definition of Done.
11. Actualizar los documentos y preparar el repositorio.

### Entregables

- Objetivo y alcance del producto.
- Historias de usuario revisadas.
- Product Backlog priorizado.
- Reglas de negocio documentadas.
- Estructura técnica propuesta.
- Definition of Done.
- Plan de pruebas.
- Documentación de planificación actualizada.

## 4. Sprint 2 — Versión mínima funcional

**Fecha:** 24 de octubre de 2026.

### Sprint Goal

Obtener una aplicación de consola ejecutable que permita registrar,
consultar y actualizar pedidos, conservar los datos en JSON y aplicar
las validaciones esenciales.

### Historias objetivo

Completar conseguir todos los requisitos de las historias de usuario.



### Actividades

1. Crear los módulos y archivos Python.
2. Construir el menú principal.
3. Definir la representación de pedidos y prendas.
4. Implementar el registro de pedidos.
5. Implementar la consulta de listados y detalles.
6. Implementar las actualizaciones permitidas.
7. Implementar el cambio de estados.
8. Implementar la identificación de pedidos atrasados y próximos a vencer.
9. Implementar la lectura y escritura de archivos JSON.
10. Validar entradas y controlar errores.
11. Integrar los módulos.
12. Probar los flujos principales.
13. Registrar defectos y pendientes.

### Entregables

- Aplicación ejecutable desde el archivo principal acordado.
- Registro y consulta de pedidos.
- Registro de prendas asociadas.
- Actualización de datos y estados.
- Persistencia JSON funcional.
- Validaciones esenciales.
- Identificación de pedidos atrasados y próximos a vencer.

## 5. Sprint 3 — Estabilización y entrega

**Fecha:** 25 de octubre de 2026.

### Sprint Goal

Entregar una versión estable, comprobada y fácil de ejecutar,
acompañada por documentación y por los elementos exigidos en la guía.
También se corregirán los defectos encontrados y se volverán a probar
las historias esenciales del Sprint 2.

### Actividades

1. Revisar y priorizar los errores pendientes.
2. Corregir los defectos que afecten el funcionamiento principal.
3. Completar la búsqueda y los filtros.
4. Completar el historial de cambios de estado.
5. Implementar y comprobar la exportación CSV.
6. Ejecutar las pruebas de aceptación.
7. Probar la persistencia y el manejo de errores de archivos.
8. Completar y verificar el README principal.
9. Preparar el informe PDF y las evidencias.
10. Revisar el repositorio.
11. Preparar una demostración del flujo principal.

### Entregables

- Código fuente integrado y ejecutable.
- Funcionalidades completadas según las prioridades acordadas.
- Pruebas de aceptación realizadas.
- README con instrucciones verificadas.
- Reporte CSV, si se implementó esa funcionalidad.
- Informe PDF y evidencias, si los solicita la guía.
- Repositorio listo para revisión y demostración.

## 6. Seguimiento entre sprints

Al inicio de cada jornada, el equipo revisará:

- Qué se terminó.
- Qué trabajo continúa pendiente.
- Qué tarea se realizará a continuación.
- Qué bloqueos requieren ayuda.
- Qué debe probarse antes de integrar.

Al final de cada sprint, se revisará el incremento 

## 7. Criterio para ajustar el plan

Si el tiempo disponible no es suficiente, se priorizarán las historias
P1 y los requisitos obligatorios del instructor.

No se deben marcar como terminadas las funcionalidades que no hayan
sido implementadas y comprobadas. Las historias pendientes deben quedar
identificadas para que el estado real del producto sea claro.