from Student import Student
filename:str = "student.csv"

def savelist(slist:list)->None:
    f = open(filename,"w")
    for student in slist:
        f.write(student.__str__().rstrip() + "\n")
        f.write("\n")
    f.close()

def loadlist()->list:
    f = open(filename,"r")
    mlist:list = []
    for item in f:
        if item.strip() =="":
            pass
        else:
            myitem:list=item.split(",")
            mlist.append(Student(myitem[0],myitem[1],myitem[2],myitem[3],myitem[4]))
    return mlist