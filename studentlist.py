from os import system
from Student import Student
from pwinput import pwinput
from filehandler import *

uname:str = "admin"
pword:str = "user"

slist:list = loadlist()

def addstudent():
    global slist
    header("Add Student")
    idno:str = input("IDNO      :")
    lastname:str = input("LASTNAME  :")
    firstname:str = input("FIRSTNAME :")
    course:str = input("COURSE    :")
    level:str = input("LEVEL     :")
    #create student object and append
    s:Student = Student(idno,lastname,firstname,course,level)
    slist.append(s)
    print("New Student Added...")

def findstudent():
    global slist
    header("Find Student")

    idno:str = input("Enter Student IDNO: ")
    missing = True
    if len(slist)>0:
        for student in slist:
            if student.__eq__(idno):
                print(student)
                print("--STUDENT FOUND--")
                missing = False
    else: 
        print("List is EMPTY")
        missing = False
    if missing:
        print("--Student NOT FOUND--")

def deletestudent():
    header("Delete Student")

    idno:str = input("Enter Student IDNO: ")
    missing = True
    if len(slist)>0:
        for student in slist:
            if student.__eq__(idno):
                missing = False
                print(student)
                choice = input("Delete this student(y/n): ")
                if choice.lower() == 'y':
                    slist.remove(student)
                    print(f"--Student {idno} DELETED--")
                    break
                else: 
                    print("--Deletion Cancelled--")
                    break
    else:
        missing = False
        print("List is EMPTY!")
    if missing: print("Student NOT FOUND")

def displayallstudent():
    global slist
    header("Display All Student")
    if len(slist)==0:
        print("List is EMPTY")
    else:
        [print(student) for student in slist]
        

def quit():
    savelist(slist)
    print("---Program Terminated---")

def header(operator)->None:
    system("cls")
    print(operator)
    print("--------------------------")

def login()->bool:
    username:str = input("Enter Username :")
    password:str = pwinput(prompt="Enter Password :", mask="•")

    if username == uname and password == pword:
        return True
    else:
        return False
    
def displaymenu()->None:
    menu:tuple=(
        "------Main Menu------",
        "1. Add Student",
        "2. Find Student",
        "3. Delete Student",
        "4. Display All Student",
        "0. Quit/End",
        "---------------------",
    )
    [print(menuitem) for menuitem in menu]

def getmenuoption(option:int)->None:
    options:dict = {
        1:addstudent,
        2:findstudent,
        3:deletestudent,
        4:displayallstudent,
        0:quit,
    }
    return options.get(option)()

def main()->None:
    option:int = 999
    okey:bool = login()
    if okey:
        while option!=0:
            displaymenu()
            try:
                option=int(input("Enter option(0..4): "))
                getmenuoption(option)
            except:
                print("Invalid Input")
            finally:
                input("Press Enter to continue...")
    else: print("Incorrect USER... Program Terminated!")

if __name__ == "__main__":
    main()