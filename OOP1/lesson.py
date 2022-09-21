class Student:
    def check_if_pass(self, mark):
        self.m= mark
        if self.m >= 45:
            return True
        else:
            return False
        
s1 = Student()

s1.check_if_pass(16) 
if s1.m >=45:
    print ("You pass")
else:
    print("You Fail")