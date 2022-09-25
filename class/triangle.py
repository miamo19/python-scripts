class Triangle():
    def __init__(self, a, b, c):
        self.side1 = a
        self.side2 = b
        self.side3 = c
    def add(self):
        sum = self.side1 + self.side2 + self.side3    #calculate the perimeter of the triangle
        return sum
triangle1 = Triangle(2, 3, 5)
print(triangle1.add())