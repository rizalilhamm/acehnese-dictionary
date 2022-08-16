from crypt import methods
from unittest import result
from flask import Blueprint, request, render_template
from fast_autocomplete import AutoComplete
from render_all_data import get_all_data
from calculate_distance import calcDictDistance

acehnese_dictionary_blueprint = Blueprint('acehnese_dictionary_blueprint', __name__)

@acehnese_dictionary_blueprint.route('/')
@acehnese_dictionary_blueprint.route('/home')
def home():
    return "Halaman Home Berisi form input data yang diinginkan"


@acehnese_dictionary_blueprint.route('/search/aceh-indonesia', methods=["GET", "POST"])
def search_data_aceh_indonesia():
    semua_kosakata = {}

    if request.method == 'POST':
        word = request.form.get('word').lower() or "".lower()

        if len(word.replace(" ", "")) == 0:
            return render_template("search_vocabulary_aceh_indonesia.html")
        semua_kosakata = calcDictDistance(word=word, numWords=10, search_type='aceh_indonesia')


        words = {}

        for kosakata_aceh in semua_kosakata:
            words[kosakata_aceh.capitalize()] = {}

        return render_template('search_vocabulary_aceh_indonesia.html', semua_kosakata=semua_kosakata, word=word)
    return render_template('search_vocabulary_aceh_indonesia.html')


@acehnese_dictionary_blueprint.route('/search/indonesia-aceh', methods=["GET", "POST"])
def search_data_indonesia_aceh():
    semua_kosakata = {}

    if request.method == 'POST':
        word = request.form.get('word').lower() or "".lower()

        if len(word.replace(" ", "")) == 0:
            return render_template("search_vocabulary_indonesia_aceh.html")
        semua_kosakata = calcDictDistance(word=word, numWords=10, search_type='indonesia_aceh')


        words = {}

        for kosakata_aceh in semua_kosakata:
            words[kosakata_aceh.capitalize()] = {}

        return render_template('search_vocabulary_indonesia_aceh.html', semua_kosakata=semua_kosakata, word=word)
    return render_template('search_vocabulary_indonesia_aceh.html')