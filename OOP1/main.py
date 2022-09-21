class Student():
    def check_if_pass(self):
        if self.mark >45:
            return  "Passed"
        else:
            return "Failed"

    def __init__(self, name):
        self.name = name
#s1 = Student(input("Enter your name: "))

while 1:
    s1 = Student(input("Enter your name: "))
    s1.mark = float(input("Enter your total mark: "))
    if s1.mark>=0:
        print("Hello", s1.name,"your total mark is:",s1.mark,"you have ", s1.check_if_pass())
    else:
        exit()
