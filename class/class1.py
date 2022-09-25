class Student:
    def check_pass_fail(self):
        if self.marks>=45:
            print("Passed")

        else:
            print("Failed")

student1 = Student()
student2 = Student()

student1.marks=52
student2.marks=44
print(student1.check_pass_fail())
print(student2.check_pass_fail())
