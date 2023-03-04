from os import system

def inputnum():
    system("cls")
    while True: 
        try:
            n = int(input("Input(1..10): ")) 
            if n in range(1,11): 
                break 
        except:
            print("Invalid input!") 
            continue 
        print("Invalid input!") 
    return n


def table(n):
    z = 0
    for x in range(z, n): 
        for y in range(z, n): 
            r = (x+y)%n
            print(r+1, end = " ")
        print()


def main():
    table(inputnum())


if __name__ == "__main__":
    main()