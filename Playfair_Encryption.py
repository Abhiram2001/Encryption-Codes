import sys
import numpy as np
from collections import OrderedDict
from string import ascii_lowercase
from os import system, name

def removeDupWithOrder(str): 
    return "".join(OrderedDict.fromkeys(str))

def missing_letters(string):
    alphabet = set(ascii_lowercase)
    return ''.join(sorted(set(alphabet) - set(string)))


def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

def encryption():
    key = input("Enter the Key:  ")
    key = key.replace("j", "i")
    key = removeDupWithOrder(key)
    keylen = len(key)
    rem_letters = missing_letters(key+"j")
    arr = [["temp" for i in range(5)] for j in range(5)]

    for i in range(0, keylen):
        arr[i//5][i%5] = key[i]

    for i in range(keylen, 25):
        arr[i//5][i%5] = rem_letters[i-keylen]

    narr = np.array(arr)
    pt = input("Enter the plain text :  ")
    alter = str(pt)
    i = 0
    end = len(alter)
    while i < end:
        if i == (len(alter)-1):
            alter = alter + "x"
            i+=2
        else: 
            if(alter[i] != alter[i+1]):
                i+=2
            elif((alter[i] == alter[i+1])):
                alter = alter[:i+1] + "x" + alter[i+1:]
                i+=2
        end = len(alter)

    print()
    print("*****************************************************")
    print("The altered plain text :",alter)
    print()
    print("*****************************************************")

    for row in arr: 
        print(row)
    i = 0
    answer= ""

    while i< len(alter):

        if ((alter[i] == "i" and alter[i+1] == "j") or (alter[i] == "j" and alter[i+1] == "i")):
            tr = np.argwhere (narr == "i")[0][0]
            tc = np.argwhere (narr == "i")[0][1]
            if(alter[i] == "i"):
                answer = answer + arr[tr-1][tc]
                answer = answer + arr[tr+1][tc]
            elif(alter[i] == "j"):
                answer = answer + arr[tr+1][tc]
                answer= answer + arr[tr-1][tc]

        else:

            if(alter[i]=="j"):
                alter = alter[:i] +"i"+ alter[i+1:]
            if(alter[i+1]=="j"):
                alter = alter[:i+1] +"i"+ alter[i+2:]

            fr = np.argwhere (narr == alter[i])[0][0]
            fc = np.argwhere (narr == alter[i])[0][1]

            sr = np.argwhere (narr == alter[i+1])[0][0]
            sc = np.argwhere (narr == alter[i+1])[0][1]

            if(fr == sr):
                answer = answer + arr[fr][(fc+1)%5]
                answer = answer + arr[sr][(sc+1)%5]
            elif(fc == sc):
                answer = answer + arr[(fr+1)%5][fc]
                answer = answer + arr[(sr+1)%5][fc]
            else:
                answer = answer + arr[fr][sc]
                answer = answer + arr[sr][fc]
        
        i+=2
    print()
    print("*****************************************************")
    print("Cipher Text : ",answer)


def decryption():
    key = input("Enter the Key:  ")
    key = key.replace("j", "i")
    key = removeDupWithOrder(key)
    keylen = len(key)
    rem_letters = missing_letters(key+"j")
    arr = [["temp" for i in range(5)] for j in range(5)]

    for i in range(0, keylen):
        arr[i//5][i%5] = key[i]

    for i in range(keylen, 25):
        arr[i//5][i%5] = rem_letters[i-keylen]

    narr = np.array(arr)
    ct = input("Enter the Cipher text :  ")
    alter = str(ct)
    i = 0
    end = len(alter)
    
    if (end %2) !=0:
        sys.exit("Invalid Cipher Text")
    
    print("*****************************************************")
    for row in arr: 
        print(row)
    i = 0
    answer= ""
    tr = np.argwhere (narr == "i")[0][0]
    tc = np.argwhere (narr == "i")[0][1]


    while i< len(alter):

        if ((ct[i] == arr[(tr-1)%5][tc] and ct[i+1] == arr[(tr+1)%5][tc]) or (ct[i+1] == arr[(tr-1)%5][tc] and ct[i] == arr[(tr+1)%5][tc])):
            if(alter[i] == arr[(tr-1)%5][tc]):
                answer = answer +"ij"
            elif(alter[i] == arr[(tr+1)%5][tc]):
                answer = answer + "ji"

        else:

            print(end="")
            fr = np.argwhere (narr == alter[i])[0][0]
            fc = np.argwhere (narr == alter[i])[0][1]

            sr = np.argwhere (narr == alter[i+1])[0][0]
            sc = np.argwhere (narr == alter[i+1])[0][1]

            if(fr == sr):
                answer = answer + arr[fr][(fc-1)%5]
                answer = answer + arr[sr][(sc-1)%5]
            elif(fc == sc):
                answer = answer + arr[(fr-1)%5][fc]
                answer = answer + arr[(sr-1)%5][fc]
            else:
                answer = answer + arr[fr][sc]
                answer = answer + arr[sr][fc]
        
        i+=2
    print()
    print("*****************************************************")
    print("Cipher Text : ",answer)

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
