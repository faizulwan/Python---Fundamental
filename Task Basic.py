# #FAIZ ULWAN


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



# # #2 Practice

# # Sembilan belas tahun lalu, umur anak setengah tahun lebih muda dari seperempat umur ibunya.
# # Umur anak sekarang 19 tahun lebih tua dari sepertujuh umur ibunya.
# # Berapa usia ibu saat melahirkan anaknya?

# # Output : Usia Ibu ketika melahirkan anaknya adalah ... tahun

# import math as m

# tahun = 19 #19 tahun yang lalu
# anak = float((tahun - 0.5)/0.75)
# ibu = float((anak-19)*7)
# ibu_melahirkan = m.floor(ibu - anak)

# print (anak, ibu)
# print('Usian Ibu ketika melahirkan anaknya adalah', ibu_melahirkan, 'tahun')





# #3Practice
# Sekarang umlah usia budi + ayah = 50 tahun
# 4 tahun lalu, usia ayah budi 6 kali usia budi
# berapa usia ayah dan usia budi saat ini?
# Output : Usia ayah saat ini adalah ... tahun dan usia budi saat ini adalah ... tahun

total_age = int(input('Total age of Budi and Ayah : '))

ayah = int((6*total_age - 20)/7)
budi = total_age - ayah

print ('Usia Ayah saat ini adalah', ayah, 'tahun dan usia Budi saat ini adalah', budi, 'tahun')