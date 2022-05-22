from flask import Blueprint

acehnese_dictionary = Blueprint('acehnese_dictionary', __name__)

@acehnese_dictionary.route('/')
@acehnese_dictionary.route('/home')
def home():
    return "Halaman Home Berisi form input data"