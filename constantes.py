"""Constantes de Agencia Conectar."""

MSG_MENU = """1) Cargar películas
2) Cargar información de ventas
3) Listar colaboraciones directas
4) Listar talentos compatibles
5) Listar talentos incompatibles
6) Exportar talentos con mayor recaudacion
7) Salir
"""
SALIR = 7
VOLVER_AL_MENU = "**"
EXTENSION_CSV = ".csv"
MSG_PELICULAS = "Ingrese el archivo de películas a cargar: "
MSG_VENTAS = "Ingrese el archivo de ventas a cargar: "
MSG_TALENTO = "Ingrese el nombre de un talento: "
MSG_COLABORADORES_DIRECTOS = "Colaboradores directos: "
ERROR_IMPORTACION = "El/los archivos a importar deben existir y ser CSV válidos"
ERROR_EXPORTACION = "Error en la exportación"
ERROR_TALENTO_NO_ENCONTRADO = "Talento no existente"
ERROR_NOMBRE_TALENTO_INVALIDO = (
    "El nombre ingresado no debe estar vacío y debe estar compuesto por caracteres "
    "alfabéticos"
)

TALENTOS_INCOMPATIBLES_INEXISTENTES = (
    "No existen talentos incompatibles para el talento ingresado"
)
TALENTOS_COMPATIBLES_INEXISTENTES = (
    "No existen talentos compatibles para el talento ingresado"
)
COLABORADORES_DIRECTOS_INEXISTENTES = (
    "No existen colaboradores directos para el talento ingresado"
)
OPCION_INVALIDA = "Seleccione una opción válida"

PELICULA_DUPLICADA = "Ignorando película duplicada:"
PELICULA_INEXISTENTE = "Ignorando película inexistente:"
COLABORADORES_DIRECTOS = "Colaboradores directos:"
TALENTOS_COMPATIBLES = "Talentos compatibles:"
TALENTOS_INCOMPATIBLES = "Talentos incompatibles:"
