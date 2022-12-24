class Rectangle:
    def __init__(self, height, width):  #the special __init__ method (called contructor in java c++ etc)
        self.height = height
        self.width = width

# the __init__ method is initialize when ever a class object is call
rect1 = Rectangle(20, 12)
rect2 = Rectangle(12, 9)
print(rect1.height*rect1.width)
print(rect2.height*rect2.width)
print(rect2.height)
