"""
Requirements:
1. Pastikan semua data dalam file terpisah berdasarkan baris
2. Pisahkan setiap kata menjadi 3 nilai dalam list [a, b, c]
3. Masukkan setiap kata ke dalam database
4. jika kata dalam list lebih 
"""

def get_all_data():
    file = open('kosa_kata.txt','r')
    data = file.readlines()
    semua_kosakata = []
    semua_kosakata_aceh = []
    semua_kosakata_indonesia = []
    semua_kosakata_english = []
    all_data = {}

    for d in data:
        kata = d.split(' - ')
        if len(kata) < 2:
            continue
        if len(d.split(' - ')) > 3:
            continue
        if len(d.split(' - ')) < 3:
            continue
        
        semua_kosakata.append([kata[0], kata[1], kata[2][:-1]])
        semua_kosakata_aceh.append(kata[0])
        semua_kosakata_indonesia.append(kata[1])
        semua_kosakata_english.append(kata[2][:-1])

    all_data['semua_kosakata'] = semua_kosakata
    all_data['semua_kosakata_aceh'] = semua_kosakata_aceh
    all_data['semua_kosakata_indonesia'] = semua_kosakata_indonesia
    all_data['semua_kosakata_english'] = semua_kosakata_english

    return all_data