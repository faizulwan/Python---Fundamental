##### LIST COMPREHENSION 

# list_baru = [expression]

# angka = [1,2,3,4,5]

# pangkat = []
# for i in angka:
#     pangkat.append(i**2)

# print (pangkat)

# pangkat2 = list(map(lambda x: x **2 , angka)) 

# print (pangkat2)


# pangkat3 = [ i ** 2 for i in angka ]  ##LIST COMPREHENSION

# print (pangkat3)

# irisan = []

# a = [1,2,3,4,5]
# b = [2,4,8,9,56]

# for i in a:
#     for j in b:
#         if i == j:
#             irisan.append(i)

# print (irisan)

# irisan2 = [i for i in a for j in b if i == j]
# print (irisan2)

##########################################################################################################
##Latihan

buah = ["mangga", "apel", "jeruk", "anggur", "semangka", "pisang"]
isi = ["coklat", "susu", "keju", "anggur", "pisang"]


#gunakan list COMPREHENSION untuk membuat kombinasi buah dan isi, Tidak ada buah dan isi yang semangka

pair = []

for i in buah:
    for j in isi:
        if i != j:
            print (i,j)

# kombinasi = [i for i in buah for j in isi if i != j]


pair =[(i,j) for i in buah for j in isi if x!=y
print (pair)

##########################################################################################################

A = [1,2,3,4,5,6]
B = ["a", "b", "c", "d"]

# Basic Syntax:
# zip(data_iteravle 1, data iteralb;e 2)
# ## Menghasilkan tipe data object sehingga perlu dikonversi

zip_A = list(zip(A,B))
zip_B = tuple(zip(A,B))
zip_C = dict(zip(A,B))

print (zip_A)
print (zip_B)
print (zip_C)