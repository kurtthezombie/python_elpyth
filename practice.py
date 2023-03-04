from os import system


def table():
    while True: 
        try:
            n = int(input("Input(1..10):")) 
            if n in range(1,11): 
                break 
        except:
            print("Invalid input!") 
            continue 
        print("Invalid input!") 
        
    x:int = 0
    for i in range(x, n):
        for r in range(x,n):
            print((i+r+0)%n+1, end=" ")
        print()


def main():
    system("cls")
    table()
    
if __name__ == "__main__":
    main()