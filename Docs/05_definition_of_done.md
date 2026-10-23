# QPM Clothes — Definition of Done

## 1. Propósito

La Definition of Done (DoD) establece las condiciones mínimas que debe
cumplir una historia de usuario para considerarse terminada.

Su objetivo es evitar que una funcionalidad se marque como completada
cuando todavía presenta errores, no cumple sus criterios de aceptación
o no está integrada con el resto de la aplicación.

## 2. Criterios generales

Una historia de usuario se considera terminada cuando:

-  Cumple sus criterios de aceptación.
-  La funcionalidad está implementada y conectada con los módulos
  que necesita.
-  El código tiene nombres claros y una organización comprensible.
-  No presenta errores críticos conocidos que impidan utilizarla.
-  Se validan los datos de entrada que correspondan.
-  Los mensajes de error ayudan a entender y corregir los problemas.
-  Se han probado los casos válidos e inválidos relevantes.
-  El comportamiento de la funcionalidad coincide con las reglas
  de negocio acordadas.
-  Los cambios están integrados con la versión actual del proyecto.
-  Otro integrante puede revisar el código y comprender su propósito.
-  Se actualiza la documentación cuando la funcionalidad modifica
  instrucciones o comportamiento de uso.
- Los cambios están guardados en el repositorio.

## 3. Criterios para pedidos y prendas

Cuando una historia afecta el registro o actualización de pedidos:

- Cada pedido tiene un código único.
- Se solicitan los datos obligatorios.
- Cada pedido contiene al menos una prenda cuando se registra.
- Cada prenda tiene tipo, talla, color y cantidad.
- La cantidad es un entero mayor que cero.
- La fecha de entrega no es anterior a la fecha de registro.
- Las actualizaciones respetan los campos que se pueden modificar.
- Los pedidos existentes se pueden localizar y consultar.
- Los cambios no eliminan accidentalmente información necesaria.

Solo deben aplicarse los criterios relacionados con la historia que
se está verificando.

## 4. Criterios para estados e historial

Cuando una historia modifica el estado de un pedido:

- Se utilizan únicamente los estados permitidos:
  Recibido, En preparación, Listo, Entregado y Cancelado.
- Se respetan las transiciones de estado definidas.
- Los cambios no permitidos se rechazan con un mensaje claro.
- Cuando el historial esté implementado, se conserva el estado
  anterior, el nuevo estado y la fecha y hora del cambio.
- Los pedidos entregados o cancelados no se identifican como atrasados.

## 5. Criterios para persistencia JSON

Cuando una historia utiliza el almacenamiento de datos:

- Los datos se guardan correctamente en JSON.
- La aplicación puede recuperar los datos en una nueva ejecución.
- Se manejan los errores de lectura y escritura.
- La ausencia inicial del archivo se trata de acuerdo con el diseño.
- Un archivo dañado no se sobrescribe silenciosamente.
- La aplicación informa al usuario cuando no puede recuperar
  o guardar la información.

## 6. Criterios para reportes CSV

Cuando se implemente la exportación:

- El archivo CSV contiene encabezados.
- Las columnas corresponden a los datos definidos para el reporte.
- Los registros exportados corresponden a la información disponible.
- El usuario recibe confirmación o un mensaje claro si la exportación falla.
- El archivo se guarda en la ubicación definida por el proyecto.

## 7. Criterios para el menú de consola

- Las opciones se presentan de forma comprensible.
- El usuario puede volver al menú cuando corresponda.
- Una opción inválida no cierra inesperadamente el programa.
- Las operaciones muestran mensajes que permiten identificar
  si se completaron o si requieren corrección.

## 8. Verificación y evidencias

El equipo debe comprobar cada historia con los criterios que le
correspondan. Puede utilizar pruebas manuales y, cuando sea viable,
pruebas automatizadas sencillas.

No se deben declarar pruebas como exitosas si no se han ejecutado.

## 9. Aprobación de una historia

Antes de marcar una historia como terminada, el equipo debe confirmar:

1. Que los criterios de aceptación se cumplen.
2. Que las pruebas relevantes se realizaron.
3. Que la funcionalidad está integrada.
4. Que no quedan errores críticos conocidos.
5. Que la documentación necesaria está actualizada.

Si una condición importante no se cumple, la historia debe permanecer
pendiente o identificarse como parcialmente implementada.

## 10. Aplicación de la DoD

Esta definición se aplica a las historias de usuario y a las
funcionalidades desarrolladas durante los sprints de QPM Clothes.

La DoD puede actualizarse mediante un acuerdo del equipo cuando
se identifiquen nuevas necesidades de calidad. Los cambios deben
quedar documentados y comunicarse a todos los integrantes.