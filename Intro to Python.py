# #Data Types in Python
# ##Primitive Data Types = Basic Data Type
# - String => Alfanumeric
# - Integer => Number
# - Float => Decimal Number
# - Complex Number => Rarely use in data science => Imaginary number
# - Boolean => True and false

# ##Python
# - Interpreter Programming Language => Program will excecute every single line from top to toe directly
# - Case Sensitive => 'A' is different with 'a'
# - Does not need a semicolon (;)
# - Tabulation - Indentation : is a sign of code block (Need a 'Tab')

# ###String
# - Need a ' ' like print ('Chelsea FC')
# print ('Biden\'s win')
# print ('Biden"s win')
# print ("Biden's win")
# print (''' Helo today is,
# Bidens win ''') #Use for showing multiple line

# ###Integer
# print (-8)
# print (9+9)
# print ('9' + '9')
# #To know your data type => type(data)
# print(type(9))
# print(type('9'))

# ###Float
# print(7.8)
# print(type(7.8))

###Boolean
# print(True)
# print(type(True))

# ### Variable
# - A 'name' use to storage data
# - Case Sensitive
# - Can not be initialized with number
# - No spacing
# - Can not use a reserved word (word that already have in python function)
# - No need to declare your variable data type
# - Will be overwrite by the last variable

####Operator Assignment (=)

# 1. Single Assignment
# x = data =>store 'data' in to 'x' variable
# a = input('Number: ');
# b = input ('Number: ');
# print (a + b)

# 2. Multiple Assignment
# a, b = 'John', 'Bandung'
# print (a+ ' ' +b)
# print (b)
# a = 25
# b = 75
# print (a)
# #We want to change a = 75 and b = 25
# a,b = b,a
# print (a)
# a = 45
# b = 45
# c = 45
# a = b = c = 45
# print(a)
# print(b)
# print(c)

#Access a String with Indexing
#Indexing in Python start with 0
#Indexing Access use []
  
# nama = 'Faiz Ulwan'
# print(nama[5])

# ##Slicing
# - We access to several element in one time
# Basic Syntax => variable[start : end : step]
# Step default = 1
#[Star : End]
#[Inclusive : Exclusive]
# Inclusive = Index is accessed (n)
# Exclusive = Index Will be accessed (n-1) 

# nama = 'Indonesia Raya is a national song anthem for Indonesia'
# print(nama[0:8])

# #If we want to access until mentioned index
# # Alternative 1
# print (nama[0:9])

# #Alternative 2
# print (nama[:4])
# print(nama[10:])
# print (nama[:])
# print(nama[-8])
# print(nama[0])

# #Calculate lengthness of String
# #with len function

# print(len(nama))
# print(nama[::-1]) #Flip the letters from back


# ## Function for convert data type into another type
# int(data) #convert to integer
# str(data) #convert tp string
# float(data) #convert to float
# ##Notes : data must fit
# x = '10'
# print(x + x)
