#No.1 
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

i=1 
while (i<6):
      print((str(i) + ' ') *i)
      i+= 1
#=================================================================

#=================================================================
#No.2
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

i=1
n=6
while (i<n):
    j = 1
    while (j<=i):
        print (j, ' ', end='')
        j += 1
    print()
    i+=1
#=================================================================

#=================================================================
# No.3
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

i=6 
n=0
while (i>=n):
    j=5
    while (j>i):
        print (j, ' ', end ='')
        j -=1
    print()
    i-=1

#=================================================================

#=================================================================
# No.4
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

i=1
j=5 
while (i<6):
      print((str(i) + ' ') *j)
      i+=1
      j-=1
    
#=================================================================

#=================================================================
# No.5
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2 
# 1

i=1 
n=6
while (i<=n):
    j=1
    while (j<n):
        print (j, ' ', end ='')
        j +=1
    print()
    n-=1
#=================================================================

#=================================================================
# No.6
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4 
# 5

i=0
n=6
while (i<=n):
    j=5
    while (j>i):
        print (j, ' ', end ='')
        j -=1
    print()
    i+=1
#=================================================================

#=================================================================
# No.7 
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

for i in range (0,5,1):
    for j in range (0,5-i):
        print(' ' + ' ', end='')
    for k in range (0, 2*i + 1):
        print('*' + ' ', end='')
    print("  ")
for x in range (4,-1,-1):
    for y in range (0,5-x):
        print(' ' + ' ', end='')
    for z in range (0, 2*x + 1):
        print('*' + ' ', end='')
    print("  ")

Palindrome