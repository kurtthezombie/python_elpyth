from flask import Flask, render_template, request, redirect
from db.dbhelper import *
import sys
sys.path.insert(0, 'db/')
from os import system
from pwinput import pwinput
from model.studentmodel import *
from model.usermodel import *
from student import *

app=Flask(__name__)

header:list = ["id","idno","lastname","firstname","course","level","image","action"]
slist:list = []

upload_folder="static/imgs"
app.config["UPLOAD_FOLDER"]=upload_folder
imagename = ""

@app.route("/upload",methods=['POST','GET'])
def upload():
    global imagename
    if request.method=="POST":
        file = request.files['webcam']
        
        idno = request.args.get("idno")

        imagename = upload_folder+"/"+idno+".jpg"

        file.save(imagename)
        """okey: bool = addrecord('student',idno=idno,lastname=lastname,firstname=firstname,
                               course=course,level=level,image=imagename)"""
        return redirect("/");

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
    global imagename

    if flag == 1:
        updatestudent(id=id,idno=idno,lastname=lastname,firstname=firstname,
                        course=course,level=level, image=imagename)
    else:
        ok = addstudent(idno=idno, lastname=lastname,firstname=firstname,
                course=course,level=level, image = imagename)
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