#A simple class that check for passed and failed
class Student:
    def check_if_pass(self, mark):
        self.mark= mark
        if self.mark >= 50:
            return True
        else:
            return False
        
student1 = Student()

student1.check_if_pass(16) 
if student1.mark >=45:
    print ("You pass")
else:
    print("You Fail")
