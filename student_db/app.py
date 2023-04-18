import sys
sys.path.insert(0, 'db/')
from os import system
from pwinput import pwinput
from model.studentmodel import *
from model.usermodel import *
from student import *

table = 'student'
stlist:list = []

def addstud(**kwargs)->bool:
    toplabel("Add Student")
    ##id = input("ID       : ")
    idno = input("IDNO     : " )
    lastname = input("Lastname : ")
    firstname = input("Firstname: ")
    course = input("Course   : ")
    level = input("Level    : ")
    ok = addstudent(idno=idno, lastname=lastname,firstname=firstname,
                course=course,level=level)
    print("Student ADDED...")
    return ok

def findstud()->bool:
    toplabel("Find Student")
    ##global table
    idno = input("IDNO: ")
    ok = findstudent(idno=idno)
    if ok:
        record = ok.values()
        [print(stud, end=" ") for stud in record]
        print()
    else:
        print("Student NOT FOUND")
    print("------------------------------")
    return ok

def delstudent()->bool:
    toplabel("Delete Student")
    idno = input("IDNO: ")
    ok = findstudent(idno=idno)
    if ok:
        record = ok.values()
        [print(stud, end=" ") for stud in record]
        print()
        ##yes or no to delete
        print("\n")
        choice = input("Delete student record(y/n)? ").lower()
        if choice == 'y':
            deleted = deletestudent(idno=idno)
            print("Record DELETED.")
        else:
            print("Deletion CANCELLED...")
            deleted = False
    else:
        print("Student NOT FOUND")
        return ok
    print("------------------------------")
    return deleted
    
def updatestud()->bool:
    toplabel("Update Student")
    ##global table
    idno = input("IDNO: ")
    ok = findstudent(idno=idno)
    if ok:
        record = ok.values()
        [print(stud, end=" ") for stud in record]
        print()
        
        lastname = input("Lastname : ")
        firstname = input("Firstname: ")
        course = input("Course   : ")
        level = input("Level    : ")
        updated = updatestudent(id=id,idno=idno,lastname=lastname,firstname=firstname,
                        course=course,level=level)
        print("Student Record UPDATED...")
    else:
        print("Student NOT FOUND")
        return ok
    print("------------------------------")
    return updated

def displayall()->None:
    toplabel("Display All Student")
    students:list = getallstudent()
    for s in students:
        values:list = list(s.values())
        stlist.append(Student(values[0],values[1],values[2],values[3],values[4],values[5]))
    [print(stud) for stud in stlist]
    stlist.clear()
    
    
def quit()->None:
    print("Program terminated...")

def toplabel(label:str)->None:
    system("cls")
    print("---------"+label+"---------")

def displaymenu()->None:
    system("cls")
    menu:tuple=(
        "--------- Main Menu ---------",
        "1. Add Student",
        "2. Find Student",
        "3. Delete Student",
        "4. Update Student",
        "5. Display All",
        "0. Quit/End",
        "-----------------------------"
    )
    [print(menuitem) for menuitem in menu]

def getmenuoption(opt:int)->None:
    menuoption:dict={
        1:addstud,
        2:findstud,
        3:delstudent,
        4:updatestud,
        5:displayall,
        0:quit,
    }
    return menuoption.get(opt)()

def login()->bool:
    system("cls")
    username = input("USERNAME   :")
    password = pwinput(prompt="PASSWORD   :", mask="•")
    message = loginuser(username = username, password = password)
    if message == "LOGIN ACCEPTED":
        return True
    else: return False
    
def main()->None:
    logincheck = login()
    if logincheck:
        opt:int = -1
        while opt!=0:
            displaymenu()
            try:
                opt=int(input("Enter Option (0..5):"))
                getmenuoption(opt)
            except:
                print("Invalid Input!")
            finally:
                input("Press Enter to continue...")
    else:
        print("INVALID USER")
        quit()

if __name__=="__main__":
    main()