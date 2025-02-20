def maximisingxor(a,b):
    result1=0
    result2=0
    for i in range(a,b+1):
        for j in range(i,b+1):
            result1=i^j
            if result1>result2:
                result2=result1
    return result2
                
            
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
val=maximisingxor(a,b)
print(val)