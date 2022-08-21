"""
Requirements:
1. Pastikan semua data dalam file terpisah berdasarkan baris
2. Pisahkan setiap kata menjadi 3 nilai dalam list [a, b, c]
3. Masukkan setiap kata ke dalam database
4. jika kata dalam list lebih 
"""

from app.controller.kosakata import buat_kosakata_baru

file = open('kosa_kata.txt','r')

data = file.readlines()

for d in data:
    kata = d.split(' - ')
    if len(kata) < 2:
        continue
    if len(d.split(' - ')) > 3:
        print('lebih dari 3')
    if len(d.split(' - ')) < 3:
        print('kurang dari 3')

    print(f'{kata[0]}, {kata[1]}, {kata[2]}')
    buat_kosakata_baru(kata[0], kata[1], kata[2])