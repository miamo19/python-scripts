class A:
    def __init__(self):
        print("All is fine A")
    def features(self):
        print("this feature is working")
    def features1(self):
        print("this feature1 is working")

class B:
    def __init__(self):
        print("All is Good  for B")

    def features2(self):
        print("this feature2 is working")

    def features3(self):
        print("this feature3 is working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("All is Good  for C")

    def features1(self):
        super().__init__()
        print("this feature2 is working C")

    def features4(self):
        print("this feature3 is working")
i=C()
print(i)
print(i.features2())
