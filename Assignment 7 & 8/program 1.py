class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
    
    def delete(self, key):
        temp, prev = self.head, None
        while temp and temp.data != key:
            prev, temp = temp, temp.next
        if temp:
            prev.next = temp.next if prev else self.head.next
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None")


ll = LinkedList()
for num in [10, 20, 30]:
    ll.insert(num)
ll.display()
ll.delete(20)
ll.display()