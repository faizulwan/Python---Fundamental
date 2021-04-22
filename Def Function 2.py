


# angka = 6
# if angka%2 == 0:
#     print ("Genap")
# else:
#     print ("Ganjil")


# angka2 = 18
# if angka%2 == 0:
#     print ("Genap")
# else:
#     print ("Ganjil")





### def Function
### Memberikan Nama untuk suatu fungsi, agar fungsi dapat digunakan berkali-kali tanpa perlu diketik ulang
###  Memiliki konsep yang sama dengan variabel, hanya saja kalau variabel menyimpan data, kalau def menyimpan fungsi

# #Basic Syntax = 
# namaFunction():
#     Fungsi programnya


# def namaFunction(Argumen):
#     Fungsi/programnya

#Pemberian nama Function mengikuti aturan pemberian nama variabel
#Argumen bersifat opsional => Bisa kosong bisa berisi
#Jumlah argumen tidak dibatasi (tak terhingga)

# def cekbilangan(angka):
#     if angka == 0:
#         print ("Angka merupakan bilangan nol")
    
#     elif angka%2 == 0:
#         print ("Genap")
    
#     else:
#         print ("Ganjil")

# cekbilangan(11)



# Inisialisasi Function
# def namabuah():
#     print  ("Ini buah apel")

# ## Cara menggunakan function atau memanggil function
# # namabuah()

# def hargabuah():
#     namabuah()
#     print ("Harga apel per kilo Rp65.000")

# hargabuah()


# kg = int(input("Berat buah (kg) : "))

'''
## Argumen == Variabel
Memasukkan value-dat ke dalam local variabel
Global Variabel ==> Variabel yang di define di luar Function 
-bisa digunakan di semua tempat

Local Variabel ==> Variabel yang di define dan digunakan di dalam function
- hanya dapat digunakan di dalam function yangg bersangkutan (temopat variabel yang di define)
'''

# A = 5  #==>> Global Variabel (Karena di define di luar function)

# def totalbelanja(berat):
#     hargabuah()
#     harga = 65000  #==>> Local variabel
#     total = berat * harga  #==>> Local variabel
    
#     print ("Harga apel per", berat, "kilo adalah" ,total)

# totalbelanja(10)





### Multiple Argumen
# def guru(nama, pelajaran):
#     print("Nama guru ini adalah", nama)
#     print("Mengajar pelajaran", pelajaran)

# guru("Faiz", "Geotech")
# ## Urutan memasukkan value  harus sesuai dengan urutan pada argumen
# ## Jumlah value harus  sama persih dengan jumlah argumen pada function
# guru("sandy") ### Salah
# guru("math") ### Salah

####  Memanfaatkan keyword
# guru (pelajaran='fisika',nama='beni')  ##Langsung memasukkan value ke dalam argumen


### Menggunakan nilai default

# def pegawai(nama, jabatan="staff", gaji=700000):  ##Staff dan 7000000 itu merupakan nilai default
#     print ("Nama pegawai :", nama)
#     print ("Memiliki jabatan :", jabatan)
#     print ("Gaji : Rp", gaji)

# pegawai(nama="Doni", jabatan="Data Manager", gaji="50000000")
# pegawai(nama="Doni")
# pegawai(gaji="50000000",nama="Doni",)
# pegawai("Adi")
## Jika argumen tidak ditentukan default valulenya maka kita wajib memasukkan valuenya


### Return Function
# Function dengan return value
# Ketika kita ingin mendapatkan hasil dari proses fungsi/program di dalam function
# dengan menggunakan return function kita bisa memasukkan hasil function ke dalam variabel sehingga dapat digunakan untuk kalkulasi lanjutan

def kuadrat(x):
    hasil = x ** 2
    return (hasil)

# A = kuadrat(3) * 10
# print(A)


def pangkat(x,y):
    hasil = x ** y
    return (hasil)

# C = pangkat(2,3)
# D = pangkat(4,2)

# print (C)
# print (D)

# ## Penentuan variabel sangat penting


# angka1 = int(input("Masukkan angka 1 : "))
# angka2 = int(input("Masukkan angka 2 : "))

# result = pangkat(angka1,angka2)
# print ("Hasil dari perhitungan adalah", result)

def perkalian(x,y):
    hasil = x * y
    return (hasil)

A = kuadrat(5)
B = pangkat (4,2)
C = perkalian (A,B)
print(A)
print(B)
print(C)
print('='*50)

result = perkalian(kuadrat(5), pangkat(4,2))
print(result)