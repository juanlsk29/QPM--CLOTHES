# QPM Clothes — Objetivo y alcance del producto

## 1. Información general

- **Nombre del proyecto:** QPM Clothes
- **Tipo de aplicación:** Aplicación de consola.
- **Lenguaje de programación:** Python 3.
- **Persistencia:** Archivos JSON.
- **Reportes:** Archivos CSV.
- **Metodología de trabajo:** Scrum.
- **Equipo:** Juan Quintero, Marco Gonzales y Brayan Parra.
- **Fechas de planificación:** 23, 24 y 25 de octubre de 2026.

## 2. Problema identificado

Una tienda pequeña de ropa puede recibir pedidos personalizados que
incluyen diferentes prendas, tallas, colores y cantidades, cada uno
con una fecha acordada de entrega.

Cuando la información se registra en notas o archivos separados,
puede resultar difícil consultar el estado de los pedidos, encontrar
los que están atrasados y recordar los cambios realizados.

QPM Clothes busca centralizar esta información en una aplicación
sencilla que permita registrar, consultar y hacer seguimiento de
los pedidos desde la terminal.

## 3. Product Goal

Desarrollar una aplicación de consola en Python que permita administrar
el ciclo de vida de los pedidos de una tienda de ropa, desde su registro
hasta su entrega o cancelación, conservando la información mediante
archivos JSON y aplicando validaciones para reducir errores.

## 4. Usuarios objetivo

- **Encargado de la tienda:** registra pedidos, consulta información,
  actualiza estados y revisa las fechas de entrega.
- **Personal de apoyo:** consulta los detalles necesarios para preparar
  y entregar las prendas solicitadas.

## 5. Funcionalidades incluidas

1. Registrar pedidos con un código único.
2. Registrar los datos del cliente.
3. Agregar una o varias prendas a cada pedido.
4. Guardar el tipo de prenda, talla, color y cantidad.
5. Consultar el listado de pedidos.
6. Consultar el detalle de un pedido.
7. Actualizar los datos permitidos de un pedido.
8. Cambiar el estado de los pedidos.
9. Cancelar pedidos de acuerdo con las reglas definidas.
10. Identificar pedidos atrasados y próximos a vencer.
11. Guardar y recuperar los pedidos utilizando archivos JSON.
12. Validar los datos ingresados y controlar errores.
13. Buscar y filtrar pedidos.
14. Consultar el historial de cambios de estado.
15. Exportar reportes a archivos CSV.
16. Consultar un resumen general de los pedidos.
17. Navegar por las funcionalidades mediante un menú de consola.

Las funcionalidades se implementarán según la prioridad y la capacidad
del equipo durante los sprints.

## 6. Funcionalidades excluidas

QPM Clothes no tendrá como objetivo principal:

- Administrar inventarios o existencias.
- Registrar entradas o salidas de stock.
- Calcular el valor total de un inventario.
- Funcionar como cotizador de prendas.
- Gestionar compras en línea o pagos.
- Generar facturación electrónica.
- Utilizar una interfaz gráfica o una página web.
- Utilizar una base de datos relacional.
- Enviar notificaciones automáticas por correo, SMS o WhatsApp.
- Integrarse con servicios externos.

La persistencia se realizará mediante archivos JSON, y los reportes
complementarios se generarán en CSV.


## 7. Criterio de éxito

El producto será satisfactorio cuando permita ejecutar desde la
terminal el flujo principal de gestión de pedidos, guardar y recuperar
la información, validar los datos importantes y consultar correctamente
el estado y las fechas de entrega.

Las funciones complementarias se entregarán si la capacidad del equipo
lo permite, sin comprometer las funcionalidades esenciales ni los
requisitos obligatorios del instructor.