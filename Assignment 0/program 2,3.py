n = int(input("enter the number you want to calculate the factorial of: "))
fact = 1 

for i in range(1,n+1):
    fact*= i 
    
print(fact)    