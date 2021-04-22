### Tugas Latihan
#####################################################################################
# 1. 
# Input : Masukkan kalimat
# "Nama Saya Joni"
# Output : 'aman ayas inoj'

'''
masukkan = "i"
while masukkan != " ":
    masukkan = str(input("Masukkan kalimat Anda: "))
    masukkan_dibagi = masukkan[::-1].split()
    hasil = masukkan_dibagi[::-1]

    print (hasil)
'''
#####################################################################################
   


#####################################################################################   
# 2. 
# Buat Algoritma 
# Buat list (masukkan list inputan dari user)
# --Angka - Alfa
# --Numerik
# Pilihan 
# 1. Ascending
# 2. Descending

# Output sesuai pilihan
# 1. Angka akan disort dari terkecil ke terbesar
# 2. Angka akan disort dari terbesar ke terkecil
# 3. Nilai maks dan nilai min
# Looping, If, map, lambda, def

# Tidak boleh menggunakan fungsi sort atau [::-1]
# Gunakan algoritma
#####################################################################################




#####################################################################################
# 3.
# Stats
# Buat list
# - Cari nilai 
# Modus : Nilai yang paling sering muncul
# Median : Nilai tengah
# Mean : Rata-rata
# Q1 : Kuartil 1 (25%)
# Q3 : Kuartil 3 (75%)
# Outliers : 

#menghitung mean

# baris = [1,1,5,2,2,2,2,2,2,2,2,2,2,2,4,4,4,3,7,9,15,10,10,10,10,10,10,11]
# baris2 = list(range(1,1000))

# def mean(listangka):
#     suma=0
#     for a in listangka:
#         suma+= a
#     mean = suma/len(listangka)
#     return mean

# def median(listangka):
#     listangka.sort()
#     freq = len(listangka)
#     if freq %2 != 0:
#         median = listangka[freq//2+1]
#         return median
#     else:
#         median = (listangka[freq//2+1] + listangka[freq//2])/2
#         return int(median)

# def percentile(listangka,persentil):
#     listangka.sort()
#     freq = len(listangka)
#     indexpersentil = int(freq * persentil/100)
#     if freq %2 != 0:
#         persentil = listangka[indexpersentil]
#         return persentil
#     else:
#         persentil = ((listangka[indexpersentil] + listangka[indexpersentil+1])/2)
#         return int(persentil)

# def modus(listangka):
#     freq = 0
#     angka = 0

#     for a in listangka:
#         if listangka.count(a)>freq :
#             freq = listangka.count(a)
#             angka = a
#     return angka

# #     for a in (listangka):       

# print (mean(baris2))

# print (median(baris))

# print (modus(baris))

# print (percentile(baris,10))
#####################################################################################




#####################################################################################
# 4.
# Buat return def function untuk spin angka

# Ada deret angka

# [[1 2 3 4 5],
# [6 7 8 9 10],
# [11 12 13 14 15],
# [16 17 18 19 20]]

# Input :
# masukkan angka 1-4

# Pilihan 1:
# [[21,16,20,6,1],]
# [[22,17,21,7,2],]
# [[23,18,22,8,3],]
# [[24,19,23,9,4],]
# [[25,20,24,10,5]]

# Pilihan 2:
# [[25,24,23,22,21],]
# [[20,19,18,17,16],]
# [[15,14,13,12,11],]
# [[10,9,8,7,6],]
# [[5,4,3,2,1]]

# Pilihan 3:
# [[5,10,15,20,25],]
# [[4,9,14,19,24],]
# [[3,8,13,18,23],]
# [[2,7,12,17,22],]
# [[1,6,11,16,21]]
#####################################################################################


#####################################################################################
# 5.
# Buat return def function
# Kalkulator (+)(-)(/)(*)
# Inputan
# input angka 1:
# input angka 2:
# Masukkan operator :
# Output : Hasil penjumlahan dari 8 + 10 = 18

'''
def jumlah (x,y):
    hasill = x + y
    return hasill

def kurang (x,y):
    hasil = x - y
    return hasil

def kali (x,y):
    hasil = x * y
    return hasil

def bagi (x,y):
    hasil = x / y
    return hasil

try:
    input_1 = float(input("Masukkan angka pertama: "))
    input_2 = float(input("Masukkan angka kedua: "))
    operator = str(input("Masukkan operator (+)(-)(/)(*): "))

    if operator == "+":
        A = jumlah(input_1,input_2)
        print (f'Hasil penjumlahan dari {input_1} + {input_2} = {A}')

    elif operator == "-":
        B = kurang(input_1,input_2)
        print (f'Hasil pengurangan dari {input_1} + {input_2} = {B}')

    elif operator == "*":
        C = kali(input_1,input_2)
        print (f'Hasil perkalian dari {input_1} + {input_2} = {C}')

    elif operator == "/":
        D = bagi(input_1,input_2)
        print (f'Hasil pembagian dari {input_1} + {input_2} = {D}')
    
    else:
        print ("Operator tidak tersedia")



except:
    print ("Tidak dapat menerima inputan ")
'''
#####################################################################################



#####################################################################################
# 6.
# Buat def function
# Fizz Buzz

# Input : Masukkan  angka :
# Output :
# Angka dari input user akan menjadi range -1 inputan tersebut
# outputnya akan dicek seluruh angka tersebut
# kemudian akan diprint angka yang habis menjadi 3 akan diubah menjadi Fizz
# angka yang habis dibagi 5 akan diubah menjadi Buzz
# angkat yang habis dibagi 3 dan 5 menjadi fizzbuzz
# angka lain dicetak normal
'''
try:
    inputan = int(input("Masukkan angka: "))

    angka = list()
    for i in range (0, inputan):
        angka.append(i)

    # print (angka)

    for i in angka:
        if angka[i] % 3 == 0 and angka[i] % 5 == 0:
            print ("fizzbuzz")

        elif angka[i] % 3 == 0:
            print ("fizz")
        
        elif angka[i] % 5 ==0:
            print ("buzz") 

        else:
            print (angka[i])

except:
    print ("Inputan harus berupa angka")
'''
#####################################################################################





#####################################################################################
# 7.
# Buat def function
# Caesar Cipher (nambah ngurangin abjad sesuai angka)
# masukkan kata/kalimat : Joni
# masukkan angka : 2
# outputnya : Lqpk
# j + 2 = l
# 0 + 2 = q
# n + 2 = p
# i + 2 = k

# masukkan kata : Joni
# masukkan angka : -2
# outputnya : imlg

'''
huruf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

masukkan = str(input("Masukkan kata atau kalimat: ")).lower()
kata_list = list(masukkan)
angka = int(input("Masukkan angka: "))
huruf = huruf * 5
katafinal = list()
strkata = str()

if masukkan.isalpha() == True:
    for i in kata_list:
    
        index_huruf = huruf.index(i)
        tambah_huruf = index_huruf + angka
        final_huruf = huruf[tambah_huruf]
        katafinal.append(final_huruf)
    strkata = strkata.join(katafinal)
    print (strkata)

else:
    print ("Format inputan kata atau kalimat salah")
'''
#####################################################################################
    





# #####################################################################################
# # 8.
# # Konversi Romawi
# # buat return function
# # Gunakan dict
# # batasan maksimal <= 4000
# # keluar notif angka diluar jangkauan

# # Silahkan masukkan angka : 2018
# # Ouputnya : MMXVIII

# # Silahkan masukkan angka : MMXVIII
# # Ouputnya : 2018

# kamus = {
#     "M" : 1000, 
#     "CM" : 900, 
#     "D": 500, 
#     "CD": 400, 
#     "C" : 100, 
#     "XC" : 90,
#     "L": 50, 
#     "XL":40,
#     "X": 10, 
#     "IX": 9, 
#     "V": 5, 
#     "IV":4, 
#     "I": 1
#     }

# roman = list (kamus.keys())
# numeric = list (kamus.values())








# print ("==> NUMBER-ROMAN CONVERSION <==")
# print (''' What is your goal : 
# 1. Number to Roman
# 2. Roman to Number''')


# try:
#     masukkan = int(input("Choose your goal (1/2) : "))

#     if masukkan == 1:
#         print ("Number to Roman Conversion")
#         number = int(input("Input your number : "))

#         if number > 4000:
#             print ("Can not process number greater than 4000")

#         elif number <= 0:
#             print ("Can not process zero and negative number")

#         else:


#     elif masukkan == 2:
#         print ("Roman to Number Conversion")

#     else:
#         print ("Application can not be found")

# except:
#     print ("Invalid input")



for i in range(50):
        huruf = int(i*(i+1)/2)
        print ('\nhuruf\n')