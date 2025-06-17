## Ejemplo de pruebas de rutas/blueprints con base de datos

- Usa pytest y los fixtures de Flask para crear una base de datos en memoria en cada test.
- Los tests pueden hacer POST y GET a rutas reales y verificar la respuesta y la base de datos.
- Puedes usar `client.post` para simular formularios y verificar que los datos se guardan.
- Usa fixtures como `preloaded_db` para poblar la base antes de los tests.

Para correr los tests:

```bash
pytest
```