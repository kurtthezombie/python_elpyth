from random import randint
from os import system

num:int = randint(1,20)

def inputnum():
    while True:
        try:
            n = int(input("Guess number: "))
            if n in range(1,20+1):
                break
        except:
            print("Invalid input!")
            continue
        print("Invalid input!")
    return n

def guess(n):
    if n<num:
        print("Higher!")
    elif n>num:
        print("Lower!")
    else:
        return 1

def main():
    count:int = 0
    system("cls")
    while True:
        gate = guess(inputnum())
        count += 1
        if gate == 1:
            break
        else:
            continue
    print("You got the correct answer!")
    print(f"Tries: {count}")
        
        
if __name__ == "__main__":
    main()