'''
=== Filter function ===
- Comparison function = untuk pengecekan kondisi

Basic syntax :
filter(function, Data iterable)

- Function hanya bisa 1
- Data iterable 
- Menghasilkan data object sehingga perlu dikonversi


Comparison - Conditional
>
<
>=
<=
OR, AND, dll

TRUE and FALSE
Filter hanya akan mengambil Nilai yang bernilai True
'''

A = [1,2,3,4,5,6,7,8,9,10]

hasil = list(filter(lambda x: x%2 == 0, A))

print (hasil)

B = [26, 20, 10, 8, 70, 56, 89, 100, 5]

cek = lambda x: x > 20
hasil2 = list(filter(cek, B))
print (hasil2)

'''
=== Reduce ===
- Akan menghasilkan satu value
Basic Syntax : 
reduce (function, data iterable)

a = [1,2,3,4,5]
x + y
1 + 2
(1 + 2) + 3
(1 + 2 + 3) + 4
(1 + 2 + 3 + 4) + 5
'''

from functools import reduce

F = [1,2,3,4,5,6,7,8,9]

hasil = reduce(lambda x,y: (x + y) * 2, F)

print (hasil)

###
# Berapa jumlah total bilangan ganjil yang telah dipangkat 3 dari rentang angka 1 - 200
# buat 1 baris fungsi (selain define var)

A = list()
for i in range (1,201):
    A.append(i)
print (A)

pangkat3 = list(map(lambda x: x ** 3, A))

ganjil = list(filter(map(lambda x: x%2 != 0, pangkat3)))

print (pangkat3.count(ganjil))


### Tugas Latihan

1. 
Input : Masukkan kalimat
"Nama Saya Joni"
Output : 'aman ayas inoj'.


2. 
Buat Algoritma 
Buat list (masukkan list inputan dari user)
--Angka - Alfa
--Numerik
Pilihan 
1. Ascending
2. Descending

Output sesuai pilihan
1. Angka akan disort dari terkecil ke terbesar
2. Angka akan disort dari terbesar ke terkecil
3. Nilai maks dan nilai min
Looping, If, map, lambda, def

Tidak boleh menggunakan fungsi sort atau [::-1]
Gunakan algoritma


3.
Stats
Buat list
- Cari nilai 
Modus : Nilai yang paling sering muncul
Median : Nilai tengah
Mean : Rata-rata
Q1 : Kuartil 1 (25%)
Q3 : Kuartil 3 (75%)
Outliers : 


4.
Buat def function untuk spin angka

Ada deret angka

[[1 2 3 4 5],
[6 7 8 9 10],
[11 12 13 14 15],
[16 17 18 19 20]]

Input :
masukkan angka 1-4

Pilihan 1:
[[21,16,20,6,1],]
[[22,17,21,7,2],]
[[23,18,22,8,3],]
[[24,19,23,9,4],]
[[25,20,24,10,5]]

Pilihan 2:
[[25,24,23,22,21],]
[[20,19,18,17,16],]
[[15,14,13,12,11],]
[[10,9,8,7,6],]
[[5,4,3,2,1]]

Pilihan 3:
[[5,10,15,20,25],]
[[4,9,14,19,24],]
[[3,8,13,18,23],]
[[2,7,12,17,22],]
[[1,6,11,16,21]]
