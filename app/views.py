from flask import Blueprint, request, render_template

acehnese_dictionary = Blueprint('acehnese_dictionary', __name__)

@acehnese_dictionary.route('/')
@acehnese_dictionary.route('/home')
def home():
    return "Halaman Home Berisi form input data"


@acehnese_dictionary.route('/search')
def search_data():
    if request.method == 'GET':
        languages = [
                "A", "Alat", "Alamat", "Alokasi", "Apa", "Anda", "Andai", "Arak",
                "B", "Bolu", "Bola", "Bunglon", "Badan", "Badai", "Bagaimana",
                "C", "Contoh", "Corak", "Canda", "Ceramah", "Cari", "Cermat", "Cerdas",
                "D", "Dolar", "Dunia", "Dari", "Doraemon", "Data", "Dan",
                "E", "Ember", "Elemen", "Estetik",
                "R", "Rumit", "Rencana", "Rupiah", "Roda", "Rugi", "Rangkul", "Raja", "Ratu", "Ragu"
            ]
        
        if request.method == 'POST':
            return 'Halaman Detail kosakata'
        return render_template('search_vocabulary.html', languages=languages)
