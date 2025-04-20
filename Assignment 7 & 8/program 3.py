class Bank:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
        
    def credit(self, amount):
        self.balance += amount
        print("₹",amount,"credited")
        
    def debit(self, amount):
        self.balance -= amount
        print("₹",amount,"debited")
        
    def get_balance(self):
        return self.balance
        
acc1 = Bank(10000,"abcdef")
print(acc1.balance)
print(acc1.account_no)
acc1.credit(600)
acc1.debit(500)
print(acc1.get_balance())