"""
	Student List
"""
from os import system
from pwinput import pwinput
from Student import Student

students:list=[]


def addstudent()->bool:
    
    system("cls")
    print("Add Student")
    print("-----------------------")
    ###
    idno:str = input("IDNO     :")
    lastname:str = input("LASTNAME :")
    firstname:str = input("FIRSTNAME:")
    course:str = input("COURSE   :")
    level:str = input("LEVEL    :")
    ###
    student:Student = Student(idno, lastname, firstname, course, level)
    # push dictionary to the list
    students.append(student)
    
    
def findstudent()->bool:
    system("cls")
    print("Find Student")
    print("-----------------------")
    check = False
    idnum:str = input("IDNO to FIND:")

    for x in students:
        if x.__eq__(idnum):
            print(x)
            check=True
            break
    if not check:
        print("Student NOT FOUND!")

def deletestudent()->bool:
    system("cls")
    print("Delete Student")
    print("-----------------------")
    check = False

    idnum:str = input("IDNO to DELETE:")
    
    for x in students:
        if x.__eq__(idnum):
            print(x)
            check = True
            break

    if not check:
        print("Student NOT FOUND!")
    else:
        while True:
            choice = input(f"Remove Student: {idnum} (y/n)? ")
            if choice.lower() =='y':
                print("--STUDENT DELETED--")
                students.remove(x)
                break
            elif choice.lower()=='n':
                print("---DELETION CANCELLED")
                break
            else: print("Input y or n only!")

def showallstudent()->None:
    global students
    system("cls")
    print("Student List")
    print("-----------------------")
    
    [print(x) for x in students]
    
def quit()->None:
    print("Program Terminated")

def showmenu()->None:
    system("cls")
    menulist:tuple=(
        "------ Main Menu ------",
        "1. Add Student",
        "2. Find Student",
        "3. Delete Student",
        "4. Display All",
        "0. Quit/End",
        "-----------------------",
    )
    [print(menuitem) for menuitem in menulist]

def getmenuoption(option:int)->None:
    options={
        1:addstudent,
        2:findstudent,
        3:deletestudent,
        4:showallstudent,
        0:quit
    }
    return options.get(option)()


def login()->bool:
    okey:bool =False
    system("cls")
    username:str = input("Username:")
    password:str = pwinput(prompt="Password:",mask="*")
    if username=="admin" and password=="user": # using short circuit notation
        okey=True
    return okey
   

def main()->None:
    okey:bool=login()
    option:int = 999
    if okey:
        while option!=0:
            showmenu()
            try:
                option=int(input("Enter option(0..4):"))
                getmenuoption(option)
            except:
                print("Invalid Input")
            finally:
                input("Press any to continue...")
    else:
        print("Invalid User...program ends")
    
if __name__=="__main__":
    main()