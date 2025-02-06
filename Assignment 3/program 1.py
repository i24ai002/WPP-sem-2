def digit_root(n):
    while(n>9):
        num,sum,q=n,0,0
        list1=[]
        while num!=0:
            q=num%10
            sum+=q
            num//=10
        n=sum
    return n

num=int(input("Enter the number"))
print("The digit root of the number is :")
print(digit_root(num))
            