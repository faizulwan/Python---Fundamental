# ##Input() => Program can recieve an input from user
# x = input('Whats your name : ')
# y = input('Whats your age: ')
# print(x)
# print(y)
# All of the input will assign as a STRING

# a = 'faiz ulwan'
# b = 'AULIA MUTHIA'
# c = 22

# # print(a.capitalize()) ## Capitilize first letter
# # print(a.title()) ## Capitalize every first letter
# # print(a.lower()) ## all turn into lower case
# # print(a.upper()) ## all turn capital

# # #Alt 1
# # print ("My name is", a, 'I\'m', c, 'years old') ##Combine with variable

# # #Alt 2
# # print ('My name is ' + a + ', I\'m ' + str(c) + ' years old')

# # We can apply mathematical operator, but only (+) and (*)
# # (+) We only plus string by string
# # # (*) string with int
# # print (a + b) #Concat => String combining 
# # print (a * 3) #String will be shown 3 times

# #Alt 3
# print("My name is {} and I\'m {} years old".format(a,c))

# #Alt 4
# print (f"My name is {a} and I\m {c} years old")


## Math Operator
# print (5 + 10)
# print (10 - 7)
# print (5 * 8)
# print (10 / 2) ## Will be shown as a float
# print (10 / 3) ## Will be shown as a float
# print (10 // 3) ## will be shown as an integer
# print (10 %4)

# # Basic Syntax : round (number, significant figure)
# print(round(3.749385, 2)) #If there is no decimal, will be assign as an integer





# #1 Practice
# # Number of chicken + goat = 13
# # number of chicken's feet + goat's feet = 32
# # How many chicken and goat ?

# total_animals = int(input ('Total number of chicken and goat : '))
# total_feets = int (input ('Total number of chicken and goat\'s feet : '))
# c_feet = 2
# g_feet = 4

# goat = int(total_feets/c_feet - total_animals)
# chicken = int((total_animals - goat))

# print('Jumlah ayam ', chicken, 'ekor dan jumlah kambing', goat, ' ekor'  )



# #2 Practice



# Sembilan belas tahun lalu, umur anak setengah tahun lebih muda dari seperempat umur ibunya.
# Umur anak sekarang 19 tahun lebih tua dari sepertujuh umur ibunya.
# Berapa usia ibu saat melahirkan anaknya?

# Output : Usia Ibu ketika melahirkan anaknya adalah ... tahun

import math as m

tahun = 19 #19 tahun yang lalu
anak = float((tahun - 0.5)/0.75)
ibu = float((anak-19)*7)
ibu_melahirkan = m.floor(ibu - anak)

print (anak, ibu)
print('Usian Ibu ketika melahirkan anaknya adalah', ibu_melahirkan, 'tahun')

# #3Practice
# Sekarang umlah usia budi + ayah = 50 tahun
# 4 tahun lalu, usia ayah budi 6 kali usia budi
# berapa usia ayah dan usia budi saat ini?
# Output : Usia ayah saat ini adalah ... tahun dan usia budi saat ini adalah ... tahun

# total_age = int(input('Total age of Budi and Ayah : '))

# ayah = int((6*total_age - 20)/7)
# budi = total_age - ayah

# print ('Usia Ayah saat ini adalah', ayah, 'tahun dan usia Budi saat ini adalah', budi, 'tahun')



# ###Kirim email ke khumaeni@purwadhika.com (dalam bentuk file python)


# --- Library - Package - Module ---
# A program is made by user either individual person or group
# There is a several package that already installed in Python (or Built in Package)
# Several package/library that has not already install we need to install first

#How to use package in Python
##Alt1. import math
# import math
# print(math.pi) ##Show phi value
# print(math.pow(2,3)) ##Show pangkat
# print(math.floor(4.6)) ##
# print(math.ceil(2.3))
# print(math.sqrt(36))

##Alt2. import maths as m
# import math as m #Giving alias
# print(m.pi) ##Show phi value
# print(m.pow(2,3)) ##Show pangkat
# print(m.floor(4.6)) ##
# # print(m.ceil(2.3)) ##
# # print(m.sqrt(36)) ##squareroot

# ##Alt3. from math import pow, floor, ceil, sqrt, etc....
# from math import pow, floor, ceil, sqrt
# print (floor(5.8))
# print (pow(3,3))
# print (ceil(6.3))

# nama = 'Faiz Ulwan'
# usia = '25'

# print (nama.isalnum()) ## Mengandung seluruhnya adalah alfa numeric
# print (usia.isdigit()) ## Apakah seluruh elemen adalah digit/angka
# print (usia.isalpha()) ## Apakah seluruh elemen adalah alfabet
# print (nama.islower()) ## Apakah seluruh elemen lower case
# print (nama.isupper()) ## Mengecek apakah seluruh elemen upper case