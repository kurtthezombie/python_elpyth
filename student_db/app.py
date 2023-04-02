import sys
sys.path.insert(0, 'db/')
from os import system
from model.studentmodel import *
from model.usermodel import *
from student import *

table = 'student'
stlist:list = []

def addstudent(**kwargs)->bool:
    toplabel("Add Student")
    ##id = input("ID       : ")
    idno = input("IDNO     : " )
    lastname = input("Lastname : ")
    firstname = input("Firstname: ")
    course = input("Course   : ")
    level = input("Level    : ")
    ok = addrecord('student', idno=idno, lastname=lastname,
                   firstname=firstname,course=course,level=level) 
    return ok

def findstudent(*args)->bool:
    toplabel("Find Student")
    global table
    id = int(input("ID: "))
    ok = getrecord(table,[id])
    if ok:
        record = getrecord(table,[id]).values()
        [print(stud, end=" ") for stud in record]
        print()
    else:
        print("Student NOT FOUND")
    print("------------------------------")
    return ok

def deletestudent()->bool:
    toplabel("Delete Student")
    delid = int(input("ID: "))
    ok = getrecord('student',[delid])
    if ok:
        record = getrecord('student',[delid]).values()
        [print(stud, end=" ") for stud in record]
        print()
        ##yes or no to delete
        choice = input("Delete student record(y/n)? ").lower()
        if choice == 'y':
            deleted = deleterecord('student', [delid])
            print("Record DELETED.")
        else:
            print("Deletion CANCELLED...")
    else:
        print("Student NOT FOUND")
    print("------------------------------")
    return deleted

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
        "4. Display All Student",
        "0. Quit/End",
        "-----------------------------"
    )
    [print(menuitem) for menuitem in menu]

def getmenuoption(opt:int)->None:
    menuoption:dict={
        1:addstudent,
        2:findstudent,
        3:deletestudent,
        4:displayall,
        0:quit,
    }
    return menuoption.get(opt)()


def main()->None:
    opt:int = -1
    while opt!=0:
        displaymenu()
        try:
            opt=int(input("Enter Option (0..4):"))
            getmenuoption(opt)
        except:
            print("Invalid Input!")
        finally:
            input("Press any key to continue...")
    
    
if __name__=="__main__":
    main()