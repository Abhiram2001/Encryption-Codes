from os import system, name

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

def ENCRYPTION():
    print("********************ENCRYPTION*********************************")
    key1 = int(input("Enter the Key:  "))
    pt = input("Enter the plain text :  ").lower()
    i=0
    answer = ""
    while i < len(pt):
        temp = ord(pt[i]) - 97
        temp = temp + key1
        temp = temp % 26
        answer = answer + chr(temp+97)
        i+=1
    print(answer.upper())

def DECRYPTION():
    print("********************DECRYPTION*********************************")
    key = int(input("Enter the Key:  "))
    ct = input("Enter the cipher text :  ").lower()
    i=0
    answer = ""
    while i < len(ct):
        temp = ord(ct[i]) - 97
        temp = temp - key
        temp = temp % 26
        answer = answer + chr(temp+97)
        i+=1
    print(answer.upper())

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