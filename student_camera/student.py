class Person(object):
    def __init__(self,lastname:str,firstname:str):
        self.lastname = lastname
        self.firstname = firstname
    
    def __str__(self)->str:
        return f"{self.lastname} {self.firstname}"
        
########################################

class Student(Person):
    def __init__(self,id:str,idno:str,lastname:str,firstname:str,course:str,level:str,image:str):
        super().__init__(lastname,firstname)
        self.id=id
        self.idno=idno
        self.course=course
        self.level=level
        self.image=image
        
    def __str__(self)->str:
        return f"{self.id} {self.idno} { super().__str__()} {self.course} {self.level} {self.image}"
        

        