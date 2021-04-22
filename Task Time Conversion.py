###SOAL UJIAN 1###
'''
Buatlah sebuah return function dengan 1 argumen yang akan menerima inputan bilangan integer(Seconds). Dan akan menghasilkan output string dengan format waktu ("HH:MM:SS").
HH : Hours, 2 digits, range: 00 - 99
MM : Minutes, 2 digits, range: 00 - 59
SS : Seconds, 2 digits, range: 00 - 59

Case Flow: Saat dieksekusi, program akan mencetak nilai return function.
'''




app = 1  # Inisiasi awal untuk kondisi while

while app != 0:  # Kondisi while agar program tidak perlu dirunning ulang
    try:   
        print ("===========Mesin Konversi Waktu===========")
        inputan_detik = int(input("Masukkan jumlah detik yang ingin dikonversi : "))  # Fungsi agar user dapat menginput banyaknya detik

        def timeConverter (inputan_detik):  # Fungsi Konversi Waktu
            jam = inputan_detik//3600       # Menentukkan banyaknya jumlah jam
            sisajam = inputan_detik%3600    # Hasil sisa bagi jumlah jam
            menit = sisajam//60             # Menentukkan banyakanya jumlah menit
            sisamenit = sisajam%60          # Hasil sisa bagi jumlah menit
            detik = sisamenit               # Jumlah detik
    
            return '("%02d:%02d:%02d")' % (jam, menit, detik)    # Membuat format konversi sesuai dengan ("HH:MM:SS")

        if inputan_detik > 359999:    # Handle untuk nilai detik yang tidak bisa lebih dari 359999
            print ("Invalid Input")
        elif inputan_detik < 0:       # Handle untuk nilai detik yang tidak bisa bernilai negatif
            print ("Invalid Input")
        else:
            print (timeConverter(inputan_detik))   # Print hasil perhitungan konversi waktu

    except:    # Handle tipe data STRING dan FLOAT
        print ("Invalid Input")



    








