import random

list=[0,1]
values=[]
for i in range(100):
    values.append(random.choice(list))

count,maxcount=0,0
for el in values:
    if not el:
        count+=1
    else:
        if maxcount<count:
            maxcount=count
        count=0
print(values)
print("\nthe longest run of zeroes is",maxcount)