class employee:
    def __init__(self,eName):
        self.eName=eName
    def printemployee(self):
        print(f'eName={self.eName}')

class empInformation(employee):
    def __init__(self,empName,empNo):
        super().__init__(empNo)
        self.empNo=empNo
    def printempInformation(self):
        print(f'empaNo={self.empNo}')

class empSalary(employee):
    def __init__(self,empName,salary):
        super().__init__(empName)
        self.salary=salary
    def printempSalary(self):
        print(f'salary={self.salary}')

e=employee('mno')
ei=empInformation('mno',20)
es=empSalary('mno',45000)

e.printemployee()
ei.printempInformation()
es.printempSalary()
    
    