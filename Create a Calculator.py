#####################################################################################
# 5.
# Buat return def function
# Kalkulator (+)(-)(/)(*)
# Inputan
# input angka 1:
# input angka 2:
# Masukkan operator :
# Output : Hasil penjumlahan dari 8 + 10 = 18


def jumlah (x,y):
    hasill = x + y
    return hasill

def kurang (x,y):
    hasil = x - y
    return hasil

def kali (x,y):
    hasil = x * y
    return hasil

def bagi (x,y):
    hasil = x / y
    return hasil

try:
    input_1 = float(input("Masukkan angka pertama: "))
    input_2 = float(input("Masukkan angka kedua: "))
    operator = str(input("Masukkan operator (+)(-)(/)(*): "))

    if operator == "+":
        A = jumlah(input_1,input_2)
        print (f'Hasil penjumlahan dari {input_1} + {input_2} = {A}')

    elif operator == "-":
        B = kurang(input_1,input_2)
        print (f'Hasil pengurangan dari {input_1} + {input_2} = {B}')

    elif operator == "*":
        C = kali(input_1,input_2)
        print (f'Hasil perkalian dari {input_1} + {input_2} = {C}')

    elif operator == "/":
        D = bagi(input_1,input_2)
        print (f'Hasil pembagian dari {input_1} + {input_2} = {D}')
    
    else:
        print ("Operator tidak tersedia")



except:
    print ("Tidak dapat menerima inputan ")

#####################################################################################
