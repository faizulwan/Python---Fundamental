#==============================================================================================================================================================================
#Menu : Read

provinsi = ['Nanggroe Aceh Darussalam', 'Sumatera Utara', 'Sumatera Barat', 'Riau', 'Kepulauan Riau', 'Jambi', 'Bengkulu', 'Sumatera Selatan', 'Kepualauan Bangka', 
            'Lampung', 'Banten', 'Jakarta', 'Jawa Barad', 'Jawa Tengah', 'Jawa Timur', 'Yogyakarta', 'Bandung']

# if not provinsi:
#     print('Data tidak ada')
# else:
#     print('Ada data')

# #==============================================================================================================================================================================
#Back to main menu

# print ('''
# 1. Kembali ke menu utama
# 2. Kembali ke sub-menu Read''')

# menu = int(input('Pilih menu: '))
# if (menu==1):
#     print('=> Kembali ke menu utama <=')
# elif (menu==2):
#     print('=> Kembali ke sub-menu Read <=')
# else:
#     print('=> Menu tidak tersedia <=')

#==============================================================================================================================================================================
#Menu : Update
l_provinsi = [i.lower()for i in provinsi]
print (l_provinsi)
cek = str(input('Masukkan data yang ingin Anda update :'))
l_cek = cek.lower()

for j in l_provinsi:
    if j == l_cek:
        print ('Data ada')
        print ('''Apakah Anda ingin mengupdate data tersebut :
        1. Ya
        2.Tidak''')
        
        question = int(input('Pilih opsi : '))
        if (question==1):
            update = str(input('Update menjadi : '))
            a = l_provinsi.index(l_cek)
            l_provinsi[a]=update
            print('=> Data berhasil di update <=')

        elif (question==2):
            print('=> Data tidak di update <=')

        else:
            print('=> Pilihan tidak ada <=')
        break
    else:
        print('Data belum data')

l_provinsi = [x.title() for x in l_provinsi]
print (l_provinsi)




# for i in provinsi:
#     if i == 

