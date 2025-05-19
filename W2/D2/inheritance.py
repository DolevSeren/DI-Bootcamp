class Parent:
    def speak(self):
        print(f'Parent is speaking')


class Child(Parent):
    pass


class Grandchild(Child):
    pass


obj1 = Child()
obj1.speak()

obj2 = Grandchild()
obj2.speak()


class Animal:
    def __init__(self, name, family, legs):
        self.name = name
        self.family = family
        self.legs = legs
        self.full_name = f'{name} {family}'


class Dog(Animal):
    def __init__(self, name, family, legs, trained, age):
        super().__init__(name, family, legs)
        self.trained = trained
        self.age = age

    def bark(self):
        print(f'A {self.name} is barking')

    def sleep(self):
        return f'{self.name} is sleeping - from the Dog class'


class Cat(Animal):
    def __init__(self, name, family, legs, friendly, nick_name):
        super().__init__(name, family, legs)
        self.friendly = friendly
        self.nick_name = nick_name

    def get_crazy(self):
        print(f'a {self.name} is running with its {self.legs} legs in full power')


class Alien:
    def __init__(self, personal_name, planet):
        self.personal_name = personal_name
        self.planet = planet

    def fly(self):
        return f'{self.name} is flying around'

    def sleep(self):
        return f'{self.name} is sleeping - from the Alien class'

    def make_sound(self):
        return f'{self.name} is making a sound from Alien'


class AlienDog(Alien, Dog):
    def __init__(self, name, family, legs, trained, age, personal_name, planet):
        Alien.__init__(self, personal_name, planet)
        Dog.__init__(self, name, family, legs, trained, age)



#############################################################
# create a Cat class that inherit from Animal.
# create a method get_crazy that prints
# "a {self.name} is running with its {self.legs} legs in full power"

# add two other attributes specifically to the Dog class: trained (boolean), age (int)
# user the super().__init__() to do so
# create an instance of Dog after that and analyse what changed


lion = Animal('Lion', 'Felidae', 4)
print(lion.__dict__)

dog_1 = Dog('Dog', 'Canidae', 4, True, 5)
dog_1.bark()

cat_1 = Cat('Cat', 'Felidae', 4, True, 'cute cute')
cat_1.get_crazy()

aliendog1 = AlienDog('Dog', 'Canidae', 4, True, 3, 'Rexi', 'Saturn')


print(aliendog1.name, aliendog1.family, aliendog1.planet, aliendog1.personal_name)
print(aliendog1.sleep())

# if we want to call the method in some specific parent class (not by order of inheritance) we can do:
print(Dog.sleep(aliendog1))