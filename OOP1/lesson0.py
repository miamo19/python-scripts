class Student:
    school = "GBHS Atiela\n"
    town = input("Enter name of your town: ")
    def __init__(self, a, b, c):
        self.math = a
        self.chem = b
        self.bio = c

    def avg(self):
        return (self.chem + self.bio + self.math)/3
    @classmethod
    def info(cls):
        return "you are from "+ cls.town + " schooling at "+ cls.school

s1 = Student(5, 6, 12)
print(Student.avg(s1))
print(s1.avg())

#print(Student.info())