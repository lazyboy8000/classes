



class Pet(object):

    life = 1

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def killPet(self):
        self.life = 0

class Bird(Pet):

    def __init__(self,name,age,feathers):
        super(Bird, self).__init__(name, age)
        self.feathers = feathers


pet1 = Bird('Polly', 33, 7)


print pet1.name, pet1.age, pet1.feathers
