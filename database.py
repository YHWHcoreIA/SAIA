from flask import g, current_app
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = None
SessionLocal = None

def init_engine():
    global engine, SessionLocal
    if engine is None:
        database_url = current_app.config['DATABASE_URL']
        engine = create_engine(database_url, future=True)
        SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    if 'db' not in g:
        init_engine()
        g.db = SessionLocal()
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    init_engine()
    with engine.connect() as conn:
        with open('schema.sql', 'r') as f:
            conn.execute(text(f.read()))

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