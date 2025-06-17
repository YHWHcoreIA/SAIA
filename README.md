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

pasos generales para desplegar la aplicación SAIA en la nube usando Heroku, Render o Railway:

Despliegue en Heroku
Crear una cuenta en Heroku:

Regístrate en Heroku.
Instalar Heroku CLI:

Descarga e instala el Heroku CLI.
Iniciar sesión en Heroku:

Copiar
heroku login
Preparar la aplicación:

Asegúrate de que tu aplicación tenga un archivo requirements.txt y un Procfile.
requirements.txt debe listar todas las dependencias de tu aplicación.
Procfile debe contener lo siguiente:
Copiar
web: python app.py
Crear una nueva aplicación en Heroku:

Copiar
heroku create nombre-de-tu-aplicacion
Subir la aplicación a Heroku:

Copiar
git add .
git commit -m "Despliegue inicial"
git push heroku master
Configurar la base de datos (si es necesario):

Usa el addon de PostgreSQL o SQLite según lo necesites.
Abrir la aplicación:

Copiar
heroku open
Despliegue en Render
Crear una cuenta en Render:

Regístrate en Render.
Conectar tu repositorio:

En el panel de Render, elige "New Web Service" y conecta tu repositorio de GitHub.
Configurar el servicio:

Selecciona el branch que deseas desplegar.
Configura el entorno (Python) y el comando de inicio:
Copiar
python app.py
Configurar variables de entorno:

Añade las variables necesarias en la sección de configuración.
Desplegar:

Render automáticamente desplegará tu aplicación cuando hagas un push al repositorio.
Despliegue en Railway
Crear una cuenta en Railway:

Regístrate en Railway.
Crear un nuevo proyecto:

Selecciona "New Project" y elige "Deploy from GitHub".
Conectar tu repositorio:

Selecciona el repositorio que contiene tu aplicación.
Configurar el entorno:

Asegúrate de que el entorno esté configurado para Python y añade el comando de inicio.
Configurar variables de entorno:

Añade las variables necesarias en la sección de configuración.
Desplegar:

Railway desplegará automáticamente tu aplicación.
Notas Adicionales
Asegúrate de tener configurados los archivos necesarios (requirements.txt, Procfile) y de que tu aplicación sea compatible con el entorno de producción.
Revisa la documentación específica de cada plataforma para detalles adicionales y configuraciones avanzadas.
