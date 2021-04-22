# ---- Prosedural
# ---- OOP - Object Oriented Programming [Untuk software development]


# ## def Function
# - Function yang akan dipakai berkali-kali
# - Memiliki nama
# - Fungsinya generik (umum)

# ## Lambda Function
# - Function yang umumnya sekali pakau (Kecuali dimasukkan ke dalam def Function atau Variabel)
# - Anonymous (Tidak memiliki nama)
# - Biasanya digunakan untuk Fungsi khusus -Yang sekali pakai
# - Hanya memiliki satu program atau Fungsi /Expression
# - Tidak ada return ValueError

# ## Basic Syntax

# lambda Argumen = Expression
# - Jumlah argumen bisa unlimited (tidak terbatas)
# - Expression => Program / Fungsi hanya dapat 1 


# Contoh :
# def pangkat(x):
#     hasil = x**2
#     return hasil

# lambda x : x **2  ## ==> 1 Argumen => x, Expression/fungsi/program +> x ** 2
# lambda kilo : kilo * 5000 ## 1 Argumen => Kilo, Expression/fungsi/program => kilo *6000
# lambda kilo, harga : kilo * harga ## 2 Argumen => kilo, harga. Expression/fungsi/program => kilo *harga
# lambda x,y : x * y ## 2 Argumen => x,y. Expression/fungsi/program => x *y
# lambda kilo, harga, diskon : (kilo * harga) - diskon ## 3 Argumen => kilo, harga, diskon. Expression/fungsi/program (kilo * harga) - diskon


### Format def Function
# def penjumlahan (x,y):
#     hasil = x + y
#     return hasil

# def jumlah (x,y):
#     return x + y

# def pangkat2 (x):
#     hasil =  x ** 2
#     return hasil

# def triplet (a, b, c):
#     hasil = a * b *c
#     return hasil 

# # print (penjumlahan(5,5))
# # print (pangkat2(5))
# # print (triplet(5,10,5))


# ### Format Lambda Function
# ## Menggunakan Lambda dengan mengassign ke dalam variabel
# jumlah1 = lambda x,y: x + y
# pangkat = lambda x : x ** 2
# triple = lambda a, b, c,: a * b * c

# print (penjumlahan(5,5))
# print (pangkat2(5))
# print (triplet(5,10,5))
# print ("=" * 100)
# print (jumlah1(5,5))
# print (pangkat(5))
# print (triple(5,10,5))


# ### Menggunakan Lambda dengan def Function
# def myFunc(x):
#     hasil = lambda a : a ** x
#     return hasil

#     return lambda a : a ** x

# # # print (myFunc(10)) ## 2 adalah nilai x

# # pangkat2 = myFunc(2) ## 2 ==> nilai x
# # pangkat3 = myFunc(3) ## 3 ==> nilai x

# # print (pangkat2(10)) ## 10 ==> nilai a

# # pangkat4 = myFunc(4)

# # print (pangkat4(2)) ## 4==> nilai x dan 2 ==> nilai a



# # def myFunction(y):
# #     return lambda x : x * y

# # kali5 = myFunction(5)
# # print (kali5(10))

# # def myFunction(y):
# #     return lambda x : x * y
# # kali4 = myFunction(4)
# # print (kali4(10))

# ## Fungsi Konvensiomal
# # if angka%2 = 0 :
# #     print ("Ganjil")
# # else:
# #     print ("Genap")

# ## Def Function

# # def cekangka (x):
# #     if x%2 == 0:
# #         return ("Genap")
# #     else:
# #         return ("Ganjil")

# # print (cekangka(20))
# # print (cekangka(89))
# # print (cekangka(102))
# # print (cekangka(-3))
# # print (cekangka(-8))

# ## Lambda Function
# # cekGG = lambda x:True if x%2 == 0 else False
# # # print (cekGG(71))
# # # print (cekGG(22))

# # cekGG2 = lambda x: "Angka Genap" if x%2 == 0 else "Angka Ganjil"
# # print (cekGG2(9898))
# # print (cekGG2(3))



# ## Map Function
# # Function yang mirip dengan Lambda Function
# # Tapi digunakan untuk Data iterables - Data Structures (List, Tuples, Dict, Set, dll)

# A = [2, 70, 15, 81]
# B = A[::-1]

# def  kuadrat(x):
#     hasil =  x ** 2
#     return hasil

# kuadrat2 = lambda x: x ** 2

# # print (kuadrat(5))
# # print (kuadrat2(6))

# # print (kuadrat(A))
# # print (kuadrat2(A))

# # Basic Syntax:
# # map(Function, Argumen)

# # Function = Fungsi yang akan digunakan untuk Argumen
# # Argumen = Local variable yang akan digunakan
# # Argumen = Berbentuk data iterable - Data Structure
# # Jumlah Argumen sesuai dengan jumlah argumen pada Function yang digunakan
# # Hasil operasional map, berupa objek sehingga perlu dikonversi

# #hasil = list(map(kuadrat, A)) #map menggunakan def Function
# hasil2 = tuple(map(kuadrat, A)) #map menggunakan def Function

# # print (hasil)
# # print (hasil2)

# hasil3 = list(map(kuadrat2,A)) #Map dengan lambda function
# hasil4 = tuple(map(kuadrat2,A))
# # print (hasil3)
# # print (hasil4)

# hasil5 = list(map(lambda x: x**2, B[1::2]))
# # print (hasil5)

# # print ("=" * 100)

# A = [2, 70, 15, 81]
# B = []

# for i in range(len(A)):
#     if i == 0 or i == 2:
#         B.append(i)
# hasil6 = list(map(kuadrat2,B))

# print (hasil6)

# def jumlah (x,y):
#     hasil = x + y

# jumlah2 = lambda x,y : x + y

# # A = [1, 2, 3, 4, 5 ]
# # B = [10, 20, 30 ]

# hasil = list(map(jumlah2, A, B))

# print (hasil)


# hasil2 = list(map(lambda x,y: x + y, A, B))
# print (hasil2)

# A = [2, 5, 6]
# B = [10, 20, 30]
# C = [9, 8, 7]

# def triple (x,y,z):
#     hasil = x * y * z
#     return hasil

# hasil = list(map(triple, A, B, C))
# print (hasil)

# triple2 = lambda x, y, z: x * y *z

# hasil2 = list(map(triple2, A, B, C))
# print (hasil2)

# hasil = list(map(lambda x, y, z: x * y * z, A, B, C))

# print (hasil)


# D = [10, 15, 20, 30]

# ### D * (D**2)

# def pow1 (x):
#     hasil = x ** 2
#     return hasil


# def kali (x,y):
#     hasil = x * y
#     return hasil

# E = list(map(pow1, D))
# hasil = list(map(kali, D, E))

# print (hasil)

# pangkat = lambda x: x ** 2
# perkalian = lambda x, y: x*y


# result = list(map(pangkat, D))
# result1 = list(map(perkalian, D, result))

# print (result1)

# hasil = list(map(perkalian, D, map(lambda x : x **2, D)))
# print (hasil)

# hasil = list(map(lambda x, y: x * y, D, list(map(lambda x: x ** 2, D))))
# print (hasil)


'''
#########################################
A = [1, 2, 3, 4, 5]

## (A**2) + ((A**2) * 3) + ((A**2) * 5)


def kalkulasi (angka):
    hasil = []
    for i in angka:
        x = i ** 2
        D = x + (x *3) + (x * 5)
        hasil.append(D)
    return hasil

print (kalkulasi(A))

calc = lambda i: (i**2) + ((i**2)*3) + ((i**2)*5)
hasil = list(map(calc, A))

print (hasil)
'''

A = [1, 2, 3, 4, 5]

## (A**2) + ((A**2) * 3) + ((A**2) * 5)

pangkat2 = lambda i: i **2
kali3 = lambda x: x * 3
kali5 = lambda x: x * 5
jumlahkan = lambda j, k, l: j + k + l

E = list(map(pangkat2, A))  # -->Pangkat2
F = list(map(kali3, E)) # -->kali3
G = list(map(kali5, E)) # -->kali5
H = list(map(jumlahkan, E, F, G)) # --?


print (E)
print (F)
print (G)
print (H)

print("=" *100)

E1 = list(map(lambda i: i ** 2, A))
F1 = list(map(kali3, list(map(lambda i: i ** 2, A))))
G1 = list(map(kali5, list(map(lambda x: x * 3, A))))
H1 = list(map(jumlahkan, list(map(lambda i: i ** 2, A)), F, G))

print (E1)
print (F1)
print (G1)
print (H1)

print ("=" * 100)

F2 = list(map(lambda x: x * 3, list(map(lambda i: i ** 2, A))))
print (F2)

print ("=" * 100)

G2 = list(map(kali5, list(map(lambda i: i ** 2, A))))
print (G2)


# F = F1 = F2

result3 = list(map(jumlahkan, list(map(lambda i:i ** 2, A)), list(map(lambda x: x * 3, list(map(lambda x:x ** 2, A)))), list(map(lambda x:x * 5, list(map(lambda x:x ** 2, A))))))
print(result3)

result5 = list(map(lambda x, y, z : x + y + z, 
list(map(lambda i: i ** 2, A)), 
list(map(lambda x: x * 3, list(map(lambda x:x ** 2, A)))), 
list(map(lambda x: x * 5, list(map(lambda x:x ** 2, A)))))) 

print (result5)

R = list(map(lambda i: i ** 2, A))
S = list(map(lambda x: x * 3, R))
T = list(map(lambda x: x * 5, R))
jumlah2 = lambda x, y, z : x + y + z

result9 =  list(map(jumlah2, R, S, T))

print (result9)