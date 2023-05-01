import sys
sys.path.insert(0, '../db/')
from dbhelper import *

table:str ="users"

def userlogin(table:str,**kwargs)->str:
    message:str = "INVALID USER"
    user:dict = finduser(**kwargs)
    if user!= None: message = "LOGIN ACCEPTED"
    return message

def adduser(**kwargs)->bool:     return addrecord(table,**kwargs)
def finduser(**kwargs)->bool:       return getrecord(table,**kwargs)
def getalluser()->list:          return getall(table)
def updateuser(**kwargs)->bool:  return updaterecord(table,**kwargs)
def deleteuser(**kwargs)->bool:     return deleterecord(table,**kwargs)
def loginuser(**kwargs)->bool:      return loginrecord(table, **kwargs)   

def main():
    message = finduser(username='admin', password='user')
    print(message)

if __name__ == "__main__":
    main()