#The class Triangle with different method of calculating area and perimeter
class Triangle():
    def __init__(self, first_side, second_side, third_side):
        self.side1 = first_side
        self.side2 = second_side
        self.side3 = third_side
        
    def perimeter(self):
        sum = self.side1 + self.side2 + self.side3   
        return sum
    
    def area(self):
        base = self.side1
        height = self.side2
        area = (base*height)*0.5
        return area
    
    
triangle1 = Triangle(2, 3, 5)
print(triangle1.perimeter())
