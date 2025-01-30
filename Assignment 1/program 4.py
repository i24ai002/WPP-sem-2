list = [i for i in range(1, 10001)]

list0 = [i for i in range(1, 10001) if i % 5 == 0]
list1 = [i for i in range(1, 10001) if i % 5 == 1]
list2 = [i for i in range(1, 10001) if i % 5 == 2]
list3 = [i for i in range(1, 10001) if i % 5 == 3]
list4 = [i for i in range(1, 10001) if i % 5 == 4]

print(list0)
print(list1)
print(list2)
print(list3)
print(list4)

new_list = []
new_list.extend(list0)
new_list.extend(list1)
new_list.extend(list2)
new_list.extend(list3)
new_list.extend(list4)

if set(new_list) == set(list):
    print("True")
else:
    print("False")
