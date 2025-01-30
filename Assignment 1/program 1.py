# (a)
listA = []
for i in range(0,50):
    listA.append(i)
    i+=1 
    
print(listA)

# (b)
listB = []
for i in range(0,51):
    listB.append(i*i)
    i+=i

print(listB)   

# (c)
listC = []
for i in range(1,27):
    listC.append(chr(96+i)*i)
    i+=1 

print(listC)    
