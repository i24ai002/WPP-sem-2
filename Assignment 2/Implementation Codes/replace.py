a=input("enter the string: ")
b=[input("enter the part of string you want to replace: "),input("enter the replaced part: ")]

if len(b[0])==len(b[1]):
    c=b[0]
    d=b[1]
    z=''
    for i in a:
        for j in range(len(c)):
            if i==b[j]:
                z=z+d[j]
            else:
                z=z+i
    print("replaced string is: ",z)
else:
    c=b[0]
    d=b[1]
    z=''
    for i in a:
        for j in range(len(c)):
            if i==b[j]:
                for k in range(len(d)):
                    z=z+d[k]
            else:
                z=z+i
    print("replaced string is: ",z)
    