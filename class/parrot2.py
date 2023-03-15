class Parrot:
    # Declaration of instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age =age

    # instance method
    def sing(self, song):
        return "{} sing {}".format(self.name, song)

    def dance(self):
        return "{} is dancing".format(self.name)


# instantiate the object
blu = Parrot('pigeon',17)

# call our instance methods
print(blu.sing("'Happiiii'"))
print(blu.dance())

# Call our instance variable (attributes)
print(blu.name)
print(blu.age)
