import math
import numpy as np

key = input("Enter the Key:  ")
key = key.lower()
keylen = len(key)
dim  = math.ceil(math.sqrt(keylen))
# Initialization
arr = [[1234 for i in range(dim)] for j in range(dim)]
for i in range(0, keylen):
    arr[i//dim][i%dim] =  ord(key[i]) - 97

for i in range(keylen, dim*dim):
    arr[i//dim][i%dim] = (i-keylen)

pt = input("Enter the plain text :  ")
alter = str(pt)
ptlen = len(pt)
add = ptlen % dim
add = (dim - add, 0)[add == 0]
for i  in range (0, add):
    alter = alter + "x"

print()
print("*****************************************************")
print("The altered plain text :",alter)
print()
print("*****************************************************")

for row in arr: 
    print(row)

k = 0
answer = ""
while k<len(alter):
    data = [[ord(alter[i+j+k]) - 97 for i in range(1)] for j in range(dim)]
    data = np.dot(arr,data)
    for i in range(dim):
        answer = answer + str(chr((data[i][0]%26)+97))
    k+=dim
print()
print("*****************************************************")
print("Cipher Text : ",answer)
