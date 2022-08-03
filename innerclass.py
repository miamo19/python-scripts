class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Computer()

    def show(self):
        print(self.name , self.rollno)
        self.lap.show()

    class Computer:
        def __init__(self):
            self.brand = 'PH'
            self.cpu = 'i5'
            self.ram = '8gb'

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('miami',27)
s2 = Student('nadia', 22)

#print(s1.show())
print(s2.show())