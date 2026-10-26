# QPM Clothes — Estructura del proyecto

## 1. Propósito
Este documento define cómo se organiza el código de QPM Clothes: qué carpetas y archivos tiene el proyecto, qué responsabilidad tiene cada uno y por qué se organizaron de esa manera.

La estructura se construyó con una condición: todo el código debe basarse únicamente en lo aprendido en los cuatro laboratorios de Python. Lo que no aparece en ellos no se utiliza.

## 2. Referencia: el gestor de inventario del Laboratorio 4
El gestor de inventario del Laboratorio 4 sirvió como referencia de una aplicación de consola con clases, JSON y CSV. QPM Clothes no repite su estructura ni su forma de distribuir el código.

| Gestor de inventario (Laboratorio 4) | QPM Clothes |
|---|---|
| Todos los archivos están en una sola carpeta. | Una carpeta por responsabilidad. |
| `main.py` contiene el menú, la lectura de datos, la carga del JSON y todo el flujo. | `main.py` solo crea los objetos e inicia el menú. La consola está dividida en cuatro archivos. |
| La clase `Inventario` guarda la colección y además aplica las operaciones. | La colección (`colecciones/`) y las operaciones y reglas (`reglas_negocio/`) están separadas. |
| Las validaciones se repiten en `main.py` y en `Producto`. | Las validaciones están en `validaciones/` y las usan los modelos y la consola. |
| Las rutas son constantes del archivo que las usa. | Las rutas están en `configuracion.py` y se entregan a las clases al crearlas, de modo que las pruebas pueden usar otros archivos. |
| Una sola excepción propia. | Una excepción base y tres excepciones específicas. |
| Un único tipo de reporte. | Una clase base de reporte y tres reportes que la especializan. |
| Las pruebas son scripts con `print`. | Pruebas por capa con una función que informa OK o FALLO. |

## 3. Estructura
```
QPM-Clothes/
├── main.py
├── ejecutar_pruebas.py
├── configuracion.py
├── excepciones.py
├── README.md
├── docs/
├── datos/
│   ├── pedidos.json          (se crea al guardar el primer pedido)
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
```

## 4. Criterios para los nombres
- Cada carpeta y cada archivo se llama como lo que contiene: `estados_pedido.py` contiene las reglas de los estados del pedido; `archivo_json.py` lee y escribe el archivo JSON.
- Los archivos que contienen una clase llevan el nombre de esa clase en minúsculas y con guiones bajos: `Pedido` está en `pedido.py`.
- Los archivos de funciones comienzan con un verbo o con el tema que tratan: `validar_prenda.py`, `exportar_csv.py`.
- Se evitan nombres genéricos como utilidades, ayudas, varios o helpers.

## 5. Responsabilidad de cada carpeta y archivo

### 5.1 Raíz del proyecto
| Archivo | Responsabilidad | Contenido principal |
|---|---|---|
| `main.py` | Punto de entrada. Crea el archivo JSON, la colección y el gestor, carga los pedidos, pide la fecha y hora de trabajo e inicia el menú. | Función `main()` y `if __name__ == "__main__":`. |
| `ejecutar_pruebas.py` | Ejecuta las pruebas de todas las capas y muestra el resultado total. | Importa las funciones de `pruebas/`. |
| `configuracion.py` | Constantes del proyecto. | `ESTADOS`, `ESTADO_INICIAL`, `ESTADOS_FINALES`, `TIPOS_PRENDA`, `TALLAS`, `DIAS_VENCIMIENTO`, `DIAS_POR_MES` y las rutas de `datos/` construidas con `Path(__file__).resolve().parent`. |
| `excepciones.py` | Errores propios. | `ErrorAplicacion` (base), `ErrorValidacion`, `ErrorReglaNegocio` y `ErrorArchivoDatos`, que heredan de la base. |
| `README.md` | Requisitos, ejecución, uso y pruebas. | — |

`ejecutar_pruebas.py` y `main.py` están en la raíz para que las importaciones entre carpetas funcionen al ejecutarlos desde allí.

### 5.2 `consola/` — interacción con el usuario
Es la única carpeta que usa `input()` y `print()` (además de `main.py`, que informa el error de carga). Ninguna otra carpeta importa archivos de `consola/`.

| Archivo | Responsabilidad |
|---|---|
| `menu_principal.py` | Muestra el menú y repite el ciclo hasta que se elige salir. Redirige cada opción a `opciones_menu.py`. |
| `opciones_menu.py` | Una función por cada opción del menú: pide los datos, llama al gestor y muestra el resultado o el error. Captura `ErrorAplicacion`. Pide confirmación antes de cancelar un pedido. |
| `lectura_datos.py` | Lee texto, fechas, horas, estados y confirmaciones. Repite la pregunta si el dato no es válido, usando las funciones de `validaciones/`. |
| `mostrar_pedidos.py` | Da formato a lo que se imprime: listado, detalle, historial, alertas (con motivo) y resumen. |

### 5.3 `modelos/` — entidades del dominio
Las clases no usan `input()` ni `print()`. Validan sus propios datos con `validaciones/`.

| Archivo | Clase | Responsabilidad |
|---|---|---|
| `prenda.py` | `Prenda` | Tipo, talla, color y cantidad. Propiedades de solo lectura, `a_diccionario()`, `desde_diccionario()` y `__str__()`. |
| `cambio_estado.py` | `CambioEstado` | Estado anterior, estado nuevo y fecha y hora del cambio. El estado inicial se registra con estado anterior vacío. |
| `pedido.py` | `Pedido` | Código, cliente, fecha de registro, fecha de entrega, estado, lista de prendas y lista de cambios de estado. Métodos para agregar o reemplazar prendas, actualizar cliente y fecha de entrega, registrar (y deshacer) un cambio de estado y saber si está finalizado. Convierte el pedido a diccionario y lo reconstruye. |

Un `Pedido` contiene sus `Prenda` y sus `CambioEstado`; esos objetos no existen fuera de un pedido. Un pedido nunca queda sin prendas.

### 5.4 `reglas_negocio/` — reglas y operaciones
| Archivo | Responsabilidad |
|---|---|
| `estados_pedido.py` | Diccionario `TRANSICIONES` (estado actual → tupla de estados permitidos), comprobación de una transición y regla de qué estados permiten editar el pedido. No usa archivos ni consola. |
| `fechas_entrega.py` | Convierte una fecha a número de día, calcula los días que faltan para la entrega y decide si un pedido está atrasado o próximo a vencer. Recibe la fecha de hoy como parámetro. |
| `gestor_pedidos.py` | Clase `GestorPedidos`. Recibe la colección y el archivo JSON al crearse. Registra, actualiza, cambia el estado y cancela pedidos, busca, filtra, consulta los atrasados y próximos a vencer, controla la fecha y hora de trabajo y guarda los cambios (deshaciéndolos si el guardado falla). |

### 5.5 `colecciones/` — gestión de colecciones
| Archivo | Responsabilidad |
|---|---|
| `coleccion_pedidos.py` | Clase `ColeccionPedidos`. Guarda los pedidos en un diccionario con el código como clave. Agrega (rechazando códigos repetidos), elimina, busca por código, busca por cliente o por parte del código o del cliente sin importar mayúsculas, filtra por estado, entrega una copia de la lista y convierte sus datos para el JSON. Al cargar datos usa una colección temporal para no dejar una carga a medias. |

Esta carpeta tiene un único archivo porque en el proyecto existe una sola colección.

### 5.6 `validaciones/` — validación de datos
Las funciones reciben un dato, lo limpian y lo devuelven; si no es válido lanzan `ErrorValidacion` con un mensaje claro.

| Archivo | Responsabilidad |
|---|---|
| `validar_pedido.py` | Código, cliente, estado, texto de búsqueda y relación entre la fecha de registro y la de entrega. |
| `validar_prenda.py` | Tipo, talla, color y cantidad (entero mayor que cero). |
| `validar_fecha.py` | Formato AAAA-MM-DD, existencia real de la fecha (años bisiestos y días por mes), formato HH:MM y comparación de fecha y hora. |

### 5.7 `persistencia/` — archivos
| Archivo | Responsabilidad |
|---|---|
| `archivo_json.py` | Clase `ArchivoJSON`. Recibe la ruta al crearse. `cargar()` distingue el archivo inexistente (devuelve lista vacía), el válido (devuelve los datos) y el dañado (lanza `ErrorArchivoDatos`). `guardar()` escribe con `encoding="utf-8"`. Un archivo dañado nunca se sobrescribe. |
| `bitacora_texto.py` | Clase `BitacoraTexto`. Agrega líneas a un archivo de texto (por ejemplo, el aviso de un JSON dañado) y puede leerlas. |

### 5.8 `reportes/` — reportes
| Archivo | Responsabilidad |
|---|---|
| `reportes_pedidos.py` | Clase base `Reporte` con los encabezados, el nombre del archivo y el método `seleccionar()`, que lanza `NotImplementedError`. Las clases `ReportePendientes`, `ReporteEntregados` y `ReporteAtrasados` sobrescriben `seleccionar()`. |
| `exportar_csv.py` | Clase `ExportadorCSV`. Recibe la carpeta de destino y escribe cualquier `Reporte` con `csv.DictWriter`, con encabezados. Informa el error si no puede escribir. |
| `resumen_pedidos.py` | Calcula la cantidad de pedidos por estado (con ceros), los atrasados y los clientes distintos; devuelve un diccionario. |

### 5.9 `datos/`
| Elemento | Contenido |
|---|---|
| `pedidos.json` | Pedidos y su historial. Es el mecanismo principal de persistencia. Se crea al guardar por primera vez. |
| `bitacora.txt` | Registro de incidentes en texto. |
| `reportes_csv/` | Archivos CSV exportados. Solo se escriben desde la aplicación; nunca se leen como datos. |

### 5.10 `pruebas/`
| Archivo | Comprueba |
|---|---|
| `comprobar.py` | Función `comprobar(descripcion, condicion)` que informa OK o FALLO y acumula los resultados. |
| `prueba_modelos.py` | Creación de pedidos, prendas e historial; conversión a diccionario y de vuelta. |
| `prueba_validaciones.py` | Casos válidos e inválidos de cantidad, fecha, hora, código, talla y estado. |
| `prueba_reglas_negocio.py` | Transiciones, atrasados y próximos a vencer, y el flujo del gestor: registro, edición, cambio de estado, cancelación, historial, búsqueda y fecha de trabajo. |
| `prueba_persistencia.py` | Archivo inexistente, válido y dañado; el archivo dañado no se modifica. Usa archivos temporales, no `datos/`. |
| `prueba_reportes.py` | Los tres reportes, los encabezados del CSV, el CSV vacío y el resumen. |

## 6. Dependencias entre carpetas
- `consola/` usa `reglas_negocio/`, `colecciones/`, `reportes/` y `validaciones/`.
- `reglas_negocio/` usa `modelos/`, `colecciones/`, `persistencia/` y `validaciones/`.
- `reportes/` usa `modelos/` y `reglas_negocio/fechas_entrega.py`.
- `colecciones/` y `persistencia/` usan `modelos/`.
- `modelos/` usa `validaciones/`.
- `validaciones/` usa solo `configuracion.py` y `excepciones.py`.
- Ninguna carpeta, salvo `consola/`, usa `input()` o `print()`.
- Ninguna carpeta importa archivos de `consola/`.

## 7. Ejemplo de flujo: registrar un pedido
1. `menu_principal.py` recibe la opción y llama a la función de `opciones_menu.py`.
2. `opciones_menu.py` pide los datos con `lectura_datos.py`, que repite cada pregunta hasta recibir un dato válido.
3. `opciones_menu.py` llama a `GestorPedidos.registrar_pedido(...)`.
4. El gestor crea el `Pedido` con sus `Prenda` e historial inicial; los modelos validan con `validaciones/`.
5. El gestor agrega el pedido a `ColeccionPedidos`, que rechaza el código repetido.
6. El gestor guarda con `ArchivoJSON.guardar()`.
7. Si algo falla, se lanza una excepción de `excepciones.py` y `opciones_menu.py` muestra el mensaje sin cerrar el programa.

## 8. Fecha y hora de trabajo
Los laboratorios no incluyen herramientas para obtener la fecha y la hora del sistema, por lo que la aplicación no las utiliza.
- Al iniciar, `main.py` pide la fecha y la hora de trabajo con el formato `AAAA-MM-DD HH:MM`.
- Esa fecha se usa como fecha de registro de los pedidos, como referencia para los pedidos atrasados y próximos a vencer, y como fecha y hora de cada cambio de estado.
- El menú incluye una opción para actualizar la fecha y la hora de trabajo. No puede ser anterior al último movimiento registrado, para que el historial conserve su orden.
- Las fechas se guardan como texto `AAAA-MM-DD`. Para compararlas se separan con `split()`, se convierten con `int()` y se comparan como tuplas (año, mes, día).
- Los años bisiestos y los días por mes se calculan con operadores y con la tupla `DIAS_POR_MES` de `configuracion.py`.

## 9. Correspondencia con los laboratorios
| Laboratorio | Dónde se aplica |
|---|---|
| 01 — Primeros pasos | Constantes en `configuracion.py`. `input()`, `print()` y cadenas formateadas en `consola/`. Conversiones con `int()` en `lectura_datos.py` y `validar_fecha.py`. |
| 02 — Decisiones, ciclos y colecciones | `if`, `elif`, `else` y `while` en el menú y en las lecturas con reintento. `for` en listados y reportes. Listas de prendas y de historial. Tuplas en `ESTADOS`, `TIPOS_PRENDA` y `DIAS_POR_MES`. Conjuntos para clientes distintos en el resumen. Diccionarios en `ColeccionPedidos`, `TRANSICIONES` y el resumen. Estructuras anidadas en el JSON (pedido con prendas e historial). Comprensiones en los filtros. |
| 03 — Funciones, módulos y POO | Funciones con parámetros y retorno en `validaciones/` y `reglas_negocio/`. Importaciones entre módulos. Clases con `__init__`, `self`, propiedades y atributos con guion bajo en `modelos/`. Colaboración entre `GestorPedidos`, `ColeccionPedidos` y `Pedido`. |
| 04 — Excepciones, archivos, persistencia y POO | `try`, `except` y `raise` en `consola/`, `persistencia/` y `validaciones/`. `pathlib` en `configuracion.py` y `persistencia/`. Archivo de texto en `bitacora_texto.py`. JSON en `archivo_json.py`. CSV en `exportar_csv.py`. Herencia, sobrescritura y polimorfismo en `reportes_pedidos.py` y `excepciones.py`. Composición en `Pedido`, `GestorPedidos` y `ExportadorCSV`. |

Justificación de la herencia: los tres reportes comparten los encabezados y la forma de exportarse, y solo cambian los pedidos que seleccionan; las excepciones específicas son casos de un error general de la aplicación, de modo que el menú puede capturarlas todas con `ErrorAplicacion`. No se crearon jerarquías para otros conceptos.

## 10. Decisiones pendientes de confirmar
- Transiciones de estado propuestas: Recibido → En preparación o Cancelado; En preparación → Listo o Cancelado; Listo → Entregado o Cancelado; Entregado y Cancelado no tienen cambios posteriores.
- Estados que permiten editar un pedido: Recibido y En preparación; falta confirmar si Listo también (HU-005). El código bloquea Listo.
- Ventana de pedidos próximos a vencer: 2 días, según la propuesta de la HU-008.
- Tipos de prenda y tallas válidos para `TIPOS_PRENDA` y `TALLAS`.
