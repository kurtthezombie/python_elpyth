class Student():
    def __init__(self, idno:str, lastname:str, firstname:str, course:str, level:str)->None:
        self.idno = idno
        self.lastname = lastname
        self.firstname = firstname
        self.course = course
        self.level = level

    def __eq__(self, idno)->bool:
        return self.idno == idno
        
    def __str__(self)->str:
        return f"{self.idno} {self.lastname} {self.firstname} {self.course} {self.level}"
        