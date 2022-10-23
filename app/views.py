from flask import Blueprint, request, render_template
from calculate_distance import calcDictDistance
from app.models import Vocabularies
from flask import jsonify


acehnese_dictionary_blueprint = Blueprint('acehnese_dictionary_blueprint', __name__)

@acehnese_dictionary_blueprint.route('/')
def home():
    return render_template('aceh_indo.html')

@acehnese_dictionary_blueprint.route('/home/')
@acehnese_dictionary_blueprint.route('/search/aceh-indonesia/', methods=["GET", "POST"])
def search_data_aceh_indonesia():
    semua_kosakata = {}

    if request.method == 'POST':
        word = request.form.get('word').lower() or "".lower()

        if len(word.replace(" ", "")) == 0:
            return render_template("search_vocabulary_aceh_indonesia.html")
        response = calcDictDistance(word=word, numWords=5, search_type='aceh_indonesia')
        semua_kosakata = response[0]

        words = {}

        for kosakata_aceh in semua_kosakata:
            arti = Vocabularies.query.filter_by(aceh=kosakata_aceh).first()
            words[f'{kosakata_aceh.capitalize()} ({arti.indonesia.capitalize()})'] = {}

        return render_template('search_vocabulary_aceh_indonesia.html', semua_kosakata=words, word=word)
    return render_template('search_vocabulary_aceh_indonesia.html')


@acehnese_dictionary_blueprint.route('/search/indonesia-aceh/', methods=["GET", "POST"])
def search_data_indonesia_aceh():
    semua_kosakata = {}

    if request.method == 'POST':
        word = request.form.get('word').lower() or "".lower()

        if len(word.replace(" ", "")) == 0:
            return render_template("search_vocabulary_indonesia_aceh.html")
        response = calcDictDistance(word=word, numWords=5, search_type='indonesia_aceh')
        semua_kosakata = response[0]

        words = {}
        for kosakata_aceh in semua_kosakata:
            arti = Vocabularies.query.filter_by(indonesia=kosakata_aceh).first()
            words[f'{kosakata_aceh.capitalize()} ({arti.aceh.upper()})'] = {}

        return render_template('search_vocabulary_indonesia_aceh.html', semua_kosakata=words, word=word)
    return render_template('search_vocabulary_indonesia_aceh.html')


@acehnese_dictionary_blueprint.route('/search/indonesia-aceh/<string:kata>/', methods=["GET", "POST"])
def get_indonesia_detail_indonesia_aceh(kata):
    key = kata.split("(")[0].strip()
    key = key.lower()
    selected_word = Vocabularies.query.filter_by(indonesia=key).first()

    if selected_word is None:
        return render_template("not_found_indonesia_aceh.html")
    elif selected_word is not None:
        return render_template('terjemahan_kata_indonesia_aceh.html', aceh=selected_word.aceh.upper(), indonesia=selected_word.indonesia.upper(), english=selected_word.english[:len(selected_word.english)-1].upper())


@acehnese_dictionary_blueprint.route('/search/aceh-indonesia/<string:kata>/', methods=["GET", "POST"])
def get_indonesia_detail_aceh_indonesia(kata):
    key = kata.split("(")[0].strip()
    key = key.lower()
    selected_word = Vocabularies.query.filter_by(aceh=key).first()

    if selected_word is None:
        return render_template("not_found_aceh_indonesia.html")
    elif selected_word is not None:
        return render_template('terjemahan_kata_aceh_indonesia.html', aceh=selected_word.aceh.upper(), indonesia=selected_word.indonesia.upper(), english=selected_word.english[:len(selected_word.english)-1].upper())
