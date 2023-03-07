from os import system

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
    print("findstudent")

def deletestudent():
    print("delete student")

def showallstudent():
    global students
    system("cls")
    print("Student List")
    print("------------------")

    for x in students:
        studentval:list = x.values()
        [print(y, end = " ", flush = True) for y in studentval]
        print("")

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


def main()->None:
    while True:
        displaymenu()
        try:
            option = int(input("Enter option(0..4): "))
            if option is 0:
                quit()
                break
            elif not option in range (0,5):
                print("Invalid input!")
            else:
                getoption(option)
        except:
            print("Invalid input!")
        finally:
            input("Press any key to continue...")

if __name__ == "__main__":
    main()