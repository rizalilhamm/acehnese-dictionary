from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from app.admin.views import admin

app = Flask(__name__)
from app.views import acehnese_dictionary_blueprint

app.register_blueprint(admin)
app.register_blueprint(acehnese_dictionary_blueprint)