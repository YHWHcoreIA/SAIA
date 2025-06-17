import os
from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

# Importa y registra tus blueprints aquí

@app.route("/")
def index():
    return "SAIA Prototipo con SQLAlchemy y Alembic"

if __name__ == "__main__":
    app.run(debug=True)