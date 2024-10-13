class student:
    def __init__(self,name):
        self.name=name
    def printStudent(self):
        print(f'name={self.name}')

class teacher(student):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary
    def printteacher(self):
        print(f'salary={self.salary}')

class director(teacher):
    def __init__(self,name,salary,allowence):
        super().__init__(name,salary)
        self.allowence=allowence
    def printdirector(self):
        print(f'allowence={self.allowence}')

d = director('xyz',54000,1234)

d.printStudent()
d.printteacher()
d.printdirector()

