class Rectangle:
    def __init__(self, height, width):  #the special __init__ method (called Constructor in Java C++ etc)
        self.height = height
        self.width = width
        
    def rect_area(self):
        print(self.height*self.width)
    
# Instanciation (object of the Class Rectangle are created)
rect1 = Rectangle(20, 12)
rect2 = Rectangle(12, 9)

print(rect1.height*rect1.width)
print(rect2.rect_area)

print(rect2.height)
print(rect2.width)
