nilai = {"andi" : 80,
        "andre" : 75,
        "beni" : 85,
        "bondan" : 90,
        "joko" : 87,
        1 : ["Rendi", 80]}
'''
print (nilai)

print(nilai["andi"])
print(nilai[1])

print (list(nilai.keys())) #Mencetak keys dalam bentuk list
print (list(nilai.values())) #Mencetak  values dalam bentuk list
'''
# print(nilai['cici'])
# print(nilai.get('andi', "Data tidak ada"))
# print(nilai.get('cici','Data tidak ada'))


## Create - Menambah Data
# Basic Syntax: namaDict[Keyword] = Values

nilai['faiz'] = 1800

# print (nilai['faiz'])



# ## Update - Mengubah data
# # Basic Syntax = namaDisct[Keyword] = values
# # Keyword => Menggunakan Keyword Lama, sebelumnya sudah ada 
# # - Key Lama yg Value nya akan diupdate
# # - Value => Value Baru untuk Mengupdate Value Lama 

# nilai['andi'] = 1800
# print (nilai['andi'])
# print(nilai)

# nilai.update({"faiz" : 1000})

# print(nilai)

# A = nilai["beni"]

# nilai["jacky"] = A

# # print(nilai)


# for i in nilai.keys():
#     if i == 'jacky' or i == 'beni':
#         nilai[i] = 999

# print (nilai)

### Delete - Hapus Data ==> Akann menghapus 1 items
# Basic Syntax: nilai.pop(Keys)

# print (nilai.get("faiz","Data tidak ada"))
# print (nilai)

# nilai.pop(1)

# DaftarNilai = list(nilai.values())
# # print (DaftarNilai)
# DaftarSiswa = list(nilai.keys())
# # print (DaftarSiswa)
# NilaiSiswa = list(nilai.items())
# # print (NilaiSiswa)

# # nama = str(input('Masukkan nama siswa : '))
# # nilai = nilai.get(nama, 'Siswa yang anda cari tidak ada')

# # print("Nilai dari : ", (nama), " adalah : ", (nilai))

# nilai_baru = {}

# A = len(DaftarSiswa)
# for i in range (A):
#     nilai_baru[DaftarSiswa[i]]=NilaiSiswa[i]
# print (nilai_baru)

### Kamus Hari
Hari = {"Senin" : "Monday",
        "Selasa": "Tuesday",
        "Rabu": "Wednesday",
        "Kamis": "Thursday",
        "Jum'at":"Friday",
        "Sabtu" : "Saturday",
        "Minggu" : "Sunday"
}



try:    
    a = str(input(" Masukkan nama hari/day : "))
    a1 = a.title()
    hari = list(Hari.keys())
    day = list(Hari.values())

    if a1 in hari:
        eng = Hari[a1]
        print (a1+ " dalam bahasa inggris adalah "+ eng)
    else:
        ind = hari[day.index(a1)]
        print (a1+ ' in bahasa is '+ ind)

except:
    print ("Nama hari yang Anda masukkan salah")