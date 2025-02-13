def perfectsquare(p,q):
    count=0
    for i in range (p,q+1):
        if (i**0.5)%1==0:
            count+=1
    
    return count
            
            
test=int(input("Enter the number of test cases"))
for i in range (test):
    number=input("Enter the two numbers separated by spaces ")
        
    p,q=number.split()
    p=int(p)
    q=int(q)
    
    result=perfectsquare(p,q)
    print("the number of perfect squares in the range of given numbers is:",result) 