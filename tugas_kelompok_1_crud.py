##TUGAS KELOMPOK APLIKASI CRUD

# JUDUL APLIKASI
print('='*10+"APLIKASI CRUD DAFTAR PROVINSI"+'='*10)


# MENU LOGIN
password = "test123"
login = ""
coba = 1
batas_coba = 3

while login != password and coba <= batas_coba:
    if coba <= batas_coba:
        login = input("\nMasukkan password Anda: ")
        if login != password and coba == batas_coba-1:
                coba += 1
                print(f"Password salah. Silakan coba Lagi: percobaan ke-{coba}. Pastikan benar. Ini adalah kesempatan terakhir.")
        elif login != password and coba < batas_coba:
                coba += 1
                print(f"Password Salah. Silakan coba Lagi: percobaan ke-{coba}.")
        elif login != password and coba == batas_coba:
                coba +=1
                print(f"Password Salah dan Kesempatan Habis. Anda akan otomatis keluar dari aplikasi.")
                opsi_menu_awal = 5
        else:
                print("Password Benar, Anda Berhasil Login.")
                opsi_menu_awal = ' '



#MENU UTAMA
provinsi = ['Nanggroe Aceh Darussalam', 'Sumatera Utara', 'Sumatera Barat', 'Riau', 'Kepulauan Riau', 'Jambi', 'Bengkulu', 'Sumatera Selatan', 'Kepualauan Bangka', 'Lampung', 'Banten', 'Jakarta', 'Jawa Barad', 'Jawa Tengah', 'Jawa Timur', 'DI Yogyakarta', 'Bandung']
l_provinsi = [i.lower()for i in provinsi]
opsi_read = ''
opsi_create = ''
opsi_update = ''
opsi_delete = ''
opsi_exit = ''

while opsi_menu_awal == ' ' or opsi_create == 1 or opsi_read == 1 or opsi_exit == 'Y' or opsi_delete == 1: #or opsi_delete == 1 or opsi_update == 1 :
    print()
    print('----------MENU UTAMA----------')
    print('''
    1. Read
    2. Create
    3. Update
    4. Delete
    5. Exit
    ''')
    opsi_menu_awal = int(input('Masukkan pilihan Submenu (1, 2, 3, 4, atau 5): '))



    ## Submenu READ
    opsi_read = ' '
    while opsi_menu_awal == 1 or opsi_read == 2:
        if not provinsi:
            print('=> TIDAK ADA DATA <=')
        else:
            print('\n=> DATA TERSEDIA <=')
            print(f'Berikut adalah data daftar provinsi:\n{[x.title() for x in l_provinsi]}')
        
        print('''\n----------------------------
        Pilih opsi: 
        1. Kembali ke Menu Awal 
        2. Kembali ke Submenu Read
        ''')
        opsi_read = int(input('Opsi: '))
        opsi_menu_awal = ' '



    ## Submenu CREATE
    opsi_create = ' '
    while opsi_menu_awal == 2 or opsi_create == 2:
        print('\n----------Submenu CREATE----------\n')
        opsi_create = " "
        # CEK FORMAT DATA INPUTAN
        while opsi_create is " " or opsi_create == 2:
            input_create = str(input('Masukkan data: '))
            l_input_create = input_create.lower()
            if input_create.isalpha() == False:
                print('Format data yang Anda masukkan salah')
            else:
                print(f'Anda memasukkan {input_create.title()} ke dalam daftar provinsi')
                break

        for i in l_provinsi:
                    if i == l_input_create:
                        print('\nData sudah ada dalam daftar provinsi. Apakah data akan tetap dimasukkan?')
                        input_duplikasi = input('Y/N: ')
                        if input_duplikasi == 'Y':
                            l_provinsi.append(l_input_create)
                            print('=> DATA BERHASIL DISIMPAN <=')
                            print(f'\nBerikut adalah daftar provinsi setelah penambahan data: \n{[x.title() for x in l_provinsi]}')
                            break
                        else:
                                print('=> DATA TIDAK DISIMPAN <=')
                                break
                    elif i != l_input_create and i == l_provinsi[-1]:
                        l_provinsi.append(l_input_create)
                        print('\nDATA BERHASIL DISIMPAN')
                        print(f'\nBerikut adalah daftar provinsi setelah penambahan data: \n{[x.title() for x in l_provinsi]}')
                        break
                    # else:
                    #     print('', end=' ')        

        print('''\n----------------------------
        Pilih opsi: 
        1. Kembali ke Menu Awal 
        2. Kembali ke Submenu Create
        ''')
        opsi_create = int(input('Opsi: '))
        opsi_menu_awal = ' '           


    #Submenu UPDATE
    while opsi_menu_awal == 3 or opsi_update == 2:
            print('\n----------Submenu UPDATE----------\n')
            input_update = str(input('Masukkan data yang ingin Anda update: '))
            l_input_update = input_update.lower()
            for j in l_provinsi:
                if j == l_input_update:
                    print ('Data ada')
                    print ('''Apakah Anda ingin mengupdate data tersebut :
                    1. Ya
                    2. Tidak''')
                    
                    question = int(input('Pilih opsi : '))
                    if (question==1):
                        update = str(input('Update menjadi : '))
                        a = l_provinsi.index(l_input_update)
                        l_provinsi[a]=update
                        print('=> DATA BERHASIL DIUPDATE <=')
                        print(f'\nBerikut adalah daftar provinsi setelah pembaharuan data: \n{[x.title() for x in l_provinsi]}')

                    elif (question==2):
                        print('=> DATA TIDAK DIUPDATE <=')

                    else:
                        print('=> DATA TIDAK ADA DI DAFTAR PROVINSI <=')
                    break
                elif j != l_input_update and j == l_provinsi[-1]:
                    print('=> DATA TIDAK ADA DI DAFTAR PROVINSI <=')
                    break
                else:
                    continue
            
            print('\n----------------------------\nPilih opsi: \n1. Kembali ke Menu Awal \n2. Kembali ke Submenu Update')
            opsi_update = int(input('Opsi: '))
            opsi_menu_awal = ' '    



    #Submenu DELETE
    opsi_delete = ' '
    while opsi_menu_awal == 4 or opsi_delete == 2:
        print('\n----------Submenu DELETE----------\n')
        input_delete = str(input('Masukkan data yang ingin dihapus: '))
        l_input_delete = input_delete.lower()
        for i in l_provinsi:
            if i == l_input_delete:
                l_provinsi.remove(l_input_delete)
                print('=> DATA BERHASIL DIHAPUS <=')
                print(f'\nBerikut adalah daftar provinsi setelah penghapusan data: \n{[x.title() for x in l_provinsi]}')
                break
            elif i != l_input_delete and i == l_provinsi[-1]:
                print('=> Data tidak ada dalam daftar provinsi <=')
                break

        print('''\n----------------------------
            Pilih opsi: 
            1. Kembali ke Menu Awal 
            2. Kembali ke Submenu Delete
            ''')
        opsi_delete = int(input('Opsi: '))
        opsi_menu_awal = ' '



#Submenu EXIT
opsi_exit = ' '
while opsi_menu_awal == 5 or opsi_exit == 2:
        print('\n----------EXIT----------\n')
        print('=> ANDA KELUAR DARI APLIKASI <=')
        break