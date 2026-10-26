# Guía de pruebas

## Automáticas
`python ejecutar_pruebas.py` desde la raíz. Debe indicar cero fallos. Cubren modelos, validaciones, reglas de negocio y el gestor (registro, edición, estados, cancelación, historial, búsqueda, fecha de trabajo), persistencia y reportes.

## Recorrido manual recomendado
1. Inicie la aplicación e ingrese `2026-10-24 16:00`.
2. Registre `Q-001`, cliente `Ana Pérez`, entrega `2026-10-26` y una camiseta (opción 1).
3. Liste (2), consulte el detalle de `Q-001` (3) y busque `ana` y `q-0` (4); filtre por `Recibido` (5).
4. Cambie el estado a `En preparación` (7) y revise el historial (9).
5. Intente pasar de `En preparación` a `Entregado`: debe rechazarse y conservar el estado.
6. Elija Cancelado en la opción 7 y responda `n`: el estado no cambia.
7. Consulte próximos a vencer (11) con fecha de trabajo `2026-10-25 09:00` y atrasados (10) con `2026-10-27 09:00`.
8. Exporte los tres reportes (12 a 14) y revise `datos/reportes_csv/`.
9. Salga, vuelva a iniciar y verifique que pedidos e historial persisten.
10. Escriba `2025-02-29` como fecha de entrega: debe rechazarse y pedirla de nuevo.
11. Dañe `datos/pedidos.json` (por ejemplo, escriba `{roto`): la aplicación debe informar el error, registrarlo en `bitacora.txt` y no modificar el archivo.
