# QPM Clothes — Estructura del proyecto

## 1. Propósito

Este documento explica cómo se organiza el código de QPM Clothes, qué responsabilidad tiene cada carpeta y archivo, y cómo se relacionan sus partes.

La aplicación es un sistema de consola en Python para registrar y gestionar pedidos de prendas de vestir. Utiliza archivos JSON para conservar los datos y CSV para generar reportes. Su diseño se mantiene dentro de los conceptos estudiados en los cuatro laboratorios de Python: funciones, módulos, programación orientada a objetos, validaciones, excepciones y manejo de archivos.

## 2. Principios de organización

- Cada módulo tiene una responsabilidad principal.
- Los modelos representan los datos que utiliza la aplicación.
- Las reglas de negocio determinan qué operaciones se permiten.
- Las validaciones revisan los datos antes de procesarlos.
- La persistencia se encarga de leer y escribir archivos.
- Los reportes preparan la información solicitada y la exportan cuando corresponde.
- El menú coordina la interacción con el usuario, pero no debe concentrar toda la lógica del sistema.
- No se utilizan bases de datos, frameworks, paquetes externos ni servicios web.

## 3. Árbol de carpetas y archivos

La siguiente estructura corresponde a la organización técnica acordada para el proyecto. Si durante la implementación se modifica algún nombre o archivo, se debe actualizar este documento para que represente la estructura real del repositorio.

```text
QPM-CLOTHES/
├── main.py
├── ejecutar_pruebas.py
├── configuracion.py
├── excepciones.py
├── README.md
├── datos/
│   ├── pedidos.json
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
├── pruebas/
│   ├── comprobar.py
│   ├── prueba_modelos.py
│   ├── prueba_validaciones.py
│   ├── prueba_reglas_negocio.py
│   ├── prueba_persistencia.py
│   └── prueba_reportes.py
└── docs/
    ├── 01_product_goal_y_alcance.md
    ├── 02_historias_de_usuario.md
    ├── 03_planificacion_sprints.md
    ├── 04_tareas_tecnicas.md
    ├── 05_definition_of_done.md
    ├── 06_acuerdos_del_equipo.md
    ├── 07_estructura_del_proyecto.md
    └── 08_plan_de_pruebas.md
```

## 4. Responsabilidad de los archivos principales

| Archivo o carpeta | Responsabilidad |
|---|---|
| `main.py` | Punto de entrada. Inicia la aplicación y conecta el flujo general. |
| `ejecutar_pruebas.py` | Permite iniciar las comprobaciones o pruebas organizadas para el proyecto. |
| `configuracion.py` | Centraliza valores de configuración del sistema, como las credenciales definidas en el código y otros valores fijos necesarios. |
| `excepciones.py` | Agrupa el manejo o las definiciones de excepciones propias que el proyecto necesite, sin reemplazar el manejo estándar de errores de Python. |
| `README.md` | Explica el propósito del proyecto, los requisitos, cómo ejecutarlo y cómo utilizar sus funciones principales. | --//PROXIMO A AÑADIR\\--
| `datos/pedidos.json` | Archivo de datos donde se guardan los pedidos para recuperarlos entre ejecuciones. |
| `datos/reportes_csv/` | Carpeta de destino para los archivos CSV generados por los reportes. |
| `consola/` | Contiene la interacción con el usuario: menú, lectura de opciones y presentación de resultados. |
| `modelos/` | Define las entidades y los datos principales: pedidos, prendas y cambios de estado. |
| `reglas_negocio/` | Implementa las reglas para gestionar pedidos, sus estados y las fechas de entrega. |
| `colecciones/` | Administra la colección de pedidos en memoria durante la ejecución. |
| `validaciones/` | Revisa que los datos de pedidos, prendas y fechas cumplan las condiciones establecidas. |
| `persistencia/` | Se encarga de leer y guardar información en archivos, incluyendo JSON y la bitácora de texto si se utiliza. |
| `reportes/` | Consulta, organiza y presenta información de pedidos; incluye la exportación a CSV y el resumen general. |
| `pruebas/` | Agrupa las comprobaciones de modelos, validaciones, reglas de negocio, persistencia y reportes. |


## 5. Función de los módulos específicos

### `consola/`

- `menu_principal.py`: presenta el menú general de la aplicación.
- `opciones_menu.py`: coordina la acción correspondiente a la opción elegida.
- `lectura_datos.py`: solicita y lee los datos que ingresa el usuario.
- `mostrar_pedidos.py`: presenta listados y detalles de pedidos de forma legible.

### `modelos/`

- `pedido.py`: representa la información de un pedido.
- `prenda.py`: representa las prendas asociadas a un pedido.
- `cambio_estado.py`: representa un cambio de estado para conservar la información del historial.

### `reglas_negocio/` y `colecciones/`

- `estados_pedido.py`: contiene las reglas para los estados y las transiciones permitidas.
- `fechas_entrega.py`: contiene las operaciones relacionadas con fechas de entrega y vencimientos.
- `gestor_pedidos.py`: coordina las operaciones de negocio sobre los pedidos.
- `coleccion_pedidos.py`: mantiene y administra los pedidos durante la ejecución.

### `validaciones/`

- `validar_pedido.py`: comprueba los datos requeridos para registrar o modificar un pedido.
- `validar_prenda.py`: comprueba los datos de las prendas.
- `validar_fecha.py`: comprueba el formato y las condiciones de las fechas.

### `persistencia/`

- `archivo_json.py`: carga y guarda los pedidos en formato JSON y gestiona los errores de lectura o escritura previstos.
- `bitacora_texto.py`: registra información textual de seguimiento si esa función está implementada y forma parte de la ejecución real.

### `reportes/`

- `reportes_pedidos.py`: obtiene los grupos de pedidos necesarios para las consultas y reportes.
- `exportar_csv.py`: genera los archivos CSV de pedidos pendientes, entregados y atrasados.
- `resumen_pedidos.py`: calcula y muestra el resumen general contemplado en el alcance.

### `pruebas/`

- `comprobar.py`: reúne comprobaciones auxiliares reutilizables, si son necesarias.
- `prueba_modelos.py`: comprueba el comportamiento de los modelos.
- `prueba_validaciones.py`: comprueba las validaciones de datos.
- `prueba_reglas_negocio.py`: comprueba las reglas de estados y fechas.
- `prueba_persistencia.py`: comprueba el guardado y la recuperación de información.
- `prueba_reportes.py`: comprueba las consultas y los reportes.

## 6. Flujo general de funcionamiento

1. El usuario ejecuta `main.py`.
2. La aplicación carga la configuración y solicita el inicio de sesión con las credenciales definidas en el código.
3. El menú de consola presenta las operaciones disponibles y recibe la opción seleccionada.
4. Los módulos de consola leen los datos y delegan las operaciones a las reglas de negocio.
5. Las validaciones comprueban los datos antes de registrar o modificar pedidos.
6. Los modelos y la colección representan y administran los pedidos durante la ejecución.
7. El módulo de persistencia lee o escribe `datos/pedidos.json` para conservar la información.
8. Las consultas y reglas de fechas permiten listar, buscar, filtrar, actualizar, cancelar y revisar pedidos atrasados o próximos a vencer.
9. Los módulos de reportes preparan el resumen o generan archivos CSV en `datos/reportes_csv/`.
10. El usuario puede salir de la aplicación; los datos guardados en JSON permanecen disponibles para una ejecución posterior.

## 7. Formatos de archivo

| Formato | Uso en QPM Clothes |
|---|---|
| JSON | Guardar y recuperar la información de los pedidos. |
| CSV | Exportar reportes de pedidos pendientes, entregados y atrasados. |
| TXT | Utilizarse para una bitácora únicamente si la funcionalidad está implementada en el sistema. |


## 8. Relación con los laboratorios de Python

La estructura busca aplicar lo estudiado sin introducir herramientas ajenas al alcance:

- **Funciones y módulos:** separación del programa por responsabilidades.
- **Programación orientada a objetos:** representación de pedidos, prendas y cambios de estado.
- **Validaciones y excepciones:** revisión de entradas y tratamiento de errores.
- **Archivos y rutas:** acceso a los archivos de datos y organización de carpetas.
- **JSON:** persistencia de pedidos.
- **CSV:** exportación de reportes.
- **Pruebas y documentación:** comprobación del comportamiento y explicación de la solución.

## 9. Mantenimiento de este documento

Este archivo describe la estructura prevista y debe mantenerse sincronizado con el repositorio. Antes de la entrega, el equipo debe verificar que los archivos enumerados existan realmente, que sus responsabilidades coincidan con su código y que no se documenten funcionalidades que no estén implementadas. Si la estructura final difiere de este árbol, se debe corregir el documento en lugar de presentar una estructura ideal como si ya estuviera construida.
