from configuracion import RUTA_PEDIDOS, RUTA_BITACORA, RUTA_REPORTES
from excepciones import ErrorAplicacion
from persistencia.archivo_json import ArchivoJSON
from persistencia.bitacora_texto import BitacoraTexto
from colecciones.coleccion_pedidos import ColeccionPedidos
from reglas_negocio.gestor_pedidos import GestorPedidos
from reportes.exportar_csv import ExportadorCSV
from consola.menu_principal import MenuPrincipal
from consola.opciones_menu import OpcionesMenu
from consola.mostrar_pedidos import MostrarPedidos
from consola.lectura_datos import LecturaDatos


def main():
    archivo = ArchivoJSON(RUTA_PEDIDOS)
    bitacora = BitacoraTexto(RUTA_BITACORA)
    coleccion = ColeccionPedidos()
    try:
        coleccion.cargar_desde_lista(archivo.cargar())
    except Exception as error:
        try:
            bitacora.registrar(f"Error al cargar los pedidos: {error}")
        except OSError:
            pass
        print(f"No fue posible cargar los datos: {error}")
        print("El archivo no fue modificado. Corrija o restaure pedidos.json e inicie de nuevo.")
        return

    gestor = GestorPedidos(coleccion, archivo, bitacora)
    exportador = ExportadorCSV(RUTA_REPORTES)
    mostrar = MostrarPedidos()
    lectura = LecturaDatos()
    menu = MenuPrincipal(OpcionesMenu(gestor, exportador, mostrar, lectura))

    try:
        while True:
            fecha_hora = lectura.leer_fecha_hora_trabajo()
            try:
                gestor.actualizar_fecha_hora_trabajo(fecha_hora)
                break
            except ErrorAplicacion as error:
                print(f"Error: {error}")
        menu.ejecutar()
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada finalizada. Se cierra la aplicación; los datos ya guardados se conservan.")


if __name__ == "__main__":
    main()
