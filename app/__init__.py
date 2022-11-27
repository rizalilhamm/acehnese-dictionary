from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_mysqldb import MySQL

from app.admin.views import admin
# from app.views import acehnese_dictionary_blueprint
from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login_admin'
from app.views import acehnese_dictionary_blueprint

app.register_blueprint(admin)
app.register_blueprint(acehnese_dictionary_blueprint)