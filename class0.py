class Student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False


student1 = Student()
student2 = Student()
student1.marks = 15
print(student1.check_pass_fail())
