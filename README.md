# QPM Clothes

Sistema de gestión y seguimiento de pedidos de una tienda de ropa. Aplicación de **consola** escrita en **Python**, con persistencia en archivos **JSON**, reportes en **CSV** y bitácora de errores en texto.

Proyecto desarrollado bajo metodología **Scrum** en el programa ADSO del **SENA** (Sprint 1: 23 oct. 2026 · Sprint 2: 24 oct. 2026 · Sprint 3: 25 oct. 2026).

- **Repositorio:** https://github.com/juanlsk29/QPM--CLOTHES (rama de entrega: `sprint-2`)

---

## 1. Equipo

| Integrante | Rol |
| --- | --- |
| Juan Quintero | Scrum Master |
| Marco Gonzales | Product Owner |
| Brayan Parra | Developer |

---

## 2. Objetivo y alcance

**Product Goal:** entregar una aplicación de terminal clara y funcional que permita a la persona encargada de la tienda administrar el ciclo de vida de los pedidos de ropa, desde su registro hasta su entrega o cancelación, con datos persistentes y validaciones que reduzcan errores de seguimiento.

**Incluye:** registro de pedidos y prendas, listado y detalle, actualización de datos y de estado, cancelación, búsqueda y filtros, historial de estados, consulta de pedidos atrasados y próximos a vencer, persistencia en JSON, reportes CSV y resumen general.

**No incluye:** inventario o stock, cotizaciones, interfaz gráfica o web, base de datos relacional, pagos ni servicios externos.

---

## 3. Requisitos

- **Python 3.10 o superior** (desarrollado y probado con Python 3.12; el equipo trabajó con 3.14).
- No requiere instalar librerías externas: usa únicamente la biblioteca estándar (`json`, `csv`, `pathlib`).
- Funciona en Windows, Linux y macOS desde cualquier terminal.

---

## 4. Cómo ejecutar

1. Descomprima el archivo `.zip`.
2. Abra una terminal dentro de la carpeta `QPM--CLOTHES/` (la que contiene `main.py`).
3. Inicie la aplicación:

```bash
python main.py
```

> En Linux/macOS puede ser necesario usar `python3 main.py`.

Al iniciar, el programa pide la **fecha y hora de trabajo** con el formato `AAAA-MM-DD HH:MM` (por ejemplo `2026-10-25 09:00`). Esta fecha **no se toma del reloj del sistema**: se ingresa manualmente y es la referencia para registrar pedidos, calcular atrasos y registrar el historial. Después se muestra el menú principal.

### Menú principal

| Opción | Acción | Historia |
| --- | --- | --- |
| 1 | Registrar pedido | HU-001, HU-002 |
| 2 | Listar pedidos | HU-003 |
| 3 | Consultar detalle de un pedido | HU-004 |
| 4 | Buscar pedidos por código o cliente | HU-009 |
| 5 | Filtrar pedidos por estado | HU-009 |
| 6 | Actualizar pedido | HU-005 |
| 7 | Cambiar estado | HU-006 |
| 8 | Cancelar pedido | HU-007 |
| 9 | Ver historial de estados | HU-010 |
| 10 | Consultar pedidos atrasados | HU-008 |
| 11 | Consultar pedidos próximos a vencer | HU-008 |
| 12 | Exportar pedidos pendientes a CSV | HU-013 |
| 13 | Exportar pedidos entregados a CSV | HU-013 |
| 14 | Exportar pedidos atrasados a CSV | HU-013 |
| 15 | Ver resumen general | HU-015 |
| 16 | Actualizar fecha y hora de trabajo | HU-008 |
| 0 | Salir | HU-014 |

---

## 5. Datos que maneja el sistema

**Pedido:** código único, cliente, fecha de registro, fecha de entrega, estado, lista de prendas e historial de cambios de estado.

**Prenda:** tipo, talla, color y cantidad.

| Dato | Valores permitidos |
| --- | --- |
| Estados | `Recibido`, `En preparacion`, `Listo`, `Entregado`, `Cancelado` |
| Tipos de prenda | `Camiseta`, `Pantalon`, `Buzo`, `Chaqueta`, `Vestido`, `Falda`, `Short`, `Otro` |
| Tallas | `XS`, `S`, `M`, `L`, `XL`, `XXL`, `Unica` |

> **Importante:** los valores se escriben **sin tilde** (`En preparacion`, `Pantalon`). Las mayúsculas y minúsculas no importan (`en preparacion` también se acepta), pero la versión con tilde (`En preparación`) es rechazada por la validación.

Otras validaciones: el código admite letras, números y guiones (máx. 20 caracteres) y se normaliza a mayúsculas; el cliente debe tener entre 2 y 80 caracteres; el color solo admite letras; la cantidad debe ser un entero mayor que cero; las fechas se validan incluyendo años bisiestos.

---

## 6. Reglas de negocio

1. Cada pedido tiene un código único.
2. Todo pedido debe tener al menos una prenda.
3. La fecha de entrega no puede ser anterior a la fecha de registro.
4. El estado inicial es `Recibido`.
5. Transiciones permitidas:

```
Recibido ──► En preparacion ──► Listo ──► Entregado
    │               │             │
    └───────────────┴─────────────┴──► Cancelado
```

6. `Entregado` y `Cancelado` son estados finales: no admiten más cambios.
7. Solo se pueden editar pedidos en estado `Recibido` o `En preparacion`.
8. Cancelar exige confirmación (`s/n`) y nunca borra el pedido.
9. **Atrasado:** pedido no finalizado con fecha de entrega anterior a la fecha de trabajo.
10. **Próximo a vencer:** pedido no finalizado cuya entrega está entre hoy y los 2 días siguientes.
11. La fecha y hora de trabajo no puede retroceder antes del último movimiento registrado.
12. Si `pedidos.json` está dañado, la aplicación informa el error, lo registra en la bitácora y **no sobrescribe el archivo**.
13. Los reportes CSV son solo exportaciones; no son fuente de datos del sistema.

El detalle completo está en `Docs/reglas_de_negocio.md`.

---

## 7. Estructura del proyecto

```
QPM--CLOTHES/
├── main.py                  Punto de entrada: crea los objetos e inicia el menú
├── ejecutar_pruebas.py      Ejecuta todas las pruebas automáticas
├── configuracion.py         Rutas, estados, tipos de prenda, tallas y constantes
├── excepciones.py           Excepciones propias de la aplicación
├── README.md                Este archivo
│
├── consola/                 Interfaz de terminal
│   ├── menu_principal.py        Menú y ciclo principal
│   ├── opciones_menu.py         Acción asociada a cada opción
│   ├── lectura_datos.py         Lectura y validación de entradas
│   └── mostrar_pedidos.py       Presentación de listados, detalle, historial y resumen
│
├── modelos/                 Clases del dominio
│   ├── pedido.py
│   ├── prenda.py
│   └── cambio_estado.py
│
├── reglas_negocio/          Lógica del negocio
│   ├── gestor_pedidos.py        Operaciones sobre pedidos
│   ├── estados_pedido.py        Transiciones y reglas de edición
│   └── fechas_entrega.py        Atrasados y próximos a vencer
│
├── colecciones/
│   └── coleccion_pedidos.py     Colección de pedidos en memoria, búsqueda y filtros
│
├── validaciones/            Validación de datos
│   ├── validar_pedido.py
│   ├── validar_prenda.py
│   └── validar_fecha.py
│
├── persistencia/            Almacenamiento
│   ├── archivo_json.py          Lectura y escritura segura de pedidos.json
│   └── bitacora_texto.py        Registro de errores en bitacora.txt
│
├── reportes/                Reportes y resumen
│   ├── reportes_pedidos.py      Reportes pendientes, entregados y atrasados
│   ├── exportar_csv.py          Exportador a CSV
│   └── resumen_pedidos.py       Resumen general
│
├── pruebas/                 Pruebas automáticas por capa
├── datos/                   Datos generados por la aplicación
│   ├── pedidos.json             Pedidos guardados
│   ├── bitacora.txt             Bitácora de errores
│   └── reportes_csv/            Reportes exportados
│
└── Docs/                    Documentación del proyecto
    ├── estructura_del_proyecto.md
    ├── reglas_de_negocio.md
    ├── historias_de_usuario.md
    ├── guia_de_pruebas.md
    └── resultado_pruebas_iniciales.txt
```

**Arquitectura:** el proyecto se organiza en capas, una carpeta por responsabilidad. `main.py` solo ensambla los objetos; la consola no contiene reglas de negocio; las validaciones se reutilizan en modelos y consola; y las rutas de archivos se entregan a las clases al crearlas, de modo que las pruebas pueden usar archivos temporales.

---

## 8. Archivos generados

| Archivo | Descripción |
| --- | --- |
| `datos/pedidos.json` | Pedidos con sus prendas e historial. Se crea al guardar el primer pedido y se escribe de forma segura (archivo temporal + reemplazo). |
| `datos/bitacora.txt` | Errores de carga o de persistencia. |
| `datos/reportes_csv/pedidos_pendientes.csv` | Pedidos que no están `Entregado` ni `Cancelado`. |
| `datos/reportes_csv/pedidos_entregados.csv` | Pedidos en estado `Entregado`. |
| `datos/reportes_csv/pedidos_atrasados.csv` | Pedidos atrasados según la fecha de trabajo. |

Columnas de los CSV: `codigo, cliente, fecha_registro, fecha_entrega, estado` (codificación UTF-8 con BOM, para abrir correctamente en Excel).

---

## 9. Pruebas

Pruebas automáticas, desde la raíz del proyecto:

```bash
python ejecutar_pruebas.py
```

Cubren modelos, validaciones, reglas de negocio y gestor, persistencia (incluido JSON dañado) y reportes. El guion de pruebas manuales paso a paso está en `Docs/guia_de_pruebas.md`.

> **Estado conocido:** en la versión entregada, dos módulos de prueba (`prueba_reglas_negocio.py` y `prueba_reportes.py`) usan valores **con tilde** (`En preparación`, `Pantalón`), mientras que la aplicación define esos valores **sin tilde**. Por eso la ejecución completa se interrumpe con un `ErrorValidacion` y no termina en `APROBADO`. Los módulos `prueba_modelos`, `prueba_validaciones` y `prueba_persistencia` pasan sin fallos. Es un desajuste de los datos de prueba, no del flujo de la aplicación.

---

## 10. Trazabilidad de historias de usuario

| Prioridad | Historias | Funcionalidad |
| --- | --- | --- |
| P1 (esenciales) | HU-001 a HU-006, HU-008, HU-010 a HU-012, HU-014 | Registro y consulta, cambios de estado, vencimientos, historial, JSON, validaciones y menú |
| P2 (importantes) | HU-007, HU-009, HU-013 | Cancelación, búsqueda y filtros, exportación CSV |
| P3 (complementaria) | HU-015 | Resumen de pedidos |

Las 15 historias de usuario están implementadas según el Informe Final de Scrum.

---

## 11. Documentación y evidencias

- `Docs/` — estructura, reglas de negocio, historias de usuario y guía de pruebas.
- **Informe Final de Scrum** (`Informe_Final_Scrum_QPM_Clothes`) — seguimiento de los tres sprints, Definition of Done, retrospectivas y conclusiones.
- **Historias de usuario** (`Historias_de_usuario_QPM_Clothes.docx`) — HU-001 a HU-015 con criterios de aceptación.
- Historial de commits en GitHub, rama `sprint-2`.

---

## 12. Solución de problemas

| Situación | Qué hacer |
| --- | --- |
| `No fue posible cargar los datos` al iniciar | `pedidos.json` está dañado. Corríjalo o restáurelo; la aplicación no lo modifica. El detalle queda en `datos/bitacora.txt`. |
| `La fecha y hora de trabajo no puede ser anterior al último movimiento` | Ingrese una fecha igual o posterior al último cambio registrado. |
| `Estado no válido` al escribir `En preparación` | Escríbalo sin tilde: `En preparacion`. |
| Los reportes CSV salen vacíos | Es normal si no hay pedidos que cumplan la condición del reporte. |

---

## 13. Licencia y uso

Proyecto académico desarrollado con fines formativos en el SENA (ADSO). 
