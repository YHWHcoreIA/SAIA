# SAIA Prototype

## Despliegue Local

1. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Inicializa la base de datos:
   ```bash
   flask --app app init-db
   ```
3. Ejecuta el servidor:
   ```bash
   flask --app app run
   ```

## Despliegue en Heroku/Render/Railway

- Sube el repo a GitHub.
- Asegúrate de tener `Procfile`, `requirements.txt`, `wsgi.py`.
- Configura variables de entorno: `SECRET_KEY`, `DATABASE_URL` (opcional), `UPLOAD_FOLDER` (opcional).
- Para inicializar la base de datos, ejecuta el comando `flask --app app init-db` desde el terminal de tu servicio en la nube.

---

## SAIA (Sistema Administrativo Integral Adaptable) 
es un prototipo de aplicación web desarrollada con Python y Flask. Proporciona una estructura básica para construir una aplicación web con funcionalidades administrativas y de gestión de datos.

## Puntos Principales de Funcionalidad
### Inicialización de una base de datos SQLite
### Configuración de variables de entorno para el despliegue en la nube
### Estructura de archivos y carpetas para una aplicación Flask

Requisitos Previos
Python: Asegúrate de tener Python instalado (preferiblemente Python 3.6 o superior).
Pip: Necesitarás pip para instalar las dependencias.
Pasos para el Despliegue Local
Clonar el Repositorio:
Abre tu terminal y clona el repositorio:

Copiar
git clone https://github.com/YHWHcoreIA/SAIA.git
cd SAIA
Crear un Entorno Virtual (opcional pero recomendado):

Copiar
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
Instalar Dependencias:
Instala las librerías necesarias con pip:

Copiar
pip install -r requirements.txt
Configurar la Base de Datos:
Asegúrate de que la base de datos SQLite esté configurada correctamente. Puede que necesites ejecutar un script para inicializarla.

Configurar Variables de Entorno:
Si hay variables de entorno necesarias, configúralas en un archivo .env en la raíz del proyecto.

Ejecutar la Aplicación:
Finalmente, ejecuta la aplicación:

Copiar
python app.py  # O el nombre del archivo principal de la aplicación
Acceder a la Aplicación:
Abre tu navegador y ve a http://127.0.0.1:5000/ (o el puerto que esté configurado).

Notas Adicionales
Revisa la documentación del proyecto en el repositorio para detalles específicos sobre la configuración y cualquier otro paso necesario.
Asegúrate de que todas las dependencias estén correctamente instaladas y de que no haya errores en la consola.

## Pila Tecnológica
### Python
### Flask
### SQLite
### Heroku/Render/Railway (para despliegue en la nube)
