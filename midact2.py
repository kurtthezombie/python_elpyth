from os import system
from pwinput import pwinput

students:list = []

def addstudent():
    system("cls")
    print("Add Student")
    print("------------------")

    idno:str = input("IDNO     :")
    lastn:str = input("LASTNAME :")
    firstn:str = input("FIRSTNAME:")
    course:str = input("COURSE   :")
    level:str = input("LEVEL    :")

    student = dict({
        'idno':idno,
        'lastname':lastn,
        'firstname':firstn,
        'course':course,
        'level':level
    })
    students.append(student)

def findstudent():
    system('cls')
    print("Find Student")
    print("------------------")
    idnum:str = input("IDNO     :")
    check = False
    for x in students:
        if x.get('idno') == idnum:    
            print(f"LASTNAME :{x.get('lastname')}")
            print(f"FIRSTNAME:{x.get('firstname')}")
            print(f"COURSE   :{x.get('course')}")
            print(f"LEVEL    :{x.get('level')}")
            check = True
    if not check:
        print("STUDENT NOT FOUND!")

def deletestudent():
    system("cls")
    print("Delete Student")
    print("------------------")

    global students
    idnum:str = input("IDNO     :")
    check = False

    for x in students:
        if x.get('idno') == idnum:    
            print(f"LASTNAME :{x.get('lastname')}")
            print(f"FIRSTNAME:{x.get('firstname')}")
            print(f"COURSE   :{x.get('course')}")
            print(f"LEVEL    :{x.get('level')}")
            check = True
            break
    if not check:
        print("STUDENT NOT FOUND!")
    else:
        while True:
            choice = input(f"Do you really want to remove Student: {idnum} (y/n)? ")
            if choice.lower() == "y":
                print("---STUDENT DELETED---")
                students.remove(x)
                break
            elif choice.lower() == "n":
                print("---DELETION CANCELLED---")
                break
            else:
                print("Input y or n only!")
           
def showallstudent():
    global students
    system("cls")
    print("Student List")
    print("------------------")
    for x in students:
        studentval:list = x.values()
        [print(y, end = " ", flush = True) for y in studentval]
        print("")
    print("------------------")

def quit():
    print("--Program Terminated--")

def displaymenu():
    system("cls")
    menulist = (
        "----- Main Menu -----",
        "1. Add Student",
        "2. Find Student",
        "3. Delete Student",
        "4. Display All",
        "0. Quit/End",
        "---------------------",
    )
    [print(menuitem) for menuitem in menulist]

def getoption(option:int):
    options = {
        1:addstudent,
        2:findstudent,
        3:deletestudent,
        4:showallstudent,
        0:quit
    }
    return options.get(option)()

def login():
    gate = False
    system("cls")
    user:str = input("Username: ")
    passw:str = pwinput(prompt="Password: ", mask ="•")
    if user == "admin" and passw == "user":
        print(f"Welcome back, {user}.")
        gate = True
        
    return gate

def main()->None:
    gate:bool = login()
    if gate:
        while True:
            displaymenu()
            try:
                option = int(input("Enter option(0..4): "))
                if option is 0:
                    quit()
                    break
                elif option not in range (0,5):
                    print("(0..5) only!")
                else:
                    getoption(option)
            except:
                print("Invalid Input!")
            finally:
                input("Press any key to continue...")
    else:
        print("Invalid User!")
        quit()

if __name__ == "__main__":
    main()