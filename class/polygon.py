#The base class
class Polygon:
    def __init__(self, no_of_sides):
        self.num_side = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.num_side)]

    def dispSides(self):
        for i in range(self.num_side):
            print("Side", i + 1, "is", self.sides[i])

# The inherited class
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


t = Triangle()

t.inputSides()
t.dispSides()
t.findArea()

# isinstance() and issubclass() are build-in function used to check inheritances
print(isinstance(t, Triangle))  # True
print(isinstance(t, Polygon))  # True
print(isinstance(t, int))  # False

print(issubclass(Polygon, Triangle))  # False
print(issubclass(Triangle, Polygon))  # True
