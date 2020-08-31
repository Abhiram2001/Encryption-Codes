import sys
from collections import OrderedDict
from os import system, name

def removeDupWithOrder(str): 
    return "".join(OrderedDict.fromkeys(str))

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

def ENCRYPTION():
    print("********************ENCRYPTION*********************************")
    key = input("Enter the Key:  ").lower()
    keylen = len(key)

    if keylen != len(removeDupWithOrder(key)):
        print("Key Contains Same letters")
        sys.exit("Invalid Key")

    sKey = ''.join(sorted(key)) 
    pt = input("Enter the plain text :  ").lower()
    ptlen = len(pt)
    answer = ""
    
    add  = ptlen % keylen
    add = (keylen - add, 0)[add == 0]
    for i  in range (0, add):
        pt = pt + "x"
    ptlen = len(pt)

    for i in range(0, keylen):
        pos = key.index(sKey[i])
        for j in range(0, (len(pt)//keylen)):
            answer  = answer + pt[(pos + (keylen*j))]
    
    print("Cipher Text : ",answer.upper())


def DECRYPTION():
    print("********************DECRYPTION*********************************")
    key = input("Enter the Key:  ").lower()
    keylen = len(key)

    if keylen != len(removeDupWithOrder(key)):
        print("Key Contains Same letters")
        sys.exit("Invalid Key")
    sKey = ''.join(sorted(key)) 
    ct = input("Enter the cipher text :  ").lower()
    ctlen = len(ct)
    answer = ""
    add  = ctlen % keylen 
    if add != 0 :
        sys.exit("Invalid Cipher Text")
    
    rows  = ctlen//keylen
    arr = [["null" for i in range(keylen)] for j in range(rows)]

    sKey = ''.join(sorted(key)) 
    
    for i in range(0, keylen):
        pos = key.index(sKey[i])
        for j in range(0, rows):
            arr[j][pos] = ct[(i*rows)+j]

    for i in range(0, rows):
        pos = key.index(sKey[i])
        for j in range(0, keylen):
            answer  = answer + arr[i][j]
    
    print("Plain Text : ",answer.upper())
    

    

def main():
  ch=int(input("1.Encryption\n2.Decryption\nEnter the choice:"))
  if ch == 1:
      ENCRYPTION()
  elif ch == 2:
    DECRYPTION()
  else:
    clear()
    print("Wrong input Try Again")
    print()

    main()

if __name__ == "__main__": 
    main() 