class Pets:
    def __init__(self, animals):
        self.animals = animals
    def walk(self):
        for animal in self.animals:
            print(animal.walk())



class Cat(Pets):
    def __init__(self, animals, sing, jumps, name, age):
        super().__init__(animals)
        self.sing = sing
        self.jump = jumps
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is walking"


class Siamese(Cat):
    def __init__(self, animals, sing, jumps, short_hair, meow, name, age):
        super().__init__(animals, sing, jumps, name, age)
        self.short_hair = short_hair
        self.meow = meow

class Bangal(Cat):
    def __init__(self, animals, sing, jumps, long_hair, name, age):
        super().__init__(animals, sing, jumps, name, age)
        self.long_hair = long_hair




all_cats = [Siamese(True,"lowed", "low", True, "yes", "sami", 9), Bangal(True,"very loud", "high", "short", "kati", 3)]


sara_pets = Pets(all_cats)
sara_pets.walk()

#  ex_2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self,other_dog):
        if self.run_speed()*self.weight > other_dog.run_speed()*other_dog.weight:
            return f"{self.name} won the fight"
        else:
            return f"{other_dog.name} won the fight"


dog1 = Dog("zeevik", 12, 40)
dog2 = Dog("taxi", 29, 400)


print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))