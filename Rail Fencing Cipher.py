import sys
from os import system, name

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

def ENCRYPTION():
    print("********************ENCRYPTION*********************************")
    key = int(input("Enter the Key:  "))
    pt = input("Enter the plain text :  ").lower()
    ptlen = len(pt)
    answer = ""
    add  = ptlen % key 
    add = (key - add, 0)[add == 0]
    for i  in range (0, add):
        pt = pt + "x"
    for i in range (0 , key):
        for j in range (0 , key):
            if (i + (key*j)) < ptlen:
                answer  = answer + pt[(i + (key*j))]
    print("Cipher Text : ",answer.upper())


def DECRYPTION():
    print("********************DECRYPTION*********************************")
    key = int(input("Enter the Key:  "))
    ct = input("Enter the cipher text :  ").lower()
    ctlen = len(ct)
    answer = ""
    add  = ctlen % key 
    if add != 0 :
        sys.exit("Invalid Cipher Text")
    for i in range (0 , key):
        for j in range (0 , key):
            answer  = answer + ct[(i + (key*j))]
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