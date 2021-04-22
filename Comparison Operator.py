# ====Comparison Operator
# Output = TRUE and False

# == : Equal to
# != : Not equal to
### == and != opeator dont need use integer

### Operator below must be use an integer or a float
# <  : less than
# >  : Greater than
# <= : less than equal to
# >= : Greater than equal to

# a = 5
# b = '5'

# print (a == b)
# print (a != b)
# print (a > b)



# =====Logical Operator
# Output = TRUE and False
# and
# or
# not ==> negasi ==> will be shown as a reverse Not TRUE = False, Not FALSE = TRUE

# a AND b ==> will be TRUE if a and b is TRUE
# a OR b ==> will be false if both a and b are false
# a NOT b


# ====Combined Operator
# # Variable must be defined
# number = 15

# number += 5  ==== number = number + 5
# number -= 4  ==== number = number - 4
# number *= 2  ==== number = number * 2
# number /= 10 ==== number = number / 10
# pow (2,3) ==> 2**3 ==> number **= 2 ====== 8
# number %= 7  ==== number = number % 7


# =====Membership Operators
# Ouput : True or False
# #in
# #not in

# name = 'My name is Faiz Ulwan and I live in Jakarta'

# # print('My' in name)
# # print ('bandung' not in name)

# print (name.replace("a","o"))
# print (name.split(' ', 3))   ###Divide string based on anything you want
# print (name.split('and'))    ###Divide string based on word
# print (name.count ('a'))     ###How many character that shown in your string

#==========================================================================================================

#Practice 3.1
## Input the number of day
## Output : Declare the number of day in ...Year...Month...Week...Day
## 1 Year = 365, 1 Month = 30 Days

# day = int(input('Input the number of days :'))

# year = 365
# month = 30
# week = 7

# tyear = day//year
# rday = day%year

# tmonth = rday//month
# rday= rday%month

# tweek = rday//week
# rday = rday%week

# print (f'{tyear} Year(s), {tmonth} Month(s), {tweek} Week(s), {rday} Day(s)')



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


# ====IF Statement
# Pengecekan Kondisi

# Basic Syntax
# if ...(Kondisi)... : Kondisi harus bernilai true agar dijalankan
#    .....program..... Jika ada 1 ketentuan


# if ...(Kondisi)... :
#     Program u/ ketentuan pertama
# else:
#     Program untuk ketentuan kedua

# nilai = 77

# if (nilai > 85):
#     print ("Anda Lulus")
# elif (nilai >70 and nilai<85):
#     print ("Anda Selamat")
# else:
#     print ('Anda Gagal')

# ##Nested IF
# Ada IF dalam IF

nilai = 90
gender = 'Male'

if (nilai > 85):
    if (gender == 'Male'):
        print ("Mahasiswa Teladan")
elif (nilai >70 and nilai<85):
    print ("Anda Selamat")
else:
    print ('Mahasiswi Teladan')


#Error Handling

nilai = 'Senin'
try:
    if nilai > 75:
        print('Anda Lulus')
    else:
        print("Anda Gagal")

except:
    print ('Nilai yang ada masukkan salah')

# try:
#     Kondisi yang akan dilakukan Pengecekan
# except:
#     Program yang akan di run dika ada error di kondisi