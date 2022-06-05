from flask import Blueprint, request, render_template
from fast_autocomplete import AutoComplete

from app.models import Vocabularies

acehnese_dictionary_blueprint = Blueprint('acehnese_dictionary_blueprint', __name__)

@acehnese_dictionary_blueprint.route('/')
@acehnese_dictionary_blueprint.route('/home')
def home():
    return "Halaman Home Berisi form input data yang diinginkan"


@acehnese_dictionary_blueprint.route('/search')
@acehnese_dictionary_blueprint.route('/search?language=aceh-indonesia')
def search_data():
    if request.method == 'GET':
        alldata = Vocabularies.query.all()
        searched_word = request.args.get('language')
        words = {}
        for data in alldata:
            words[str(data.real_aceh)] = {}
        
        if searched_word == 'indonesia-aceh':
            words = {}
            for data in alldata:
                words[str(data.indonesia)] = {}

        auto_complete = AutoComplete(words=words)
        auto_complete.search(word=searched_word, max_cost=3, size=3)
        return render_template('search_vocabulary.html', languages=words, search_type=searched_word)
