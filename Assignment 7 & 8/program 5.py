class Shape:
    def area(self):
        pass 
    
    def perimeter(self):
        pass 

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2*(self.length + self.breadth)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14*self.radius*self.radius  
    
    def perimeter(self):
        return 2*3.14*self.radius 

l = int(input("enter length of rectangle: "))
b = int(input("enter breadth of rectangle: "))
rect = Rectangle(l,b)
print("area of rectangle:", rect.area())       
print("perimeter of rectangle:", rect.perimeter())  

r = int(input("enter radius of circle: "))
circle = Circle(r)
print("area of circle:", circle.area())      
print("perimeter of circle:", circle.perimeter())