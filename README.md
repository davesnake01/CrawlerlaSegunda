# CrawlerlaSegunda

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

`CrawlerlaSegunda` es un web scraper / crawler automatizado desarrollado en Python, diseñado específicamente para la extracción estructurada de datos, noticias o publicaciones periódicas (enfocado en plataformas informativas o de prensa como La Segunda). 

El proyecto recopila, procesa y almacena la información de manera local tanto en formatos estructurados ligeros (JSON) como en sistemas de bases de datos relacionales para su posterior análisis o consumo.

## 🛠️ Arquitectura y Estructura del Proyecto

El repositorio se compone de los siguientes módulos clave:

```text
├── database.py       # Gestión de la conexión y persistencia en la Base de Datos.
├── lasegunda.json    # Almacenamiento local / caché de los datos extraídos en formato JSON.
├── main.py           # Orquestador principal, lógica del crawler y scraping.
├── requirements.txt  # Dependencias y librerías necesarias del proyecto.
└── .idea/            # Configuraciones del entorno de desarrollo (PyCharm).
