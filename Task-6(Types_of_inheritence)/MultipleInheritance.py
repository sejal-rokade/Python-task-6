class student:
    def __init__(self,name):
        self.name=name
    def printstud(self):
        print(f'name={self.name}')

class teacher:
    def __init__(self,salary):
        self.salary=salary
    def printteacher(self):
        print(f'salary={self.salary}')

class director(student,teacher):
    def __init__(self,name,salary,allowence):
        self.allowence=allowence
        student.__init__(self,name)
        teacher.__init__(self,salary)
    def printdirector(self):
        print(f'allowence={self.allowence}')

d = director('abc',45700,342)

d.printdirector()
d.printteacher()
d.printstud()