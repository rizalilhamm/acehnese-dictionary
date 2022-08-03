from flask import Blueprint, request, render_template
from fast_autocomplete import AutoComplete
from render_all_data import get_all_data

from app.models import Vocabularies

acehnese_dictionary_blueprint = Blueprint('acehnese_dictionary_blueprint', __name__)

@acehnese_dictionary_blueprint.route('/')
@acehnese_dictionary_blueprint.route('/home')
def home():
    return "Halaman Home Berisi form input data yang diinginkan"


@acehnese_dictionary_blueprint.route('/search')
@acehnese_dictionary_blueprint.route('/search?language=aceh-indonesia')
def search_data():
    semua_kosakata = get_all_data()

    if request.method == 'GET':
        searched_word = request.args.get('language')
        words = {}

        if searched_word == 'indonesia-aceh':
            semua_kosakata_indonesia = semua_kosakata['semua_kosakata_indonesia']
            print('nilai semua kosakata indonesia', semua_kosakata_indonesia)
            for kosakata_indonesia in semua_kosakata_indonesia:
                words[kosakata_indonesia] = {}
        
        elif not searched_word or searched_word == 'aceh-indonesia':
            semua_kosakata_aceh = semua_kosakata['semua_kosakata_aceh']
            print('nilai semua kosakata aceh', semua_kosakata_aceh)
            for kosakata_aceh in semua_kosakata_aceh:
                words[kosakata_aceh] = {}

        auto_complete = AutoComplete(words=words)
        auto_complete.search(word=searched_word, max_cost=3, size=3)
        return render_template('search_vocabulary.html', languages=words, search_type=searched_word)
