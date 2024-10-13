class student:
    def __init__(self,name):
        self.name=name
    def printstudent(self):
        print(f'name={self.name}')

class Test(student):
    def __init__(self,name,tMarks):
        super().__init__(name)
        self.tMarks=tMarks
    def printTest(self):
        print(f'tMarks={self.tMarks}')

class sports:
    def __init__(self,sMarks):
        self.sMarks=sMarks
    def printsports(self):
        print(f'sMarks={self.sMarks}')

class result(Test,sports):
    def __init__(self,name,tMarks,sMarks,total):
        Test.__init__(self,name,tMarks)
        sports.__init__(self,sMarks)
        self.total=self.tMarks+self.sMarks
        print(f'total={self.total}')
    def printresult(self):
        
        self.printstudent()
        self.printTest()
        self.printsports()
       
r = result('pqr',50,45)

r.printstudent()
r.printresult()
r.printsports()
r.printTest()
