#Scripts demonstrating Multiple Inheritance
class Apple:
    def __init__(self):
        print("All is fine Apple")
    def features(self):
        print("this feature is working")
    def features0(self):
        print("this feature1 is working")

class Bitter:
    def __init__(self):
        print("All is Good  for Bitter")

    def features2(self):
        print("this feature2 is working")

    def features3(self):
        print("this feature3 is working")

#Multiple Inheritance
class Fruit(Apple, Bitter):
    def __init__(self):
        super().__init__()
        print("All is Good  for Fruit")

    def features0(self):
        super().__init__()
        print("this feature2 is working Fruit")

    def features4(self):
        print("this feature3 is working")
fruit1=Fruit()
print(fruit1)

print(fruit1.features2())

print(fruit1.features0())
