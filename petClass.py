class Pet(object):

    life = 1


    def __init__(self, name, age):
        self.name = name
        self.age = age

    def killPet(self):
        self.life = 0




class Bird(Pet):

    def __init__(self, name, age, breed):
        super(Bird, self).__init__(name,age)
        self.breed = breed



pet2 = Pet('Rocky')


pet1 = Bird('Polly', 23, 'Parrot')


print pet1.name.breed

#print pet1.name, pet1.age, pet1.breed, pet1.life
