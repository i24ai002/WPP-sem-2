students = []
print("enter the name of 10 students (maximum 15 characters each):")
for i in range(1,11):
    while True:
        name = input(f"enter the name of student {i}: ")
        if len(name)<=15:
            students.append(name)
            break
        else:
            print("name exceeds 15 characters")
            
print(students)

print("\nreversed name of students: ")
for name in students:
    print(name[::-1])