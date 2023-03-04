from os import system

def add():
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
    print(num1+num2)

def subtract():
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
    print(num1-num2)

def multiply():
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
    print(num1*num2)

def divide():
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
    print(num1/num2)

def quit()->None:
    print("----Program Terminated----")

def displaymenu()->None:
    menu:list = [
        "---- Menu ----",
        "1. Addition",
        "2. Subtract",
        "3. Multiply",
        "4. Division",
        "0. Quit/End",
        "--------------"
    ]
    [print(x) for x in menu]

def getmenu(opt:int)->None:
    menuoption={
        1:add,
        2:subtract,
        3:multiply,
        4:divide,
        0:quit,
    }
    return menuoption.get(opt)()
    
def main()->None:
    option:int = None
    
    while True:
        system("cls")
        try:
            displaymenu()
            option:int = int(input("Select(0..4): "))
            if option is 0:
                quit()
                break
            elif option in range(0,5):
                getmenu(option)
        except:
            print("Invalid input!")
        finally:
            input("Press any key to continue...")
        print("Should not go beyond 1..4")



if __name__=="__main__":
    main()