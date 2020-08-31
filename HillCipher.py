import math
import numpy as np
from sympy import Matrix
from os import system, name

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

key=""
keylen=0
dim = 0
arr = []

def keyInput():
    global key , keylen , dim ,arr
    key = input("Enter the Key:  ")
    key = key.lower()
    keylen = len(key)
    dim  = math.ceil(math.sqrt(keylen))
    arr = [[1234 for i in range(dim)] for j in range(dim)]

    for i in range(0, keylen):
        arr[i//dim][i%dim] =  ord(key[i]) - 97

    for i in range(keylen, dim*dim):
        arr[i//dim][i%dim] = (i-keylen)

    if np.linalg.det(np.array(arr)) == 0:
        print("We Cannot decrypt with this key so Choose another")
        print("*****************************************************")
        keyInput()



def encryption():
    global key , keylen , dim ,arr
    print("********************ENCRYPTION*********************************")
    keyInput()
    print("*****************************************************")
    pt = input("Enter the plain text :  ").lower()
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
    print("Cipher Text : ",answer.upper())




def decryption():
    global key , keylen , dim ,arr
    print("********************DECRYPTION*********************************")
    keyInput()
    print("*****************************************************")
    ct = input("Enter the Cipher text :  ").lower()
    print()
    print("*****************************************************")

    inverseKeyMatrix = Matrix(arr).inv_mod(26)
    np.inverseKeyMatrix = np.array(inverseKeyMatrix)
    arr = np.array(inverseKeyMatrix)
    for row in arr: 
        print(row)    

    k = 0
    answer = ""
    while k<len(ct):
        data = [[ord(ct[i+j+k]) - 97 for i in range(1)] for j in range(dim)]
        data = np.dot(inverseKeyMatrix,data)
        for i in range(dim):
            answer = answer + str(chr(int(round(data[i][0]))%26 + 97))
        k+=dim
    print()
    print("*****************************************************")
    print("Plain Text : ",answer.upper())



def main():
  ch=int(input("1.Encryption\n2.Decryption\nEnter the choice:"))
  if ch == 1:
      encryption()
  elif ch == 2:
    decryption()
  else:
    clear()
    print("Wrong input Try Again")
    print()
    main()

if __name__ == "__main__": 
    main() 
