from flask import Flask, render_template, request, redirect

app=Flask(__name__)

header:list = ["idno","lastname","firstname","course","level","action"]
slist:list = [
    {
        "idno":"0001",
        "lastname":"durano",
        "firstname":"dennis",
        "course":"bscpe",
        "level":"4",
    },
    {
        "idno":"0002",
        "lastname":"alpha",
        "firstname":"bravo",
        "course":"bsit",
        "level":"2",
    },
    {
        "idno":"0003",
        "lastname":"charlie",
        "firstname":"echo",
        "course":"bscs",
        "level":"3",
    }
]


@app.route("/deletestudent",methods=["GET"])
def deletestudent():
    idno:str = request.args.get("idno")
    print("Deleting student with idno:", idno)
    for student in slist:
        if student["idno"] ==idno:
            slist.remove(student)
            break
    return redirect("/")

@app.route("/savestudent",methods=["POST"])
def savestudent():
    flag:int= request.form["flag"]
    idno:str = request.form["idno"]
    lastname:str = request.form["lastname"]
    firstname:str = request.form["firstname"]
    course:str = request.form["course"]
    level:str = request.form["level"]
    
    for student in slist:
        if student["idno"]==idno:
            student['lastname'] = lastname
            student['firstname'] = firstname
            student['course'] = course
            student['level'] = level
            break

    else:
        slist.append({
            "idno":idno,
            "lastname":lastname,
            "firstname":firstname,
            "course":course,
            "level":level,
        })
    return redirect("/")


@app.route("/")
def index():
    return render_template("index.html", title = 'Student List', 
                           list=slist, header_list=header)

if __name__=="__main__":
    app.run(debug=True)