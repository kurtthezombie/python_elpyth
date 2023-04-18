import sys
sys.path.insert(0,'../db/')
from dbhelper import *

table:str ="student"

def addstudent(**kwargs)->bool:     return addrecord(table,**kwargs)
def findstudent(**kwargs)->bool:       return getrecord(table,**kwargs)
def getallstudent()->list:          return getall(table)
def updatestudent(**kwargs)->bool:  return updaterecord(table,**kwargs)
def deletestudent(**kwargs)->bool:     return deleterecord(table,**kwargs)

def main()->None:
    students:list = findstudent(idno = '0002')
    print(students)
    
if __name__=="__main__":
    main()
