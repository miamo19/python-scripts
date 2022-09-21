        #concept of innerclass
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Computer()

    def all(self):
        print(self.name, self.rollno)
        self.lap.all

        #inner class
    class Computer:
        def __init__(self):
            self.brand = 'hp'
            self.cpu = 'i5'
            self.ram = '16GB'

        def all(self):
            print(self.brand, self.cpu, self.ram)

        #create an object (c1) of the inner class inside the inner class
    c1 = Computer()
    print(c1.ram)
    print(c1.all())

  #create an object (c0) of the inner class outside the inner class
c0 = Student.Computer()
print(c0.cpu)
print(c0.all())

  #object of the outer class
s0= Student("nadia", 25)
s1 = Student("Lauence", 28)
print(s0.all())
