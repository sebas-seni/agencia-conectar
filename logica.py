import os
import constantes
import usuario
import validaciones



def volver_al_menu(input_usuario: str) -> bool:
    """Devuelve True si el usuario ingresa '**'"""

    return input_usuario == constantes.VOLVER_AL_MENU


def crear_diccionario_peliculas(peliculas: dict, nombre_pelicula: str, precio: int, talentos):
    """
    Se crea el diccionario asociado al nombre de una pelicula,
    cuyos valores son el precio y los talentos de la película
    """

    peliculas[nombre_pelicula] = {
        "precio": precio,
        "talentos": talentos
    }

    return peliculas


def validar_rutas(ruta: str) -> list:
    """
    Dada una ruta verifica si es válida o no. Si es una carpeta, la explora recursivamente,
    sino chequea la extension del archivo.
    Devuelve una lista con las rutas de los archivos encontrados

    POST-CONDICIONES:
        - 'lista_csvs' contiene rutas a archivos CSV o se devuelve una lista vacía si las rutas no son válidas
        o se quiere volver al menú principal.
    """

    ruta_es_directorio = os.path.isdir(ruta)

    ruta_existe = os.path.exists(ruta)

    ruta_es_csv = ruta.endswith(constantes.EXTENSION_CSV)

    if not ruta_existe:
        return []

    if " " in ruta:
        return []

    if not ruta_es_directorio and ruta_existe:

        if ruta_es_csv:
            return [ruta]

        return []

    contenido_ruta = os.listdir(ruta)

    lista_csvs = []

    for contenido in contenido_ruta:
        lista_csvs += validar_rutas(os.path.join(ruta, contenido))

    return lista_csvs

def crear_clave_pelicula(rutas_validas: list, peliculas: dict)-> int:
    """
    Recorre la/s ruta/s previamente validada/s y crea la base de datos con los datos brindados. Devuelve
    la cantidad de peliculas agregadas correctamente.

    PRE-CONDICIONES:
        - 'rutas_validas' contiene carpetas o archivos existentes y válidos.

    POST-CONDICIONES:
        - 'peliculas' es un diccionario donde el nombre de la pelicula es la clave y los valores son el precio
        y los talentos involucrados en la película.

        - 'cant_peliculas' contiene la cantidad de peliculas agregadas correctamente.
    """

    cant_peliculas = 0

    for ruta_archivo in rutas_validas:

        with open(ruta_archivo, "r", encoding="utf-8") as archivo:

            next(archivo, None)

            for linea in archivo:
                linea = linea.strip()

                if not linea:
                    continue

                nombre_pelicula, precio, talentos = linea.split(",")

                if nombre_pelicula in peliculas:
                    print(constantes.PELICULA_DUPLICADA, nombre_pelicula)
                    continue

                crear_diccionario_peliculas(peliculas,nombre_pelicula, precio, talentos)

                cant_peliculas += 1

    return cant_peliculas


def crear_clave_ventas(rutas_validas: list, peliculas: dict)-> int:
    """
    Dada una o varias rutas que contienen informacion sobre las entradas vendidas de una pelicula
    y el diccionario con todas las peliculas, se leen los registros de ventas y se asignan
    la cantidad de entradas vendidas a cada pelicula registrada.
    Se devuelve la cantidad de registros agregados correctamente.

    PRE-CONDICIONES:
        - 'rutas_validas' contiene carpetas o archivos existentes y válidos.
        - 'peliculas' contiene todas las peliculas con su nombre, precio y talentos involuctados.

    POST-CONDICIONES:
        'peliculas[nombre_pelicula]' contiene una nueva clave con la cantidad de entradas vendidas.
        'cant_registros_ventas' contiene la cantidad de reigstros agregados correctamente.
    """

    cant_registros_ventas = 0

    for ruta_archivo in rutas_validas:

        with open(ruta_archivo, "r", encoding="utf-8") as archivo:

            next(archivo, None)

            for linea in archivo:
                linea = linea.strip()

                if not linea:
                    continue

                nombre_pelicula, cant_entradas_vendidas = linea.split(",")

                if nombre_pelicula not in peliculas:
                    print(constantes.PELICULA_INEXISTENTE, nombre_pelicula)
                    continue

                pelicula = peliculas[nombre_pelicula]

                entradas_viejas = int(pelicula.get("entradas_vendidas", 0))

                pelicula["entradas_vendidas"] = entradas_viejas + int(cant_entradas_vendidas)

                cant_registros_ventas += 1

    return cant_registros_ventas


def listar_rutas_validas(rutas_individuales: list)-> list:
    """Dada una lista de rutas, valida una por una y las acumula en una lista nueva.

    PRE-CONDICIONES:
        -'rutas_individuales' es una lista con rutas ingresadas por el usuario.

    POST-CONDICIONES:
        - 'rutas_validas' es una lista con todas las rutas de archivos CSV encontrados y válidos.
    """

    rutas_validas = []

    for ruta in rutas_individuales:
        rutas_validas += validar_rutas(ruta)

    return rutas_validas


def devolver_rutas_validadas(mensaje_input: str)-> list:
    """
    Pide al usuario que ingrese una o mas rutas, verifica la existencia de las mismas y gestiona los casos de error.
    Si la validación es válida, delega la busqueda de archivos CSV

    POST-CONDICIONES:

    """

    while True:

        input_usuario = input(mensaje_input)

        if volver_al_menu(input_usuario):
            return None

        rutas_individuales = input_usuario.split()

        todas_las_rutas_existen = True

        for ruta in rutas_individuales:

            if not os.path.exists(ruta):
                todas_las_rutas_existen = False
                break

            if not os.path.isdir(ruta) and not ruta.endswith(constantes.EXTENSION_CSV):
                todas_las_rutas_existen = False
                break

        if todas_las_rutas_existen:
            break


        print(constantes.ERROR_IMPORTACION)

    listado_rutas_validas = listar_rutas_validas(rutas_individuales)

    return listado_rutas_validas


def cargar_peliculas(peliculas: dict):
    """
    Dada una o más rutas válidas, carga las películas con las claves correspondientes en la base de datos y
    se imprime la cantidad de películas cargardas correctamente.

    POST-CONDICIONES:
        -' peliculas_cargadas' contiene la cantidad de peliculas que se agregaron correctamente.
    """

    rutas_validadas = devolver_rutas_validadas(constantes.MSG_PELICULAS)

    if rutas_validadas is None:

        return

    peliculas_cargadas = crear_clave_pelicula(rutas_validadas, peliculas)
    print("OK", peliculas_cargadas)


def cargar_info_ventas(peliculas: dict):
    """
    Dadas las rutas ya validadas, se cargan las ventas en la base de datos.
    Se imprimen la cantidad de registros de ventas cargados correctamente.

    PRE-CONDCIIONES:
        - 'peliculas' contiene todos los datos de cada película.

    POST-CONDICIONES:
        - Se actualiza el diccionario 'peliculas' con los datos de las entradas vendidas.
    """

    rutas_validadas = devolver_rutas_validadas(constantes.MSG_VENTAS)

    if rutas_validadas is None:
        return

    ventas_cargadas = crear_clave_ventas(rutas_validadas, peliculas)

    print("OK", ventas_cargadas)




def normalizar_talentos(peliculas: dict)-> dict:
    """
    Normaliza todos los talentos de las películas cargadas. Devuelve un diccionario
    con los nombres normalizados y sus nombres originales.

    PRE-CONDICIONES:
        - La base de datos con las películas debe estar correctamente cargada.
    """

    mapa_talentos = {}

    for _pelicula, datos_pelicula in peliculas.items():

        talentos = datos_pelicula["talentos"].split(";")

        for talento_original in talentos:
            clave_limpia = validaciones.limpiar_texto(talento_original)

            mapa_talentos[clave_limpia] = talento_original

    return mapa_talentos


def encontrar_colabs_de_un_talento(peliculas: dict, nombre_talento: str)-> set:
    """
    Encuentra los colaboradores directos de un talento específico, basandose en las películas cargadas.

    PRE-CONDICIONES:
        - La base de datos con las películas debe estar correctamente cargada.

    """

    colaboraciones_directas = set()


    for _pelicula, datos_pelicula in peliculas.items():

        talentos_pelicula = datos_pelicula["talentos"].split(";")
        talentos_minuscula_temporal = [t.lower() for t in talentos_pelicula]

        if not nombre_talento.lower() in talentos_minuscula_temporal:
            continue

        for talento_original in talentos_pelicula:

            if talento_original.lower() == nombre_talento.lower():
                continue

            colaboraciones_directas.add(talento_original)

    return colaboraciones_directas


def obtener_talento_validado(peliculas: dict)-> str:
    """
    Pide el nombre de un talento al usuario y lo valida. Devuelve el nombre tal cual aparece en el diccionario
    de peliculas.

    PRE-CONDICIONES:
        - La base de datos con las películas debe estar correctamente cargada.
    """

    mapa_talentos = normalizar_talentos(peliculas)

    while True:
        input_usuario = usuario.pedir_talento()

        if volver_al_menu(input_usuario):
            return None

        if not validaciones.es_talento_valido(input_usuario, mapa_talentos):
            continue

        break

    input_limpio = validaciones.limpiar_texto(input_usuario)
    nombre_real = mapa_talentos[input_limpio]

    return nombre_real


def encontrar_colabs_directas(peliculas: dict)-> set:
    """
    Dado un nombre sin normalizar brindado por el usuario, se devuelven sus colaboradores directos.

    PRE-CONDICIONES:
        - La base de datos con las películas debe estar correctamente cargada.

    """

    nombre_real = obtener_talento_validado(peliculas)

    if nombre_real is None:
        return None

    colaboradores = encontrar_colabs_de_un_talento(peliculas, nombre_real)

    return colaboradores


def ordenar_alfabeticamente(coleccion: set)-> list:
    "Ordena alfabeticamente los talentos de un set y los devuelve en formato lista."

    return sorted(list(coleccion))


def imprimir_colabs_directas(peliculas: dict):
    """
    Dado un set de colaboraciones directas, se ordenan alfabeticamente y se imprimen de manera numerada.
    Si el set esta vacio se imprime el mensaje 'No existen colaboradores directos para el talento ingresado'.


    PRE-CONDICIONES:
        - La base de datos con las películas debe estar correctamente cargada.
    """

    set_colabs_directas = encontrar_colabs_directas(peliculas)

    if set_colabs_directas is None:
        return

    talentos_ordenados = ordenar_alfabeticamente(set_colabs_directas)

    if talentos_ordenados == []:
        print(constantes.COLABORADORES_DIRECTOS_INEXISTENTES)
        return

    print(constantes.COLABORADORES_DIRECTOS)
    for i, talento in enumerate(talentos_ordenados, start=1):
        print(f"{i}. {talento}")


def encontrar_conexiones_recursivo(peliculas: dict, talento_actual: str, visitados: set):
    """
    Explora todas las colaboraciones de un talento específico para encontrar todos los talentos conectados

    PRE-CONDICIONES:
        - La base de datos con las películas debe estar correctamente cargada.
        - 'talento_actual' es un talento válido
    """


    visitados.add(talento_actual)

    colaboradores_directos = encontrar_colabs_de_un_talento(peliculas, talento_actual)

    for colaborador_directo in colaboradores_directos:

        if not colaborador_directo in visitados:
            encontrar_conexiones_recursivo(peliculas, colaborador_directo, visitados)


def filtrar_solo_compatibles(peliculas: dict)-> set:
    """
    Procesa todos los talentos y los filtra para quedarse solo con los compatibles.
    Devuelve el set con todos los talentos compatibles.

    PRE-CONDICIONES:
        - La base de datos con las películas debe estar correctamente cargada.
    """
    nombre_real = obtener_talento_validado(peliculas)

    if nombre_real is None:
        return None

    visitados = set()

    encontrar_conexiones_recursivo(peliculas, nombre_real, visitados)

    colabs_directas = encontrar_colabs_de_un_talento(peliculas, nombre_real)

    compatibles = visitados - colabs_directas - {nombre_real}

    return compatibles


def imprimir_talentos_compatibles(peliculas: dict):
    """
    Ordena los talentos compatibles alfabéticamente y los imprime de forma numerada. Si no hay compatibles se
    imprime el mensaje: 'No existen talentos compatibles para el talento ingresado'.

    PRE-CONDICIONES:
        - La base de datos con las películas debe estar correctamente cargada.
    """

    set_colabs_compatibles= filtrar_solo_compatibles(peliculas)

    if set_colabs_compatibles is None:
        return

    talentos_ordenados = ordenar_alfabeticamente(set_colabs_compatibles)

    if talentos_ordenados == []:
        print(constantes.TALENTOS_COMPATIBLES_INEXISTENTES)
        return

    print(constantes.TALENTOS_COMPATIBLES)
    for i, talento in enumerate(talentos_ordenados, start=1):
        print(f"{i}. {talento}")


def filtrar_solo_incompatibles(peliculas: dict)-> set:
    """
    Procesa todos los talentos y los filtra para quedarse solo con los incompatibles.
    Devuelve el set con todos los talentos incompatibles.

    PRE-CONDICIONES:
        - La base de datos con las películas debe estar correctamente cargada.
    """

    nombre_real = obtener_talento_validado(peliculas)

    if nombre_real is None:
        return None

    mapa_talentos = normalizar_talentos(peliculas)

    talentos_peliculas = set(mapa_talentos.values())

    conectados = set()
    encontrar_conexiones_recursivo(peliculas, nombre_real, conectados)

    incompatibles = talentos_peliculas - conectados

    return incompatibles



def imprimir_talentos_incompatibles(peliculas: dict):

    set_colabs_incompatibles = filtrar_solo_incompatibles(peliculas)

    if set_colabs_incompatibles is None:
        return

    talentos_ordenados = ordenar_alfabeticamente(set_colabs_incompatibles)

    if talentos_ordenados == []:
        print(constantes.TALENTOS_INCOMPATIBLES_INEXISTENTES)
        return

    print(constantes.TALENTOS_INCOMPATIBLES)
    for i, talento in enumerate(talentos_ordenados, start=1):
        print(f"{i}. {talento}")


def calcular_recaudaciones(peliculas: dict)-> dict:
    """
    Calcula y devuelve la recaudacion de cada talento segun las entradas vendidas de sus películas
    y se agrega el monto al diccionario de las recaudaciones.

    PRE-CONDICIONES:
        - La base de datos con las películas debe estar correctamente cargada.

    POST-CONDICIONES:
        - Se crea un diccionario que tiene al nombre del talento como clave
        y al monto que vendio una película como valor.
    """


    recaudacion_por_actor = {}

    for _pelicula, datos_pelicula in peliculas.items():

        talentos_pelicula = datos_pelicula["talentos"].split(";")

        precio = int(datos_pelicula["precio"])

        cant_entradas_vendidas = int(datos_pelicula.get("entradas_vendidas", 0))

        monto_pelicula = precio * cant_entradas_vendidas

        for talento in talentos_pelicula:

            if not talento in recaudacion_por_actor:

                recaudacion_por_actor[talento] = monto_pelicula
            else:
                recaudacion_por_actor[talento] += monto_pelicula

    return recaudacion_por_actor


def exportar_recaudaciones(peliculas: dict)-> str:
    """
    Genera y guarda un archivo CSV con el ranking de recaudación de todos los talentos registrados.
    Devuelve el nombre del archivo junto con la lista que contiene las recaudaciones de cada actor.

    PRE-CONDICIONES:
        - La base de datos con las películas debe estar correctamente cargada.

    POST-CONDICIONES:
        - Se crea un archivo CSV con el nombre proveído por el usuario que contiene el ranking de recaudaciones.
    """

    while True:
        archivo_csv = input("Ingrese la ruta del archivo a guardar: ")

        if volver_al_menu(archivo_csv):
            return None

        es_ruta_valida = validaciones.validar_csv(archivo_csv)

        if not es_ruta_valida:
            print(constantes.ERROR_EXPORTACION)
            continue

        break

    recaudaciones_por_actor = calcular_recaudaciones(peliculas)

    lista_entradas_vendidas = list(recaudaciones_por_actor.items())

    lista_ordenada = ordenar_recaudaciones(lista_entradas_vendidas)

    escribir_csv(archivo_csv, lista_ordenada)

    print("OK")

    return archivo_csv, lista_entradas_vendidas


def obtener_clave_ordenamiento(tupla_actor: tuple)-> tuple:
    """Recibe una tupla y devuelve otra transformada para el ordenamiento"""

    nombre_actor = tupla_actor[0]

    recaudacion_actor = tupla_actor[1]

    recaudacion_negativa = -recaudacion_actor

    return (recaudacion_negativa, nombre_actor)


def ordenar_recaudaciones(lista_recaudaciones: list)-> list:
    """
    Recibe una lista que contiene el nombre de los actores junto con su recaudación y las ordena de manera
    descendente según la recaudación. Si coinciden dos talentos en recaudación se ordenan alfabéticamente.
    """

    recaudaciones_ordenadas = sorted(lista_recaudaciones, key=obtener_clave_ordenamiento)

    return recaudaciones_ordenadas

def escribir_csv(ruta_archivo: str, recaudaciones_ordenadas: list):
    """
    Escribe en un archivo CSV a los talentos que mas recaudaron.

    PRE-CONDICIONES:
        - 'ruta_archivo' es una ruta que contiene un archivo CSV válido.

    POST-CONDICIONES:
        - Se crea un archivo CSV que contiene a los talentos y al dinero recaudado por cada uno
    """

    with open(ruta_archivo, "w", encoding="utf-8") as archivo:

        archivo.write("actor,recaudacion\n")

        for actor, recaudacion in recaudaciones_ordenadas:
            linea = f"{actor},{recaudacion}"
            archivo.write(f"{linea}\n")
