"""
Program menghitung luas segitiga
luas segitiga = alas * tinggi / 2
"""
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('fungsi hitung luas segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'Menghitung luas segitiga dengan alas= 10, tinggi= 6, hasilnya= {hitung_luas_segitiga(10, 6)}')
print(f'Menghitung luas segitiga dengan alas= 20, tinggi= 2, hasilnya= {hitung_luas_segitiga(20, 2)}')

