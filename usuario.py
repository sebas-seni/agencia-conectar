import constantes

def mostrar_menu_principal():
    """Muestra el menú principal con todas las opciones."""

    opcion = input(constantes.MSG_MENU)

    return opcion

def pedir_opcion():
    """
    Solicita al usuario que ingrese numero entre 1 y 7.
    La función continua hasta que se ingrese un número válido.

    POST-CONDICIONES:
        - Devuelve la opción válida o el programa finaliza si se ingresa un 7.
    """

    while True:
        opcion_elegida = mostrar_menu_principal().strip()

        if opcion_elegida == "**":
            print(constantes.OPCION_INVALIDA)

            continue

        if not opcion_elegida.isdigit():
            print(constantes.OPCION_INVALIDA)
            continue

        opcion_elegida = int(opcion_elegida)

        if 0 < opcion_elegida < 8:
            return opcion_elegida

        print(constantes.OPCION_INVALIDA)


def pedir_talento():
    """
    Pide al usuario que ingrese el nombre de un talento. Devuelve el input del usuario.
    """
    input_usuario = input(constantes.MSG_TALENTO)

    return input_usuario
