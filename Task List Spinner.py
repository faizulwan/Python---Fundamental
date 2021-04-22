###SOAL UJIAN 1###
'''
Buatlah sebuah return function dengan 1 argumen yang dapat memutar list angka (Putaran 1X counter-clockwise) seperti keterangan di bawah ini .

List Awal
[[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]


Function Initialization
 def counterClockwise(...):
     .....
     
# Use the Function
print(counterClockwise(List_awal))


List Output
[[3, 6, 9],
[2, 5, 8],
[1, 4, 7]]

'''



# Inisiasi data awal berupa list
list_A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

def counterClockwise (list_A):  # Fungsi untuk memutar balik setiap elemen data dengan berlawanan arah jarum jam 

    set1 = list_A[0][0]         # Membuat variabel baru untuk substitusi angka 1 dengan angka 7  
    list_A[0][0]=list_A[2][0]
    list_A[2][0]=set1 
    
    set2 = list_A[0][1]         # Membuat variabel baru untuk substitusi angka 2 dengan angka 4 
    list_A[0][1]=list_A[1][0]
    list_A[1][0]=set2
    
    set3 = list_A[0][2]         # Membuat variabel baru untuk substitusi angka 3 dengan angka 7
    list_A[0][2]=list_A[0][0]            
    list_A[0][0]=set3 
    
    set5 = list_A[1][2]         # Membuat variabel baru untuk substitusi angka 6 dengan angka 4
    list_A[1][2]=list_A[0][1]
    list_A[0][1]=set5
      
    set7 = list_A[2][1]         # Membuat variabel baru untuk substitusi angka 8 dengan angka 4
    list_A[2][1]=list_A[1][2]
    list_A[1][2]=set7   
    
    set8 = list_A[2][2]         # Membuat variabel baru untuk substitusi angka 9 dengan angka 7
    list_A[2][2]=list_A[0][2]
    list_A[0][2]=set8
    
    return list_A

print (list_A)
print ("=" * 50)
print(counterClockwise(list_A))
