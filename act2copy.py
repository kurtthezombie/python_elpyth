"""
	Student List
"""
from os import system
from pwinput import pwinput

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
    student=dict({
        'idno':idno,
        'lastname':lastname,
        'firstname':firstname,
        'course':course,
        'level':level
    })
    # push dictionary to the list
    students.append(student)
    
    
def findstudent()->bool:
    system("cls")
    print("Find Student")
    print("-----------------------")
    
def deletestudent()->bool:
    system("cls")
    print("Delete Student")
    print("-----------------------")
    
def showallstudent()->None:
    global students
    system("cls")
    print("Student List")
    print("-----------------------")
    for st in students:
        student_values:list=st.values()
        [print(v,end=" ",flush=True) for v in student_values]
        print("")
    
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