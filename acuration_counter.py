from levenshtein import levenshteinDistanceMatrix
from app.utilities import calculate_percentage_accuracy, insert_distance_percentage
from calculate_distance import calcDictDistance

file = open('expected_data_test.txt', 'r')

jumlah_list = int(input('Masukkan jumlah list data: '))
def hitung():
    data = file.readlines()
    jumlah = 0
    rekap_posisi_kata_dicari = []
    rata_rata_posisi = 0
    for d in data:
        kosakata = d.split(' - ')
        if len(kosakata) == 2:        
            jumlah += 1
            list_rekomendasi = calcDictDistance(kosakata[0], jumlah_list, 'aceh_indonesia')[0]
            posisi_sort = list_rekomendasi.index(kosakata[1][:-1]) + 1
            list_rekomendasi.reverse()
            posisi_kata_dicari = list_rekomendasi.index(kosakata[1][:-1]) + 1
            rekap_posisi_kata_dicari.append(posisi_kata_dicari)
            rata_rata_posisi += posisi_kata_dicari/jumlah_list
            hasil_bagi = posisi_kata_dicari/jumlah_list
    
    akurasi = (rata_rata_posisi / jumlah) * 100
    output = {
        'jumlah': jumlah,
        'rekap_posisi_kata_dicari': rekap_posisi_kata_dicari,
        'rata_rata_posisi': rata_rata_posisi,
        'akurasi': f'{akurasi}%'
    }
    return output

print(hitung())
