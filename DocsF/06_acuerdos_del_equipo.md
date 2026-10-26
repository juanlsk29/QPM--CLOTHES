# QPM Clothes — Acuerdos del equipo

## 1. Propósito

Este documento establece los acuerdos de colaboración, comunicación,
organización y seguimiento del equipo que desarrolla QPM Clothes
mediante Scrum.

Los acuerdos buscan facilitar el trabajo conjunto, reducir errores
de integración y cumplir los objetivos de cada sprint.

## 2. Integrantes y roles

| Integrante | Rol Scrum | Responsabilidades principales |
|---|---|---|
| Juan Quintero | Scrum Master | Facilitar la planificación, promover la colaboración, hacer visibles los impedimentos y apoyar el seguimiento del sprint. |
| Marco | Product Owner | Comunicar las necesidades del producto, ayudar a priorizar el backlog y aclarar los criterios de aceptación. |
| Parra | Developer | Participar en el diseño, programación, integración, pruebas y documentación del producto. |

Los roles organizan las responsabilidades, pero no limitan la
participación de los integrantes. Todo el equipo debe colaborar
en las actividades necesarias para entregar un producto funcional.

## 3. Acuerdos de comunicación

1. Comunicar las dudas y los impedimentos tan pronto aparezcan.
2. Informar al equipo sobre los avances y las tareas pendientes.
3. Consultar antes de modificar decisiones técnicas que afecten
   a otros módulos.
4. Mantener los acuerdos y decisiones importantes en la documentación
   o en el repositorio.
5. Revisar conjuntamente los problemas que puedan retrasar el sprint.
6. Mantener una comunicación respetuosa y centrada en la solución.

## 4. Seguimiento del trabajo

El equipo realizará un seguimiento breve durante cada jornada
de trabajo.

Cada integrante debe poder comunicar:

- Qué trabajo terminó.
- En qué está trabajando.
- Qué necesita hacer a continuación.
- Qué dificultad o impedimento tiene.
- Si necesita apoyo de otro integrante.

El seguimiento no debe convertirse en una reunión extensa.
Su propósito es detectar bloqueos y coordinar el trabajo.

## 5. Organización de tareas

1. Las tareas deben ser pequeñas y tener un resultado verificable.
2. Cada tarea debe tener una persona encargada de impulsar su avance.
3. Cuando sea posible, otro integrante revisará el resultado.
4. Las tareas deben relacionarse con una historia de usuario
   o con una necesidad técnica documentada.
5. Se debe actualizar el estado de las tareas en el tablero acordado.
6. Las historias no se marcarán como terminadas sin comprobar
   sus criterios de aceptación.

Los estados de trabajo acordados son:

- Por hacer.
- En progreso.
- En revisión o pruebas.
- Terminado.

El equipo puede utilizar GitHub para llevar el seguimiento.

## 6. Acuerdos de programación

1. Utilizar Python 3.
2. Mantener la aplicación dentro del alcance de consola.
3. Utilizar archivos JSON para guardar y recuperar pedidos.
4. Utilizar CSV para los reportes que se implementen.
5. Escribir código legible, con nombres descriptivos.
6. Separar las responsabilidades en módulos cuando sea conveniente.
7. Evitar duplicar lógica de validación o reglas de negocio.
8. Manejar los errores previsibles con mensajes comprensibles.
9. No añadir funcionalidades de inventario o cotización.
10. Probar los cambios antes de integrarlos con el resto del proyecto.

## 7. Acuerdos de Git y GitHub

1. Utilizar el repositorio acordado para centralizar el código
   y la documentación.
2. Guardar cambios mediante commits pequeños y descriptivos.
3. Revisar el estado del proyecto antes de integrar cambios.
4. Coordinar la edición de archivos compartidos para reducir conflictos.
5. Resolver los conflictos de integración antes de continuar.
6. No subir contraseñas personales ni información sensible.
7. Mantener el README principal actualizado con el funcionamiento real.
8. No eliminar cambios de otro integrante sin coordinarlo.
9. Comprobar que la versión integrada puede ejecutarse.

Ejemplos de mensajes de commit:

- `docs: documentar el alcance del producto`
- `feat: registrar pedidos de ropa`
- `feat: guardar pedidos en JSON`
- `fix: validar fecha de entrega`
- `test: verificar actualización de estados`

Estos ejemplos sirven como guía; los mensajes deben describir
el cambio que realmente se realizó.

## 8. Acuerdos para las reuniones Scrum

### Sprint Planning

El equipo acuerda el objetivo del sprint, las historias prioritarias,
las tareas necesarias y la capacidad disponible.

### Seguimiento diario breve

Los integrantes informan sus avances, próximos pasos y bloqueos.

### Sprint Review

El equipo muestra las funcionalidades realmente implementadas
y verifica si cumplen los criterios de aceptación.

### Sprint Retrospective

El equipo identifica qué funcionó, qué dificultad se presentó
y qué mejora concreta aplicará en el siguiente sprint.

Las reuniones se adaptarán a las jornadas y al tiempo disponible.

## 9. Gestión de cambios

Si aparece una nueva necesidad o se identifica una función que
no estaba contemplada:

1. Describir la necesidad.
2. Evaluar su valor para el usuario.
3. Estimar el esfuerzo y las dependencias.
4. Revisar su efecto sobre el sprint y la fecha de entrega.
5. Acordar si se incorpora, se aplaza o se descarta.
6. Actualizar el backlog y la documentación cuando corresponda.

No se deben agregar funciones nuevas de manera improvisada si
ponen en riesgo las funcionalidades esenciales o los requisitos
obligatorios de la actividad.

## 10. Acuerdo de calidad

Todos los integrantes se comprometen a:

- Revisar los criterios de aceptación antes de programar.
- Probar los casos válidos e inválidos relevantes.
- Informar los errores encontrados.
- Ayudar a resolver problemas de integración.
- Actualizar la documentación necesaria.
- No presentar como terminada una función que no se ha comprobado.
- Priorizar la estabilidad y el cumplimiento del alcance acordado.

## 11. Acuerdo de alcance

QPM Clothes será una aplicación de consola en Python destinada
a gestionar y hacer seguimiento de pedidos de ropa.

El producto no se convertirá en un sistema de inventario, control
de existencias o cotización como objetivo principal.

Las decisiones técnicas y funcionales deben mantenerse alineadas
con el Product Goal y con las historias de usuario aprobadas.

## 12. Fechas de trabajo acordadas

| Sprint | Fecha | Enfoque |
|---|---|---|
| Sprint 1 | 23 de octubre de 2026 | Planificación y preparación |
| Sprint 2 | 24 de octubre de 2026 | Construcción de la versión mínima funcional |
| Sprint 3 | 25 de octubre de 2026 | Pruebas, estabilización y entrega |

## 13. Revisión de los acuerdos

Los acuerdos podrán ajustarse cuando el equipo identifique una mejora
necesaria. Todo cambio relevante debe comunicarse a los integrantes
y quedar reflejado en el documento.

El objetivo de estos acuerdos es trabajar de manera organizada,
colaborativa y transparente para entregar una versión funcional
y verificable de QPM Clothes.