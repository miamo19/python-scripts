class Parrot:
    species = 'Bird'
    def __init__(self, name, age):
        self.name= name
        self.age= age

blu = Parrot('pigeon', 41)
woo = Parrot('riptite',18)

print('blu is of the species {}'.format(blu.__class__.species))
print('blu is of the species', blu.__class__.species)
