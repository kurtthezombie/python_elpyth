from os import system
from empfilehandler import loadlist, savelist

emplist:list = []
poslist:list = []
empposlist:list = []

#payroll list
payroll_list:list = loadlist()

def csvtolist():
    #append to emplist
    f = open("employee.csv", "r")
    for employee in f:
        employee = employee.strip()
        values = employee.split(',')
        emplist.append(values)
    #append to poslist
    g = open("position.csv", "r")
    for position in g:
        position = position.strip()
        values = position.split(',')
        poslist.append(values)

#merge both lists
def mergedata():
    for emp in emplist:
        for pos in poslist:
            if emp[3] == pos[0]:
                x:list = [emp[0], emp[1]+','+emp[2]]
                x.extend(pos[1:3])
                empposlist.append(x)

def findemp():
    header("Find Employee")
    found = False
    idno = input("IDNO: ")

    for item in empposlist:
        if item[0] == idno:
            for x in item:
                print(x, end=" ")
            found = True
    if not found:
        print("Employee Not Found")
    else:
        print()

def displayallemp():
    header("Display All Employee")
    global emplist
    global poslist
    
    #print list
    #print(emplist[item[1]])
    for x in empposlist:
        for y in x:
            print(y,end=" ")
        print()

def daysworked():
    global payroll_list
    header("Add Worked Day(s)")
    found = False
    idno = input("IDNO: ") 
    for item in empposlist:
        if item[0] == idno:
            for x in item:
                print(x, end=" ")
            found = True
            days = int(input("\nEnter Day(s) Worked: "))
            salary = days * float(item[3])
            fhalf:list = item[0:3]
            fhalf.extend([str(salary)])
            payroll_list.append(fhalf)

    if not found:
        print("Employee Not Found")
    else:
        print()
        print(f"Total Salary: {salary}")
    
def genpayroll():
    global payroll_list
    header("Generate Payroll")
    if len(payroll_list)==0:
        print("List is Empty")
    else:
        for x in payroll_list:
            for y in x:
                print(y,end=" ")
            print()

def delpayroll():
    header("Delete Payroll")
    
    found = False
    global payroll_list
    if len(payroll_list)==0: 
        print("List is Empty")
        found = True 
    else:
        idno = input("IDNO: ")
        for item in payroll_list:
            if item[0] == idno:
                found = True
                [print(itemval, end = " ") for itemval in item]
                print()
                choice = input("Delete this student(y/n): ")
                if choice.lower() =='y':
                    payroll_list.remove(item)
                    print(f"--Employee {idno} DELETED--")
                else: print("--Deletion Cancelled--")
                break
    if not found: print("Employee NOT FOUND")

def quit():
    system('cls')
    savelist(payroll_list)
    print("List saved..")
    print("---Program Terminated!---")

def header(operation):
    system('cls')
    if operation =="Menu":
        print("--------Main Menu--------")
    else:
        print(operation)
        print("-------------------------")

def getmenuoption(option:int):
    options:dict = {
        1:findemp,
        2:displayallemp,
        3:daysworked,
        4:genpayroll,
        5:delpayroll,
        0:quit
    }
    return options.get(option)()

def showmenu():
    system('cls')
    menu:tuple = (
        "1. Find Employee",
        "2. Display All Employee",
        "3. Add number of day(s) worked",
        "4. Generate payroll",
        "5. Delete payroll",
        "0. Quit/End",
    )
    header("Menu")
    [print(item) for item in menu]
    print("-------------------------")

def main()->None:
    csvtolist()
    mergedata()
    while True:
        showmenu()
        try:
            option = int(input("Enter option(0..4): "))
            getmenuoption(option)
            print("-------------------------")
            if option==0: 
                break
        except ValueError:
            if option==0:
                break
            print("Invalid Input!")
        finally:
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()