from flask import Flask, render_template, request, redirect
import sys
sys.path.insert(0, 'db/')
from os import system
from pwinput import pwinput
from model.studentmodel import *
from model.usermodel import *
from student import *

app=Flask(__name__)

header:list = ["id","idno","lastname","firstname","course","level","action"]
slist:list = []

@app.route("/deletestudent",methods=["GET"])
def delstudent():
    idno:str = request.args.get("idno")
    print("Deleting student with idno:", idno)
    deletestudent(idno=idno)
    """for student in slist:
        if student["idno"] ==idno:
            deletestudent(idno=idno)
            break"""
    return redirect("/")

@app.route("/savestudent",methods=["POST"])
def savestudent():
    flag:int= int(request.form["flag"])
    idno:str = request.form["idno"]
    lastname:str = request.form["lastname"]
    firstname:str = request.form["firstname"]
    course:str = request.form["course"]
    level:str = request.form["level"]
    
    if flag == 1:
        updatestudent(id=id,idno=idno,lastname=lastname,firstname=firstname,
                        course=course,level=level)
    else:
        ok = addstudent(idno=idno, lastname=lastname,firstname=firstname,
                course=course,level=level)
    return redirect("/")

def displayall()->list:
    students:list = getallstudent()
    student_list = []
    for s in students:
        student_dict = s.copy()
        student_list.append(student_dict)
        """values:list = list(s.values())
        slist.append(Student(values[0],values[1],values[2],values[3],values[4],values[5]))"""
    return student_list
    ##slist.clear()

@app.route("/")
def index():
    slist = displayall()
    return render_template("index.html", title = 'Student List', 
                           list=slist, header_list=header)

if __name__=="__main__":
    app.run(debug=True)