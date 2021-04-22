
# Data Structured
# List_A = [1,2,3]  => list()
# Tuple_A = (1,2,3) => tuple()
# Set_A = {1,2,3}  => set()

# ### Dictionary - Asosiasi - Mapping
# Kamus
# Kata : Definisi
# Keyword : Definition
# Key : Value
# -Yang memisahkan key dan value adalah tanda (:)
# -Key + value ==> Item ==> Gabungan antara key dan value
# -Yang memisahkan antar item adalah tanda (,)

# Key = umumnya berupa string atau integer
# Value = Bisa berbentuk tipe data apapun

# List ==> Menggunakan Index (Integer - Numerik)
# Dict ==> Menggunakan Key - 'Nama'


# Dict_A = {}
# Dict_B = dict()

# Data = {key : value, 
#         key2 : value2,
#         key3 : value3,
#         key4 : value4}

# nilai = {'Andi' : 80,
#         'Andre' : 75,
#         'Beni' :  85,
#         'Bondan' : 90,
#         'Joko' : 87,
#         1 : ['Rendi', 80]}

# # ## Read - Baca-Akses Data
# # Basic Syntax :
# # NamaDictionary[Keyword]

# # print(nilai['Andi'])
# # print (nilai[1])

# # print (nilai) #Mencetak dictionary
# # print (list(nilai.keys())) #Mencetak keys dari dictionary
# # #Kemudian mengubahnya menjadi list
# # print (nilai.values()) #mencetak values dari dictionary
# # print(nilai.items()) ##Mencetak items dari dictionary

# # print (nilai['Beni']) ##Akan keluar error jika tidak ada key

# # ##Alternatif lain untuk mengakses dictionary
# # print (nilai.get('Andi'))
# # print (nilai.get('Cici', 'Tidak Ada')) ##Jika data tidak ada, tidak memunculkan error
# # print (nilai.get('Bondan', 'Tidak Ada'))



# # ### Create - Menambah Data
# # # Basic Data :
# # # namadict[keywird] = values

# # print(nilai.get('Joni', 'Data tidak ada'))
# # nilai ['Joni'] = 84

# # print (nilai ['Joni'])


# # ### Update - Mengubah Data
# # Basic Syntax :
# # namaDict[keywird] = Value
# # -Keyword => Menggunakan keyword lama, sebelumnya sudah ada
# # -Key lama yang valuenya akan diupdate
# # -Value => Value baru untuk mengupdate value lama

# print(nilai)
# nilai['Joni'] = 95
# print (nilai)
















# ### Kamus Hari
# Hari = {"Senin" : "Monday",
#         "Selasa" : "Tuesday",
#         "Rabu" : "Wednesday",
#         "Kamis" : "Thursday",
#         "Juma'at" : "Friday",
#         "Sabtu" : "Saturday",
#         "Minggu" : "Sunday"
#         }

# print (list(Hari.items()))

# item_Hari = list(Hari.items())

# for hari, day in item_Hari:      ## Unpacking atau mengambi item dari dictionary
#         print(hari, "dan", day)

# hari = input("Masukkan nama hari : ")
# eng = Hari [hari]
# print (f"Hari {hari} dalam bahasa inggris adalah {eng}")

##Latihan Auoto Translator

# Input :
# Masukkan nama hari :

# Kondisi
# -Tidak case sensitif
# -Tidak menerima inputan bukan hari (ex: int, float, dll)

# Keluar notif : Nama yang anda masukkan salah

# output:
# tergantung inputan
# -jika inputan hari dalam bahasa indo
# ===>(f"Hari {hari} dalam bahasa inggris adalah {eng}")
# -jika inputan hari dalam bahasa inggris
# ===>(f"{eng} in bahasa is {hari}")


# ### Kamus Hari
# Hari = {"Senin" : "Monday",
#         "Selasa" : "Tuesday",
#         "Rabu" : "Wednesday",
#         "Kamis" : "Thursday",
#         "Juma'at" : "Friday",
#         "Sabtu" : "Saturday",
#         "Minggu" : "Sunday"
#         }


# print ("AUTO -TRANSLATOR")

# try: 
#         masukkan = str(input('''Masukkan nama hari/Input the day : ''')).lower()

#         indo = list(Hari.keys())
#         eng = list(Hari.keys())

#         if masukkan in indo:
#                 day = Hari [masukkan]
#                 print ("Hari ", (masukkan), " dalam inggirs adalah ", (day))
#         else:
#                 indoday = indo[eng.index(masukkan)]
#                 print ((masukkan), " in Indonesia is ", (indoday))

# except:
#         print("inputan salah")



member1 = { 
        "name" : "Faiz",
        "email" : "faiz@gmail.com",
        "pass" : "faiz123",
        "username" : "faiz123",
        "age" : 22,
        "is_married" : False,
        "height" : 172.5,
        "weight" : 59.5,
        "job" : "Data Analyst",
        "cars" : ["Alphard", "Xenia", "Jazz"],
        "address" :{
                "street" : "East Independence",
                "RT" : 6,
                "RW" : 4,
                "No" : 20,
                "City" : ["West Jakarta", "East Jakarta", "South Jakarta"],
                "Zipcode" : 58647,
                "geo" : {
                        "lat" : 58.69,
                        "lng" : [89.25, 63.58, 60.80, [25.2, 98.7]]
                }
        }
}

member2 = { 
        "name" : "Andi",
        "email" : "andi@gmail.com",
        "pass" : "adi123",
        "username" : "adi123",
        "age" : 22,
        "is_married" : False,
        "height" : 172.5,
        "weight" : 59.5,
        "job" : "Data Analyst",
        "cars" : ["Alphard", "Xenia", "Jazz"],
        "address" :{
                "street" : "East Independence",
                "RT" : 6,
                "RW" : 4,
                "No" : 20,
                "City" : ["West Jakarta", "East Jakarta", "South Jakarta"],
                "Zipcode" : 58647,
                "geo" : {
                        "lat" : 58.69,
                        "lng" : [89.25, 63.58, 60.80, [25.2, 98.7]]
                }
        }
}

daftar_anggota = {
                101 : member1,
                102 : member2,
}

member1["username"]
member1["login"]


##Kita akan akses 98.7
print (member["name"])
print (member["height"])
print (member["is_married"])
print (member["cars"][1])

print (member["address"]["street"])
print (member["address"]["No"])
print (member["address"]["City"][1])
print (member["address"]["geo"]["lat"])
print (member["address"]["geo"]["lng"][2])
print (member["address"]["geo"]["lng"][3][1])

member["cars"][1] = "HR-V"
print (member["cars"][1])
print (member["cars"])

member["address"]["geo"]["lng"][3][1] = 1800
print (member["address"]["geo"]["lng"])