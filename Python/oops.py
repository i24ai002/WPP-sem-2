'''
class programmer:
    company = "microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    
p = programmer("neel",1200000,395009)
print(p.name,p.company,p.salary,p.pin)  
'''  

'''
class calculator:
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(f"{self.n*self.n}")
            
    def cube(self):
        print(f"{self.n*self.n*self.n}")
        
    def root(self):
        print(f"{self.n**0.5}")    
    
    @staticmethod
    def hello():
        print("hello world")       
           
a = calculator(4)
a.hello()
a.square()
a.cube()
a.root()    
'''

'''
from random import randint

class train:
    
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def book(self, fro, to):
        print(f"ticket is booked in train no: {self.trainNo} from {fro} to {to}")
        
    def status(self):
        print(f"train no: {self.trainNo} is running on time")
        
    def fare(self, fro, to):
        print(f"ticket fare for train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")
        
    
t = train(19034)
t.book("surat","nadiad")
t.status()
t.fare("surat","nadiad")    
'''    


                