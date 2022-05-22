from flask import Flask

from app.admin.views import admin
from app.views import acehnese_dictionary

app = Flask(__name__)

app.register_blueprint(admin)
app.register_blueprint(acehnese_dictionary)