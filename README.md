# Proyecto de Reporte de Bicicletas 🚲

Este proyecto permite crear una base de datos en MongoDB para almacenar y visualizar datos de ventas de bicicletas, con herramientas de análisis y visualización de datos como `pandas`, `matplotlib`, `plotly`, `bokeh`, y `seaborn`. Utiliza `Flask` como servidor web para mostrar reportes interactivos.

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Requisitos

Asegúrate de tener instalado:
- [Python 3.8+](https://www.python.org/downloads/)
- [MongoDB](https://www.mongodb.com/try/download/community) (local o en la nube)
- [Git](https://git-scm.com/)

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio


## Crea y activa un entorno virtual:

python -m venv venv

## Actívalo

# En Windows
.\venv\Scripts\Activate

# En macOS/Linux
source venv/bin/activate


# Instala las dependencias:

pip install -r requirements.txt


# Configuración
**Base de Datos en MongoDB**
**1 Abre la terminal de MongoDB y crea la base de datos:**

mongo
use dbReporteBicicleta

**2 Crea la colección:**
db.createCollection('VentasBicicleta')

**3 Importa los datos desde un archivo CSV**
mongoimport --db dbReporteBicicleta --collection VentasBicicleta --type CSV --file C:\ProyectoBicicleta\DataBicicleta.csv --headerline


# Uso
**Ejecuta la aplicación:**

Asegúrate de tener el entorno virtual activado y luego inicia el servidor:

python app.py


**También puedes ejecutar la aplicación con Flask:**
flask run


Accede a la interfaz web:

Abre tu navegador y dirígete a http://127.0.0.1:5000 para interactuar con la aplicación.


# Estructura del Proyecto

ProyectoBicicleta/
├── venv/               # Entorno virtual (agregado en .gitignore)
├── DataBicicleta.csv   # Archivo CSV con los datos de ventas
├── app.py              # Archivo principal de la aplicación
├── requirements.txt    # Archivo de dependencias
├── README.md           # Este archivo
└── templates/          # Plantillas HTML para la aplicación Flask




¡Este es tu archivo `README.md` completo y listo para usar!
