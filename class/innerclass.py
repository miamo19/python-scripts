#Inner Class example
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Computer()

    def show(self):
        print(self.name , self.rollno)
        self.lap.show()
   
    #inner class
    class Computer:
        def __init__(self):
            self.brand = 'PH'
            self.cpu = 'i5'
            self.ram = '8gb'

        def show(self):
            print(self.brand, self.cpu, self.ram)
            
        #If you will need to use somewhere in you project the method show() only for the inner class, then you can create an instance here
        com = Computer()


s1 = Student('miami',27)
s2 = Student('nadia', 22)

print(s1.show())
print(s2.show())

print(s1.name)
print(s1.rollno)

#if you need to use the show() method just for the inner class
s1.com.show()
