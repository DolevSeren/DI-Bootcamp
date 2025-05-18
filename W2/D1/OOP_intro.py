# OOP: OBJECT ORIENTD PROGRAMING

#wht is an object?
# what is class?

# How to create a class

class Dog:
    def __init__(self, name, color, breed, age):
        print("creating object")
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age

    #how to create methods of the classes
    def bark(self):
        print(f"{self.name} is barking")
        pass

    def walking(self, meters):
        print(f"{self.name} is walking {meters}")

    def birthday(self):
        self.age += 1
        return self

    def rename(self, name):
        self.name = name
        return self


    #An instance (or object) of class Dog is created:
# shelter_dog = Dog()

#creating attributes to the instance
# shelter_dog.color = "black"
# print(shelter_dog.color)


# creating the instances of dog after creating the __init___ method:
shelter_dog = Dog("rex", "black","shelter", 5 )
print(shelter_dog.__dict__)


german_shepperd = Dog("zeevik", "brown", "shepperd", 12)
print(german_shepperd.name, german_shepperd.color, german_shepperd.age)

terior = Dog("taxi", "white", "terior", 1)
print(terior.__dict__)

my_dogs = [shelter_dog, german_shepperd, terior]
print(my_dogs)

# for dog in my_dogs:
#     print(dog.name)

# print(type(terior))
#
# my_dogs_objects = [obj for obj in globals().values() if isinstance(obj,Dog)]
#
# print(my_dogs_objects)



for dog in my_dogs:
    print(dog.walking(500))

german_shepperd.rename("jojo")
print(german_shepperd.name)
