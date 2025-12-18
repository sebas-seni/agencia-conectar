import os
import constantes


def limpiar_texto(texto: str)-> str:
    """Recibe el nombre de un talento y devuelve su version normalizada"""

    texto = texto.lower()
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")

    return texto


def es_talento_valido(input_usuario: str,mapa_talentos: dict)-> bool:
    """
    Valida que el talento ingresado por el usuario sea válido. Devuelve True o False respectivamente.
    """

    input_sin_espacios = input_usuario.replace(" ", "")

    input_limpio = limpiar_texto(input_usuario)

    if not input_sin_espacios.isalpha() or input_usuario.strip() ==  "":
        print(constantes.ERROR_NOMBRE_TALENTO_INVALIDO)
        return False

    if not input_limpio in mapa_talentos:
        print(constantes.ERROR_TALENTO_NO_ENCONTRADO)
        return False

    return True


def validar_csv(archivo_csv: str)-> bool:
    """Dada una ruta verifica si es válida o no."""

    ruta_es_csv = archivo_csv.endswith(constantes.EXTENSION_CSV)

    if not ruta_es_csv:
        return False

    if " " in archivo_csv:
        return False

    partes = []

    if "/" in archivo_csv:
        partes = archivo_csv.split("/")

    elif "\\" in archivo_csv:
        partes = archivo_csv.split("\\")

    else:
        return True

    carpetas = partes[:-1]

    ruta_directorio = carpetas[0]

    for i in range(1, len(carpetas)):
        siguiente_carpeta = carpetas[i]

        ruta_directorio = os.path.join(ruta_directorio, siguiente_carpeta)

    if not os.path.exists(ruta_directorio):
        return False

    return True
