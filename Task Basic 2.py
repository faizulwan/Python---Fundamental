#----------------TUGAS FAIZ ULWAN--------------------
#==================================================================================
#Practice 3.1
## Input the number of day
## Output : Declare the number of day in ...Year...Month...Week...Day
## 1 Year = 365, 1 Month = 30 Days

day = int(input('Input the number of days :'))

year = 365
month = 30
week = 7

tyear = day//year
rday = day%year

tmonth = rday//month
rday= rday%month

tweek = rday//week
rday = rday%week

print (f'{tyear} Year(s), {tmonth} Month(s), {tweek} Week(s), {rday} Day(s)')


#================================================================================
#Practice 3.2
## Input sentence and words
## Output : Total of x character in sentence (xxxxx) is 5
# Hari ini, HARi TIdAk MASuk kuLIAH
# masukkan karakter : a
# 5

# kalimat = str(input('Masukkan kalimat : '))
# kata = str(input ('Masukkan kata : '))
# kecil_kalimat = kalimat.lower()
# kecil_kata = kata.lower()

# print (kecil_kalimat.count(kecil_kata))


#=================================================================================
# #3.3 Prcatice
# Masukkan teks : Hari ini adalah hari rabu
# Masukkan hurf vokal : o

# Output : Horo ono odoloh....dst


# teks = str(input('Masukkan Teks : '))
# vokal = str(input('Masukkan Huruf vokal : '))

# teks2 = teks.replace('a',vokal)
# teks2 = teks2.replace('A',vokal)
# teks2 = teks2.replace('i',vokal)
# teks2 = teks2.replace('I',vokal)
# teks2 = teks2.replace('u',vokal)
# teks2 = teks2.replace('U',vokal)
# teks2 = teks2.replace('e',vokal)
# teks2 = teks2.replace('E',vokal)
# teks2 = teks2.replace('o',vokal)
# teks2 = teks2.replace('O',vokal)

# print(teks2)

#=================================================================================
# #3.4 Practice
# Hitung Body Mass Index
# Rumus BMI : Massa (kg) / tinggi (m) pangkat 2

# input:
# Masukkan tinggi badan (cm) :
# Masukkan massa (kg) :

# Kondisi
# - Nilai tinggi dan massa tidak boleh negatif ===> Keluar notif "Tidak menerima angka negatif"
# - Nilai tinggi dan massa tidak boleh string/decimal ===> Keluar notif "Angka yang anda masukkan salah"
# - Batas maksimal massa = 200 kg dan tinggi 300 cm ===> "Tinggi/massa yang Anda masukkan diluar batas"

# Output
# Sesuaikan dengan hasil
# BMI < 18.5 ===> Berat badan kurang
# 18.5 - 24.9 ===> Berat badan ideal
# 25 - 29.9 ===> Berat badan berlebih
# 30 - 39.9 ===> Berat badan sangat berlebih
# BMI >= 40 ===> Obesitas

# Tinggi badan anda.....m dan massa anda...kg 




# try :
#     tinggi = int(input('Masukkan tinggi badan Anda (cm): '))
#     berat = int(input('Masukkan berat badan Anda (kg): '))

#     meter = 100
#     tinggi2 = float(tinggi/meter)
#     tinggi2 **= 2
#     bmi = float(berat/tinggi2)
   
#     if(tinggi<0 or berat<0):
#         print('Mohon maaf tidak menerima nilai negatif')
#     elif(tinggi>200 or tinggi>300):
#         (print('Mohon maaf tinggi atau berat yang anda masukkan diluar batas'))
#     else:
#         if (berat>0 and tinggi>0 and bmi < 18.5):
#             print ('Tinggi Anda =', tinggi, 'm dan berat badan Anda =', berat, 'kg.'' Berat badan Anda kurang')
#         elif (berat>0 and tinggi>0 and bmi >= 18.5 and bmi <= 24.9):
#             print ('Tinggi Anda =', tinggi, 'm dan berat badan Anda =', berat, 'kg.'' Berat badan Anda ideal')
#         elif (berat>0 and tinggi>0 and bmi >= 25 and bmi <= 29.9):
#             print ('Tinggi Anda =', tinggi, 'm dan berat badan Anda =', berat, 'kg. ''Berat badan Anda berlebih')
#         elif (berat>0 and tinggi>0 and bmi >=30 and bmi < 40):
#             print ('Tinggi Anda =', tinggi, 'm dan berat badan Anda =', berat, 'kg. ''Berat badan Anda sangat berlebih')
#         else:
#             print ('Tinggi Anda =', tinggi, 'm dan berat badan Anda =', berat, 'kg. ''Berat badan Anda yang obesitas')

# except:
#     print ('Tidak menerima nilai negatif')







# ================================================================================
# #3.5
# Input :
# Masukkan Nilai : ....

# Kondisi :
# >90 = Grade A
# >85 = Grade A-
# >80 = Grade B
# >75 = Grade B-
# >70 = Grade C
# >65 = Grade D
# <65 : Anda Tidak lulus dan perlu remedial

# -Nilai Maksimum 100, nilai minimum 0
# -Jika nilai > 100 : Nilai diluar jangkauan
# -Jika nilai 0 : Tidak menerima nilai negatif
# -Jika inputan bukan angka : Angka yang anda masukkan salah
# - Bisa menerima desimal

# Output:
# Nilai Anda..... dan Anda ....Grade....

# try:
#     nilai = float(input('Masukkan Nilai Anda : '))

#     if (nilai >100):
#         print('Maaf nilai Anda diluar jangkauan')
#     elif (nilai <0):
#         print ('Maaf tidak bisa menerima nilai negatif')
#     else:
#         if(nilai>90):
#             print('Nilai Anda adalah ', nilai, ' dan Anda termasuk kedalam Grade A')
#         elif(nilai >85 and nilai <=90):
#             print('Nilai Anda adalah ', nilai, ' dan Anda termasuk kedalam Grade A-')
#         elif(nilai >80 and nilai <=85):
#             print('Nilai Anda adalah ', nilai, ' dan Anda termasuk kedalam Grade B')
#         elif(nilai >75 and nilai <=80):
#             print('Nilai Anda adalah ', nilai, ' dan Anda termasuk kedalam Grade B-')
#         elif(nilai >70 and nilai <=75):
#             print('Nilai Anda adalah ', nilai, ' dan Anda termasuk kedalam Grade C')
#         elif(nilai >=65 and nilai <=70):
#             print('Nilai Anda adalah ', nilai, ' dan Anda termasuk kedalam Grade D')
#         else:
#             print('Anda tidak lulus')

# except:
#     print('Nilai yang Anda masukkan salah')







# khumaeni@purwadhika.com
# Senin jam 12 siang