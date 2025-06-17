import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta-prototipo'
    DATABASE = os.environ.get('DATABASE_URL') or 'saia_prototype.db'