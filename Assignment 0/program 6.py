num = int(input("enter the number you want to reverse: "))
temp = 0 
result = 0 

while num!=0:
    temp = num%10
    result = result*10 +temp
    num//=10

print("the reverse number is",result)    
    