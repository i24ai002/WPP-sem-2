#class
class Student:  
    college_name = "SVNIT"
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("welcome",self.name)
        
    def get_marks(self):
        return self.marks

#object(instance)
s1= Student("neel",83)
s1.welcome()
print(s1.get_marks())




class Student:
    
    def __init__(self,name,phy,chem,math):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.math = math
        
    def avg(self):
        average = (self.phy + self.chem + self.math)/3
        return average
        
s1 = Student("neel",84,94,95)
print("name:", s1.name)        
print("physics:", s1.phy)
print("chemistry:", s1.chem)
print("maths:", s1.math)
print("average:", s1.avg())


class Account:
    
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no
        
    def debit(self,amount):
        self.balance -= amount 
        print("Rs.", amount,"was debited")
        
    def credit(self,amount):
        self.balance += amount 
        print("Rs.", amount,"was credted")
        
    def get_balance(self):
        return self.balance
    
acc1 = Account(10000 , "abcef")
print("balance:",acc1.balance)
print("account_no:", acc1.acc_no)
acc1.debit(500)
acc1.credit(600)
print("remaining balance:",acc1.get_balance())


#inheritance example
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

engg1 = Engineer("Elon Musk", 40)
engg1.showDetails()


#polymorphism example
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4,5)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()


#polymorphism example
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    def __gt__(self, order2):
        return self.price > order2.price
    
order1 = Order("chips",100)
order2 = Order("coffee",200)

print(order1 > order2)
print(order2 > order1)