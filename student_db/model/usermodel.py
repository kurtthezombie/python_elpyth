import sys
sys.path.insert(0, 'student_db/db/')
from dbhelper import *

table:str ="users"

def adduser(**kwargs)->bool:     return addrecord(table,**kwargs)
def finduser(*args)->bool:       return getrecord(table,*args)
def getalluser()->list:          return getall(table)
def updateuser(**kwargs)->bool:  return updaterecord(table,**kwargs)
def deleteuser(*args)->bool:     return deleterecord(table,*args)
def loginuser(*args)->bool:      return login(*args)   
