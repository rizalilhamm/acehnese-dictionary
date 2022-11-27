import os
from flask import Blueprint, request, render_template, redirect
from calculate_distance import calcDictDistance
from app.models import *
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
            return render_template("search_vocabulary_aceh_indonesia2.html")
        response = calcDictDistance(word=word, numWords=100, search_type='aceh_indonesia', csv_filename='distance_percentage_aceh_indonesia.csv')
        semua_kosakata = response[0]

        words = {}

        for kosakata_aceh in semua_kosakata:
            arti = Vocabularies.query.filter_by(aceh=kosakata_aceh).first()
            words[f'{kosakata_aceh.capitalize()} ({arti.indonesia.capitalize()})'] = {}

        return render_template('search_vocabulary_aceh_indonesia2.html', semua_kosakata=words, word=word)
    return render_template('search_vocabulary_aceh_indonesia2.html')


@acehnese_dictionary_blueprint.route('/search/indonesia-aceh/', methods=["GET", "POST"])
def search_data_indonesia_aceh():
    semua_kosakata = {}

    if request.method == 'POST':
        word = request.form.get('word').lower() or "".lower()

        if len(word.replace(" ", "")) == 0:
            return render_template("search_vocabulary_indonesia_aceh2.html")
        response = calcDictDistance(word=word, numWords=100, search_type='indonesia_aceh', csv_filename='distance_percentage_indonesia_aceh.csv')
        semua_kosakata = response[0]

        words = {}
        jumlah = 0
        for kosakata_aceh in semua_kosakata:
            arti = Vocabularies.query.filter_by(indonesia=kosakata_aceh).first()
            words[f'{kosakata_aceh.capitalize()} ({arti.aceh.upper()})'] = {}
            jumlah += 1

        return render_template('search_vocabulary_indonesia_aceh2.html', semua_kosakata=words, word=word, jumlah=jumlah)
    return render_template('search_vocabulary_indonesia_aceh2.html')


@acehnese_dictionary_blueprint.route('/search/indonesia-aceh/<string:kata>/', methods=["GET", "POST"])
def get_indonesia_detail_indonesia_aceh(kata):
    key = kata.split("(")[0].strip()
    key = key.lower()
    selected_word = Vocabularies.query.filter_by(indonesia=key).first()

    if request.method == 'POST':
        return search_data_indonesia_aceh()
    if selected_word is None:
        return render_template("not_found_indonesia_aceh.html")
    elif selected_word is not None:
        return render_template('terjemahan_kata_indonesia_aceh2.html', aceh=selected_word.aceh.upper(), indonesia=selected_word.indonesia.upper(), english=selected_word.english[:len(selected_word.english)-1].upper())


@acehnese_dictionary_blueprint.route('/search/aceh-indonesia/<string:kata>/', methods=["GET", "POST"])
def get_indonesia_detail_aceh_indonesia(kata):
    key = kata.split("(")[0].strip()
    key = key.lower()
    selected_word = Vocabularies.query.filter_by(aceh=key).first()
    
    if request.method == 'POST':
        return search_data_aceh_indonesia()
    
    if selected_word is None:
        return render_template("not_found_aceh_indonesia2.html")
    elif selected_word is not None:
        return render_template('terjemahan_kata_aceh_indonesia2.html', aceh=selected_word.aceh.upper(), indonesia=selected_word.indonesia.upper(), english=selected_word.english[:len(selected_word.english)-1].upper())

@acehnese_dictionary_blueprint.route('/detailai')
def detail_aceh_indonesia():
    alldata = [
    ]
    with open(f'{os.getcwd()}/distance_percentage_aceh_indonesia.csv') as aceh_csv:
        for row in aceh_csv:
            data = row.split(',')
            alldata.append(data)

    return render_template('persen_aceh_indonesia.html', alldata=alldata)

@acehnese_dictionary_blueprint.route('/detailia')
def detail_indonesia_aceh():
    alldata = [
    ]
    with open(f'{os.getcwd()}/distance_percentage_indonesia_aceh.csv') as aceh_csv:
        for row in aceh_csv:
            data = row.split(',')
            alldata.append(data)

    return render_template('persen_indonesia_aceh.html', alldata=alldata)
