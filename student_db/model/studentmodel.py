import sys
sys.path.insert(0,'student_db/db/')
from dbhelper import *

table:str ="student"

def addstudent(**kwargs)->bool:     return addrecord(table,**kwargs)
def findstudent(*args)->bool:       return getrecord(table,*args)
def getallstudent()->list:          return getall(table)
def updatestudent(**kwargs)->bool:  return updaterecord(table,**kwargs)
def deletestudent(*args)->bool:     return deleterecord(table,*args)

def main()->None:
    students:list = getrecord('student',[1])
    print(students)
    
if __name__=="__main__":
    main()
