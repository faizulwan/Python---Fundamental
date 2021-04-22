# Data Structure ==> Data yang berisi beberapa data primitif atau struktur yang lain

# ---- Iterable Data


# Tipe Data primitif ==> Integer, Float, String, Boolean

# ### List, Tupple, Set, Dictionary

# #=====================================================================================================
# #List
# Menggunakan ==> [   ]
# List_A = [data1, data2, data3, data4, dst]

hari = ['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']
data = ['Senin', 'Selasa', 10.5, 3, True, ['Rabu', 'Kamis', 10, [9.8, 'Jumat', 'Minggu']]]

# print (hari)

# A = data [5][3][0]
# print (A)

# print(hari)

# #Cara akses/membaca element dalam list (satu elemen)
# #Menggunakan indexing ==? Urutan angka, dimulai dari NOL, berupa angka integer, Maksimal jumlah elemen terkahir - 1

# ##Jumlah data atau elemen dalam list

# print (len(hari))\

###Mengakses list dengan menggunakan looping

# for i in hari:
#     if i=='Jumat':
#         break
#     print (i)

##Untuk mengetahui index suatu elemen dalam list
# print (hari.index('Rabu'))

### Slicing
## Akses beberapa elemen list sekaligus
# namaList[Start : End : Step]
# Step secara default +1 (increment)

# [Start : End]
# Berlaku
# Start : Inclusive => Index yg ditentukan yang akan diakses
# End : Exclusive => Index yang akan diakses end -1 (Increment), end +1 (Decrement)

# [Index] => Akses Index tersebut ( Satu element)

# print (hari.index('Kamis'))
# print (hari.index('Selasa'))
# A = hari [3 : 0: -1]
# print (A)

# print(hari[1:3]) #Akan mengakses index 1 sampai dengan 2
# print(hari[2:]) #Akan mengakses index 2 sampai index terkahir Paling akhir)
# print (hari [ :4]) #Akan mengakses index awal sampai dengan indeks 3
# print (hari[:]) #Akan mengakses index 0 hingga paling akhir dengan increment/step +1
# print (hari[::-1]) #Akan mengakses index 0 hingga paling akhir dengan decrement/step -1

###Menambahkan elemen ke dalam list
###Fungsi append
# Syntax: NamaList.append(data)

# ###Fungsi Extend
# Syntax: NamaList.extend(data0)
#Penambahan data secara default akan ditambah di index terkahir

# bulan = ['Januari', 'Febuari', 'Maret', 'April', 'Mei', 'Juni','Juli']

# bulan.append('April')
# bulan.extend('Juni')
# print(bulan)

###Menambahkan data di index tertentu

###Fungsi Insert
#Syntax : NamaList.insert(Index, Datanya)

# bulan.insert(1, 'Monday')
# print(bulan)

##Mengubah/Mengupdate data/element tertentu dalam list
#Syntax : Namalist[index] Data yang akan diubah = data baru

# bulan[0] = 'Desember'

# print(bulan)

##Menghapus data dalam list
###Kita bisa menghapus berdasarkan data 
# Syntax: NamaList.remove(data) 
# bulan.remove('Januari')
# print(bulan)

###Kita bisa menghapus berdasarkan index
# # pop
# Syntax:Namalist.pop(index) data yang akan dihapus adalah index terakhir

# # bulan.pop(1)#menghapus index 1, dst.
# bulan.pop(1)
# print (bulan)

#==========================================================================================================

# number = [23,45,123,54,321,7,56,345,32,9,7,5,45,34]

# print(max(number))
# print(min(number))
# print(sum(number))
# print(number.count(45)) #Untuk mencari modus nanti
# number.sort(reverse=True)
# print (number)

# #======================== Assignment
# Mini Aplikasi
# CRUD - Create - Read - Update - Delete

# Aplikasi mini untuk data barang/elektronik/buah/ATK dll

# ----- Apps awal di RUn - Akan meminta Login (Password)
# ---Batas 4x percobaan isi Password
# --Jika Salah password samapai 4x ->Keluar Aplikasi

# Jika Password benar :
# Akan keluar menggunakan

# ---Menu---
# 1. Cetak isi Daftar Barang (Read)
# 2. Menampilkan data barang (Create)
# 3. Mengubah data barang (Update)
# 4. MEnghapus data barang (delete)
# 5. Exit (Keluar APPS)

# ---Terms & Condition---
# 1. Read (Cetak Data)
# - Jika tidak ada data akan keluar notif "Daftar Barang Masih Kosong"
# -Jika ada Data, Akan menampilkan seluruh barang

# 2. Create (Tambah Data)
# -Pengecekan jenis data, Jika salah format : 'Data yang Anda Masukkan Salah
# -Pengecekan Duplikasi:
# Jika ada data sebelumnya makan keluar notif => 'Data sudah ada, Apakah tetap akan disimpan? (Y/N)'
# Y : Keluar Notif = 'Data Akan disimpan'
# N : Keluar notif = 'Data tidak disimpan'

# - Ketika data berhasil disimpan keluar notif = 'Data berhasil disimpan'

# 3. Update (Ubah Data)
# - Program akan meminta user memasukkan data yang akan diupdate
# -Jika data yang diminta user tidak ada keluar notif : 'Data Barang tidak ada'
# -Jika barang ada => Update datanya ==> Jeruk -- Jeruk Bali
# berhasil-Keluar notif : Data terupdate/Data berhasil diubah

# 4. Delete (Hapus Data)
# - Program akan meminta user memasukkan data yang akan dihapus
# -Jika data yang diminta user tidak ada maka keluar notif : 'Data Barang tidak ada'
# -Jika barang ada ==> Hapus seluruh data yang sesuai dengan inputan user

# 5. Exit
# -Selama user belum memilih opsi ini, maka menu harus terus ditampilkan

# Setelah 