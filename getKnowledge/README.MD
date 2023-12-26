# Get Knowledge

## Descripción
La sección "Get Knowledge" contiene dos scripts de Python enfocados en la extracción, almacenamiento y presentación de enlaces web. Utilizan técnicas de web scraping y manejo de bases de datos SQLite para organizar y presentar información de sitios web específicos.

## Scripts Incluidos

### 1. Programa de Extracción y Almacenamiento de Enlaces Web
Este script utiliza `requests` y `BeautifulSoup` para raspar enlaces desde una URL específica y los almacena en una base de datos SQLite.

**Funcionalidades Principales:**
- Creación de una base de datos SQLite para almacenar enlaces.
- Extracción de enlaces web de manera recursiva hasta un nivel de profundidad definido.
- Almacenamiento de enlaces en la base de datos con información sobre su nivel de profundidad.

### 2. Generador de Páginas HTML a partir de Enlaces Almacenados
Este script recorre la base de datos de enlaces y genera un archivo HTML con el contenido de cada página web enlazada.

**Funcionalidades Principales:**
- Recuperación de enlaces almacenados en la base de datos SQLite.
- Generación de un archivo HTML que incluye el contenido de cada página web referenciada por los enlaces.

## Requisitos
- Python 3
- Paquetes: `requests`, `BeautifulSoup`, `sqlite3`
  - Instalación: `pip install requests beautifulsoup4`

## Instalación y Ejecución
1. Clona el repositorio.
2. Instala las dependencias requeridas.
3. Ejecuta los scripts:
   - `python script_extraccion_enlaces.py`
   - `python script_generador_html.py`

## Uso
- Asegúrate de tener acceso a Internet para la extracción de enlaces y la generación de contenido HTML.
- Configura la URL objetivo y la base de datos SQLite según tus necesidades antes de ejecutar los scripts.

## Advertencias
- Estos scripts están diseñados para fines educativos y de demostración. Se recomienda verificar la legalidad del web scraping en tu jurisdicción antes de su uso.
- Verifica los permisos y la seguridad al conectarte a sitios web y manejar bases de datos.

## Contribuciones
Las contribuciones para mejorar los scripts y su documentación son bienvenidas. Por favor, envía tus pull requests a la rama principal.

## Licencia
Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

---

Desarrollado con ❤️ por [b2p5]
