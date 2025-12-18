# 🎬 Agencia Conectar - Análisis de Conexiones de Talentos

Este proyecto es una aplicación de consola desarrollada en **Python** para gestionar la información de una agencia de talentos de cine. El sistema permite cargar grandes volúmenes de datos, establecer relaciones complejas entre actores y generar reportes de negocio.

## 🚀 Características Principales

El núcleo del proyecto se basa en el procesamiento de archivos y algoritmos de búsqueda:

* **Procesamiento de Datos ETL:** Ingesta y validación robusta de archivos CSV (Películas y Ventas), soportando carga recursiva de directorios.
* **Análisis de Grafos (Networking):**
    * Detecta **Colaboradores Directos** (actores que trabajaron juntos).
    * Utiliza **Algoritmos Recursivos** para encontrar conexiones indirectas (Talentos Compatibles).
    * Identifica islas de datos desconectadas (Talentos Incompatibles).
* **Inteligencia de Negocio:** Cálculo de recaudación histórica por actor y exportación de rankings ordenados por criterios múltiples.
* **UX/UI en Consola:** Menú interactivo con validaciones estrictas de entrada de usuario y manejo de errores.

## 🛠️ Tecnologías y Conceptos Aplicados

Este proyecto fue construido utilizando **Python puro (Vanilla Python)** sin librerías externas de análisis de datos, para demostrar una comprensión profunda de las estructuras de datos y algoritmos:

* **Estructuras de Datos:** Uso intensivo de `diccionarios` para indexación rápida, `sets` para operaciones de conjuntos (intersección/diferencia) y grafos.
* **Algoritmos:** Implementación de **recursividad** (DFS/BFS logic) para recorrer la red de conexiones entre actores.
* **Modularización:** Arquitectura separada en capas:
    * `logica.py`: Reglas de negocio y algoritmos.
    * `validaciones.py`: Sanitización y chequeos de integridad.
    * `usuario.py`: Capa de interacción.
    * `conectar.py`: Controlador principal.
* **Manejo de Archivos:** Lectura/Escritura eficiente de CSVs y navegación del sistema de archivos con `os`.

## 📋 Pre-requisitos

* Python 3.x

## 🔧 Cómo ejecutarlo

1.  Clona el repositorio.
2.  Ejecuta el archivo principal:
    ```bash
    python conectar.py
    ```
3.  Sigue las instrucciones del menú para cargar los archivos CSV de prueba (ubicados en la carpeta `/datasets` o similar).

## autor
[Sebastián Senillosa / Linkedin: www.linkedin.com/in/sebastián-senillosa-5548391a1]
