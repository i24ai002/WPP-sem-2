'''
class Bank:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
        
    def deposit(self, amount):
        self.balance += amount
        print("₹",amount,"deposited")
        
    def withdraw(self, amount):
        self.balance -= amount
        print("₹",amount,"withdrawn")
        
    def details(self):
        print("account_no:",self.account_no)
        print("balance:",self.balance)
        
a = int(input("enter the amount you have in bank: "))  
b = int(input("enter your account_no: "))
acc1 = Bank(a,b)
print(acc1.balance)
print(acc1.account_no)
x = int(input("enter amount you want to deposit: "))
acc1.deposit(x)
y = int(input("enter amount you want to withdraw: "))
acc1.withdraw(y)
acc1.details()
'''

class A:
    def __init__(self):
        pass

    def display(self):
        print("method of A")

class B(A):
    def __init__(self):
        pass
    
    def access_A(self):
        super().__init__() 

class C(B):
    def __init__(self):
        pass
    
    def show_A(self):
        super().__init__() 

        
obj = C()
obj.display()