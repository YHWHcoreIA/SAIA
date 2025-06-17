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
## Pila Tecnológica
### Python
### Flask
### SQLite
### Heroku/Render/Railway (para despliegue en la nube)
