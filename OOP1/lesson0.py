class Student:
    school = "GBHS Atiela\n"
    town = input("Enter name of your town: ")
    def __init__(self, a, b, c):
        self.math = a
        self.chem = b
        self.bio = c

    def average(self):
        return (self.chem + self.bio + self.math)/3
 
#An example of a Class Method    
    @classmethod
    def info(cls):
        return "You are from "+ cls.town + " schooling at "+ cls.school

s1 = Student(5, 6, 12)
print(Student.average(s1))

#Or You can instanciate as shown below
print(s1.average())

#print(Student.info())  Or Print(s1.info()) 
