class Student:
    def __init__(self,sName,sLname):
        self.sName=sName
        self.sLname=sLname
    def printStudentName(self):
        print(f'sName={self.sName},sLname={self.sLname}')

class Teacher(Student):
    def __init__(self,sName,sLname,tName,tLname):
        super().__init__(sName,sLname)
        self.tName=tName
        self.tLname=tLname
    def printTeacherName(self):
        print(f'tName={self.tName},tLname={self.tLname}')

t = Teacher('s1','s2','t1','t2')


t.printTeacherName()
t.printStudentName()