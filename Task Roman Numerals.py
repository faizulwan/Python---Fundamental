#####################################################################################
# 8.
# Konversi Romawi
# buat return function
# Gunakan dict
# batasan maksimal <= 4000
# keluar notif angka diluar jangkauan

# Silahkan masukkan angka : 2018
# Ouputnya : MMXVIII

# Silahkan masukkan angka : MMXVIII
# Ouputnya : 2018

RomNum = {"M" : 1000, "CM" : 900, "D": 500, "CD": 400, "C" : 100, "XC" : 90,
 "L": 50, "XL":40,"X": 10, "IX": 9, "V": 5, "IV":4, "I": 1}




print ("==> NUMBER-ROMAN CONVERSION <==")
print (''' What is your goal : 
1. Number to Roman
2. Roman to Number''')


Romawi = list (RomNum)
Numeral = list (RomNum.values())
bla = []

def angkakeromawi(a):
    while a > 0:
        for i in range (0,len(RomNum)):
            if a >= Numeral[i]:
                bla.append(Romawi[i] * (int(a / Numeral[i])))
                a %= Numeral[i]
                i+= 1
    return "".join(bla)



def romawikeangka(word):
    output = ''
    word = word.upper()
    word = word.split()
    word = ''.join(word)
    for i in word:
        if i in Romawi:
            Numeral_1 = Numeral[Romawi.index(i)]
            output = output + Numeral_1 + ' / '
        
    return output




try:
    
    masukkan = int(input("Choose your goal (1/2) : "))

    if masukkan == 1:
        print ("Number to Roman Conversion")
        number = int(input("Input your number : "))

        if number > 4000:
            print ("Can not process number greater than 4000")

        elif number <= 0:
            print ("Can not process zero and negative number")

        else:
            print (angkakeromawi(number))


    elif masukkan == 2:
        print ("Roman to Number Conversion")

    else:
        print ("Application can not be found")

except:
    print ("Invalid input")

