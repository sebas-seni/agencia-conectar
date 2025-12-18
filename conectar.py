import usuario
import logica
import constantes

def main():

    peliculas = {}

    acciones = {
        1: logica.cargar_peliculas,
        2: logica.cargar_info_ventas,
        3: logica.imprimir_colabs_directas,
        4: logica.imprimir_talentos_compatibles,
        5: logica.imprimir_talentos_incompatibles,
        6: logica.exportar_recaudaciones
    }


    while True:
        opcion = usuario.pedir_opcion()

        if opcion == constantes.SALIR:
            break

        accion = acciones.get(opcion)

        if accion:
            accion(peliculas)

if __name__ == "__main__":
    main()
