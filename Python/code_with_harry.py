import random

computer = random.choice([0,1,-1])

youstr = input("enter your choice: ")
youDict = {"r":-1,"p":1,"s":0}


if youstr not in youDict:
    print("Invalid choice! Please enter 'r', 'p', or 's'.")
else:
    you = youDict[youstr]
    
print("computer =",computer)
print("you =",you)    

if computer == you:
    print("It's a draw")
elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
    print("You win!")
else:
    print("You lose!")