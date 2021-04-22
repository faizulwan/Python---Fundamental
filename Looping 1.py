##Looping

#while looping ===> 
#for looping ===> 

#Looping sangat mirip dengan if karena sama-sama sangat membutuhkan conditional statement
# IF ==> Program akan dijalankan hanya satu kali (Kondisi bernilai TRUE)
# Looping ==> Program akan dijalankan beberapa kali/berulang kali/iterasi (selama kondisi TRUE)
# Looping akan digunakan => Ketika kita ingin menjalankan program yang sama berulang kali

# Jenis Looping"
# While Loop

# Basic Syntax :
# While....Kondisi (Conditional Statement)...: Selama Kondisi Bernilai TRUE, Program akan di 
#....Program...

# angka = 1  ##Define Variabel yangg akan dilakukan pengecekan kondisi
# while angka < 10 and nilai >90: ##Proses Looping akan dihentikan, ketika kondisi bernilai FLASE
#     # angka = angka + 1
#     print(angka)
#     angka += 1 ##Increment => Penambahan 1, Kita lakukan Manual

# n=1  #Untuk while harus mendefine kondisi awal
# while n<11:
#     print("Hello World")
#     n+=1 #Buat increment/decrement
#      manual
# print("Hello World")

#Tahapan Looping => iterasi => Iterable Object
# Iterasi Ke-1 : angka = 1

# print 1

# Iterasi ke-2 : angka = 2
# print 2

# Iterasi ke-3 : angka = 3
# ....
# ....
# ....

# Iterasi ke-8 : angka = 8
# print 8

# Iterasi ke-9 : angka = 9
# print 9

# Iterasi ke-10 : angka = 10


#==================================================== Tebak Angka
# angka = 5897

# tebak = '' #untuk inisiasi pertama agar program jalan x
# while tebak != angka:
#     tebak = int(input ('Masukkan Angka: '))
#     if tebak == angka:
#         print ('Tebakan Berhasil')
#     elif tebak > angka:
#         print('Angka tebakan terlalu besar')
#     elif tebak< angka:
#         print ('Angka tebakan terlalu kecil')
#     else:
#         print('tebakkan Salah')


#Menu Aplikasi....
...
...
...
# 5 Exit

# password = 'andi2345'
# login = ''
# coba = 1
# batas_coba = 5

# while login != password:
#     if coba <= batas_coba:
#         login = input('Masukkan Password Anda: ')
#         if login != password and coba < batas_coba:
#             coba += 1
#             print(f"Password Salah, Silahkan coba lagi percobaan ke-{coba}")
#         elif logi !=password and coba == batas_coba:
#             coba += 1
#             print (f'Password Salah, dan Kesempatan habis')
#         else:
#             print ("Password Benar, Anda Berhasil Login")

# Lat:

# #SOAL 1
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# i=1
# n=6
# while (i<n):
#     j = 1
#     while (j<=i):
#         print (i, ' ', end='')
#         j += 1
#     print()
#     i+=1


# #SOAL 2
# 5 5 5 5 5
# 4 4 4 4 
# 3 3 3
# 2 2
# 1

# i=5 
# while (i>0):
#     print((str(i) + ' ') *i)
#     i-= 1

# i=1
# while i<6:
#     print((str(i) + ' ')*i)
#     i+=1





#=========================================================================================================================
#### For Loop
# Pada for dapat dilakukan increment/decrement secara otomatis
# -Inisiasi awal looping tidak harus mendefine Variabel

# Basic Syntax
# for ....variabel....in....iterable object/data: ### Looping akan dijalankan hingga seluruh Data iterable diakses
#     .....program.... ### Program akan dijalankan selama data iterable diakses (kondisi TRUE)

#     Iterable object/data ==> data/object yang isinya lebih dari 1 ==> Sebagian besar dapat dilakukan indexing

#     for

'''
angka = range(10)
print(angka)

#Range mirip seperti indexing dan berisi angka/numerik berupa integer

range(START, END, STEP)

range(10) ##Ketika di dalam range, angka hanya 1, angka tersebut adalah stop
## Default START = 0
## Default STEP = 1 ==> Secara default berarti penambahan sebanyak 1 (increment)

range (1,10)  ### Ketika di dalam range angka hanya 2, angka tersebut adalah START dan STOP
##Default STEP = 1
Mengikuti aturan inclusive dan exclusive
START = inclusive
END = Exclusive = Akses akan berhenti sampai di END - 1

range (1,21,2)  ##Start = 1, END = 21 (Akses akan berhenti di 21 - 1)
range (20, 1, -1)
'''

# for i in range (10):
#     print(i)
    
# ##in ==> Membership operator menghasilkan TRUE dan FALSE
# print('=' * 50)

# i=1
# while i<10:
#     print(i)
#     i+=1

# print('=' * 50)
# for i in range (3,10): ##Ketika step increment, exclusive (END -1)
#     print(i)

#-For secara natural dengan sendirinya bisa mendapatkan kondisi false (Menghentikan proses looping) === Limited looping
#- While tidak bisa mendapatkan kondisi False kecuali kita tentukan ==> Bisa unlimited looping

# for i in range (10,1,-1): ##Ketika step decrement, exclusive (END +1)
#     print(i)

#======================================================================================================================================
###Syntax tambahan dalam looping
# 1. Break ==> untuk menghentikan proses looping secara paksa
# Secara normal/natural ==> Looping akan berhenti ketika kondisi bernilai false
# Break biasanya dipasangkan dengan key statement

# for i in range (0,11): #Iterasi ketika i = 5
#     print(i) #Print 5
#     if i == 5:
#         break #looping dihentikan

# print('='*70)
# for i in range (0,11): #Iterasi i = 5
#     if i == 5:
#         break #Loooping dihentikan
#     print(i)


#2. Continue
# Continue biasanya dipasangkan dengan if statement.
# Menghentikan sementara proses looping atau tahapan iterasi langsung ke iterasi ke iterasi berikutnya

# for i in range (0,11): 
#     print(i) 
#     if i == 5:
#         continue #Looping dihentikan dan langsung menuju iterasi berikutnya 

# print('='*70)

# for i in range (0,11): #Iterasi i = 5
#     if i == 5:
#         continue #Loooping dihentikan
#     print(i) ##Ketika i = 5 akan diskip dan akan lanjut ke iterasi berikutnya

# BREAK = Looping akan dihentikan secara paksa sesuai kondisi if yang di statement
# CONTINUE = Tahapan iterasi dari looping dihentikan, kemudian lanjut ke iterasi berikutnya

###ELSE
#Perintah atau  program dibawah else akan dijalankan ketika looping berhenti secara natural

# n = 5
# for i in range (20):
#     print(i)
#     if i == n:
#         print('Data Ditemukan')
#         break
#     else:
#         print('Data tidak ditemukan')

# print('Perintah di luar looping')

# angka = range(10)
# for i in angka:
#     print (i)
#     for j in angka:
#         print (j)
#         for k in angka:
#             print(k)

for i in range (4,20,4):
    for j in range (1,10):
        print ('*' *i)
    print(i)