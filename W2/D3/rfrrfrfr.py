class Animal:                         # Parent
    def speak(self):
        return "Some generic sound"

class Dog(Animal):                    # Child
    def bark(self):
        return "woof!"

class Flyer:
    def move(self):
        return "Flying"

class Swimmer:
    def move(self):
        return "Swimming"

class Duck(Swimmer, Flyer):
    def move(self):
        first = super().move()       # super() יפנה ל-Flyer
        return first + " and quacking"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Cow(Animal):
    def speak(self):
        return "Moo"

class Sheep(Animal):
    def speak(self):
        return "baa"

pets = [Dog(), Cat(), Cow(), Sheep()]
for pet in pets:
    print(pet.speak())

user_input = input("Give me a number: ")

try:
    num = int(user_input)
    print(num * 2)
except ValueError:
    print("That's not a number! 😢")





bobi = Dog()
print(bobi.speak())   # → "Some generic sound"
print(bobi.bark())
donald = Duck()
print(donald.move())
