# # #### Tuple == Mirip dengan list, tetapi elementnya immutable
# # #Immutable ==> Tidak bisa di update

# # # tuple_A = ()
# # # tuple_B = tuple(data)
# # # tuple_C = 2, 3, 4, 'Motor', 'Mobil', 12.4  ##Data hanya dipisahkan dengan koma tanpa tanda kurung

# # hari = ('Senin', 'Selasa', 'Rabu', 'Kamis', "Jum'at", 'Sabtu', 'Minggu')

# # print(hari)

# # # hari.append('Kamis) ##Tidak bisa menambahkan data baru ke dalam Tuple
# # # hari.extend('Jumat) ##Tuple tidak memiliki fungsi/attribut extend dan append untuk menambah dat
# # # Updating,remove, dan POP data tidak dapat dilakukan pada Tupple

# # ## Read - Membaca  Data ==> Indexing dan Slicing dapat dilakukan
# # print (hari[4])
# # print (hari[:2])
# # print (hari [1])

# # print (hari.index('Rabu'))

# # angka = (12, 13, 44, 108, 23, 44, 70, 123, 54, 12, 12, 67, -2)
# # print (angka.count(12))
# # ## Tupple tidak memiliki fungsi sort
# # ### Tupple hanya memiliki fungsi count dan index
# # ### Tupple biasanya digunakan hanya untuk 1 user (e.g. Admin) tidak ada penambahan user lain

# # ### Packing dan Upacking

# # # ----Packing----
# # user = ('Andi', 25, 'Jakarta')
# # user = 'Andi', 25, 'Jakarta' #Format Lain

# # # ---Unpacking----

# # Nama, Usia, Kota = user #Mengassign setiap elemn dari tupple ke-dalam variabel yang berbeda
# # ### Jumlah variabel harus sama dengan jumlah elemen dalam Tupple
# # print (Nama)
# # print (Usia)

# # Konsep Packing - Unpacking sebenrnya mengadopsi atau serupa dengan konsep Multiple Assignment

# # a, b, c, = 70, 85, 90

# # data = 70, 80, 85, [85, 90, 80, (56, 78, 90, ['Senin', 'Selasa', (True, False)])]

# # print (data.index([85, 90, 80, (56, 78, 90)]))
# # print (data[3])
# # print (data[3].index((56, 78, 90)))
# # print (data[3][3].index(78))
# # print(data[3][3][0])




# #### SET
# # list_A = []
# # tuple_A = ()
# # set_A = {}

# # ### Unordered List, Unique (Tidak bisa duplikat), No Indexing
# # ### SET == Himpunan
# # ### -Tidak bisa mengandung data list, Tetapi bisa mengandung tupple karen tupple bersifat immutable
# # ### -Non Indexing
# # ### -

# set_A = {}
# set_A = set()

# # Avanza = 10
# # Yaris = 50
# # Xenia = 30
# # Jazz = 10

# mobil = {'Avanza', 'Yaris', 'Xenia', 'Avanza', 'Jazz', 'Jazz', 'Xenia', 'Avanza', 'Yaris', 'Yaris', 'Xenia', 'Yaris', 'Avanza', 'Yaris', 'Jazz' }
# print(type(mobil))

# print(mobil)

# A = {2,4,5,6,8,4,4,2,(2,3,4,6,7),8,5,3,4,2,1,1,1,2,3,4,5,6,7,3,1,3,4,1}
# print (A)

###Menambahkan Data - Create
# Update ==> Sama konsepnya dengan extend pada list
# A.update ('Caca') ###Mirip dengan fungsi extend pada list => Menambahkan setiap elemen
# A.update (['Geri', 'Andre'])
# A.update (['Caca'])
# A.update (['968'])  ###Fungsi Update tidak bisa langsung menambahkan data integer/float
# print (A)

# #Add ==> Sama konsepnya dengan append pada list
# A.add ('Desi') ###Seperti fungsi append pada list
# A.add (968)
# A.add ('Desi') ###Jika ada penambahan data yang sama maka hanya ke print satu kali karena set == unique value saja
# print (A)

### Hapus Data = Delete
## Remove
# A.remove ('c')
# # A.remove (100) ##Akan mengeluarkan error jika data tidak ada
# A.discard (100) ##Tidak akan keluar error meskipun data tidak data
# print (A)

### Menghapus seluruh elemen dalam SET
# A.clear ()
# print (A)

### MEnghapus seluruh elemen beserta SET
# del A
#print (A)


####Operasi himpunan pada SET
x = {7, 8, 9, 10, 11}
y = {7, 8, 15, 20, 25}


# ##Gabungan - Union (Gabungan antara 2 atau lebih himpunan/set)
# z = x.union(y) ### Menggunakan fungsi union
# print (z)

# z1 = y.union(x) ### Menggunakan fungsi union
# print (z1)

# print (x | y) ### Menggunakan simbol union |
# print (y | x)



##Irisan - Intersection (Menampilkan data yang beririsan)
# i = x.intersection(y) ### Menggunakan fungsi union
# print (i)

# i1 = y.intersection(x) ### Menggunakan fungsi union
# print (i1)

# print (x & y) ### Menggunakan simbol intersection &
# print (y & x)



##Selisih - Difference (Menampilkan anggota set yang dikurangi dengan anggota set yang lain)
# j = x.difference(y) ###Menggunakan fungsi difference
# print (j)

# k = y.difference(x) ###Menggunakan fungsi difference
# print (k)

# print (x - y) ### Menggunakan simbol differencepy Meeting7.py
# print (y - x)



##Beda Setangkup - Symmetric Difference (Merupakan gabungan yang dikurangi irisan)

# l = x.symmetric_difference(y)  ### MEnggunakan fungsi symmetric difference
# l1 = y.symmetric_difference(x)
# print (l)
# print (l1)

# print (x ^ y) ### Menggunakan simbol Symmetric Difference


## Latihan
# a = {2,4,6,8,10,12,14,16,18,20}
# b = {1,3,5,7,9,11,13,15,17,19}
# c = {-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1}
# d = {2,3,5,7,11,13,17,19}
# e = {1,4,6,8,9,10,12,14,15,16,18,20}

# U = Union
# n = irisan

# A. a U b U c U d U e
# B. (a n b) u (d n e)
# C. (a u b) n (d u e)
# D. (a u b) - (d u e)
# E. (a u b u c) - (a n e)

##Membuat himpunannya menggunakan Fungsi


i = 0
j = -20
f = 20

#Bilangan genap
a = set()
for t in range (i+1,f+1):
    if t % 2 == 0:
        a.add(t)


#Bilangan ganjil
b = set()
for r in range (i,f):
    if r % 2 != 0:
        b.add(r)


#Bilangan negatif
c = set()
for v in range (j,i):
    if v < 0:
        c.add(v)

#Bilangan prima - Komposit
d = set()
e = set()

for x in range (i,f+1):
    if x>1:
        for z in range (2,x):
            if (x % z) == 0:
                e.add(x)
                break
        else:
            d.add(x)

# print (a)
# print (b)
# print (c)
# print (d)
# print (e)

###JAWAB SOAL========

#A. a U b U c U d U e
k = a.union(b)
l = k.union(c)
m = l.union(d)
n = m.union(e)
print(n)

print ("="*100)

# B. (a n b) u (d n e)
d1 = a.intersection(b)
d2 = d.intersection(e)
d3 = d1.union(d2)
print(d3)

print ("="*100)

# C. (a u b) n (d u e)
u1 = a.union(b)
u2 = d.union(e)
u3 = u1.intersection(u2)
print(u3)

print ("="*100)

# D. (a u b) - (d u e)
s1 = u1.difference(u2)
print(s1)

print ("="*100)

# E. (a u b u c) - (a n e)
e0 =a.intersection(e)
e1 =l.difference(e0)
print(e1)

# ###Tugas

# 1. 
# hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

# input : 
# 'Masukkan nama hari : ' (senin)
# 'Masukkan Jumlah : (100) 'Nilai harus int, jika bukan maka keluar notifikasi :...'

# Output:
# '100 hari dari hari...(senin)...adalah hari...'
# '3 hari dari hari senin adalah hari kamis'

# Kondisi :
# -Tidak Case sensitive
# -Ada pengecekan Hari : Tidak ada nama hari
# -Jumlah angka harus integer bisa positif/negatif


# 2.
# Palindrome

# katak = katak
# level = level
# madam = madam
# noon = noon

# input : Masukkan kata : ......
# kondisi:
# Lakukan pengecekan apakah kata tersebut termasuk Palindrome

# Ouput:
# Kata ini tidak termasuk/termasuk Palindrome


# 3.
# Gunakan gunakan hanya fungsi (Numerik-Aritmatik)
# + - x / // math floor ceil etc.
# Input : Masukkan 4 digit angka = 5493
# Outputnya : 9354


# 4.
# unakan gunakan hanya fungsi (Numerik-Aritmatik)
# Input :
# Masukkan 2 digit angka : 63
# Masukkan 2 digit angka kedua : 87

# Output : 6387

# Kondisi untuk soal 3 dan 4 tidak menerima inputan string, negatif, float

# Kirim Email jika server sudah UP