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