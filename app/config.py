import os
# from flask_mysqldb import MySQL

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASEDIR = os.path.dirname(PROJECT_ROOT)

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'ini-rahasia'
    SQLALCHEMY_DATABASE_URI =  os.getenv("DATABASE_URL") or 'sqlite:///' + os.path.join(BASEDIR, 'aceh_dictionary.db')
    # SQLALCHEMY_DATABASE_URI =  os.getenv("DATABASE_URL") or 'mysql://root:root@localhost/aceh_translate'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') or True