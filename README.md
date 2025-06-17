# SAIA
### S.A.I.A. Sistema Administrativo Integral Adaptable

### Paso 1: Estructura de Carpetas y Archivos Iniciales
Cree la siguiente estructura básica de carpetas y archivos. Esto te dará la base para empezar a construir y probar el prototipo desde el día 1.

texto sin formato
saia_prototype/
├── app.py
├── config.py
├── database.py
├── requirements.txt
├── schema.sql
├── routes/
│   ├── __init__.py
│   ├── config.py
│   ├── purchases.py
│   ├── inventory.py
│   ├── accounting.py
│   ├── budget.py
│   └── reports.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── config/
│       ├── coa.html
│       └── add_account.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
### Paso 2: Archivos Mínimos para Iniciar
requirements.txt
TXT
Flask
config.py
Pitón
import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta-prototipo'
    DATABASE = 'saia_prototype.db'
database.py
Pitón
import sqlite3
from flask import g

DATABASE = 'saia_prototype.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def close_db(e=None):
    db = g.pop('_database', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with open('schema.sql', 'r') as f:
        db.executescript(f.read())
    db.commit()

import click
from flask.cli import with_appcontext

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
schema.sql
SQL
DROP TABLE IF EXISTS accounts;
CREATE TABLE accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    type TEXT
);
app.py
Pitón
from flask import Flask, render_template
from config import Config
import database as db

from routes import config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(config.bp, url_prefix='/config')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
routes/__init__.py
Pitón
# deja vacío
routes/config.py
Pitón
from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import get_db

bp = Blueprint('config', __name__)

@bp.route('/coa')
def coa():
    db = get_db()
    accounts = db.execute('SELECT * FROM accounts').fetchall()
    return render_template('config/coa.html', accounts=accounts)

@bp.route('/coa/add', methods=('GET', 'POST'))
def add_account():
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        acc_type = request.form['type']
        db = get_db()
        error = None
        if not code or not name:
            error = 'Código y Nombre requeridos.'
        elif db.execute('SELECT id FROM accounts WHERE code = ?', (code,)).fetchone() is not None:
            error = f'La cuenta con código {code} ya existe.'
        if error is None:
            db.execute('INSERT INTO accounts (code, name, type) VALUES (?, ?, ?)', (code, name, acc_type))
            db.commit()
            flash('Cuenta añadida exitosamente.', 'success')
            return redirect(url_for('config.coa'))
        flash(error, 'danger')
    account_types = ['Activo', 'Pasivo', 'Capital', 'Ingresos', 'Gastos']
    return render_template('config/add_account.html', account_types=account_types)
templates/base.html
HTML
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>{% block title %}SAIA Prototipo{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header>
        <h1>SAIA - Prototipo</h1>
        <nav>
            <a href="{{ url_for('index') }}">Inicio</a> |
            <a href="{{ url_for('config.coa') }}">Configuración</a>
        </nav>
    </header>
    <main>
        {% for message in get_flashed_messages(with_categories=True) %}
            <div class="alert alert-{{ message[0] }}">{{ message[1] }}</div>
        {% endfor %}
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>&copy; 2025 SAIA Prototipo.</p>
    </footer>
</body>
</html>
templates/index.html
HTML
{% extends 'base.html' %}
{% block title %}Inicio - SAIA Prototipo{% endblock %}
{% block content %}
<h2>Bienvenido al Prototipo de SAIA</h2>
<p>Usa el menú para navegar.</p>
{% endblock %}
templates/config/coa.html
HTML
{% extends 'base.html' %}
{% block title %}Plan de Cuentas{% endblock %}
{% block content %}
<h2>Plan de Cuentas Contables</h2>
<a href="{{ url_for('config.add_account') }}" class="button">Añadir Cuenta</a>
<table>
    <tr><th>Código</th><th>Nombre</th><th>Tipo</th></tr>
    {% for account in accounts %}
        <tr>
            <td>{{ account['code'] }}</td>
            <td>{{ account['name'] }}</td>
            <td>{{ account['type'] }}</td>
        </tr>
    {% else %}
        <tr><td colspan="3">No hay cuentas aún.</td></tr>
    {% endfor %}
</table>
{% endblock %}
templates/config/add_account.html
HTML
{% extends 'base.html' %}
{% block title %}Añadir Cuenta{% endblock %}
{% block content %}
<h2>Añadir Cuenta al Plan de Cuentas</h2>
<form method="post">
    <label>Código:</label> <input name="code" required><br>
    <label>Nombre:</label> <input name="name" required><br>
    <label>Tipo:</label>
    <select name="type" required>
        <option value="">--Seleccione--</option>
        {% for acc_type in account_types %}
            <option value="{{ acc_type }}">{{ acc_type }}</option>
        {% endfor %}
    </select><br>
    <button type="submit">Guardar</button>
</form>
<a href="{{ url_for('config.coa') }}">Volver</a>
{% endblock %}
static/css/style.css
CSS
body { font-family: sans-serif; background: #f4f4f4; }
header, footer { background: #0056b3; color: #fff; padding: 10px; text-align: center; }
main { background: #fff; margin: 20px auto; max-width: 800px; padding: 20px; border-radius: 8px; }
nav a { color: #fff; margin: 0 10px; text-decoration: none; }
.button { background: #007bff; color: #fff; padding: 6px 12px; border: none; border-radius: 4px; }
table { width: 100%; border-collapse: collapse; margin-top: 15px; }
th, td { border: 1px solid #ddd; padding: 8px; }
.alert { padding: 8px; margin: 10px 0; border-radius: 4px; }
.alert-success { background: #e1f8e6; color: #205c2f; }
.alert-danger { background: #f8e1e1; color: #a12c2c; }
Paso 3: Instalación y Primer Uso
Instalar Flask:
intento
pip install Flask
Inicializa la base de datos:
intento
flask --app app init-db
Ejecuta la aplicación:
intento
flask --app app run --debug
Abre tu navegador en http://127.0.0.1:5000/.
