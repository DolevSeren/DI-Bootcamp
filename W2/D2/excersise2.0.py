# from W1.D2.tuples_and_sets import names
# from excersise_xp import Dog
# import random
#
# class PetDog(Dog):
#     def __init__(self, name, age, weight, trained=False):
#         super().__init__(name, age, weight)
#         self.trained = trained
#
#     def train(self):
#         print(self.bark())
#         self.trained = True
#
#
#     def play(self, *args):
#         names1 = [self.name] + [dog.name for dog in args]
#         names_str = ", ".join(names1)
#         print(f"{names_str} all play together")
#
#     def do_a_trick(self):
#         if self.trained:
#             tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
#             print(f"{self.name} knows how to {random.choice(tricks)}")
#
#
#
#
#
#
# dog_4 = PetDog("dolev", 13, 23, True)
# dog_a = PetDog("Zeevik", 5, 20, False)
# dog_b = PetDog("Taxi", 3, 18,True)
# dog_c = PetDog("Pau", 2, 12,False)
# dog_4.train()
# dog_a.play(dog_b, dog_c)
# dog_4.do_a_trick()



#######################################################################################################################

class Person:
    def __init__(self, first_name, age, last_name = ""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age, self.last_name)
        self.members.append(new_person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")

    def family_presentation(self):
        print(self.last_name)
        for person in self.members:
            print(f"{person.first_name} {person.age}")

new_last_name = "Seren"
seren_family = Family(new_last_name)
print(seren_family.__dict__)
seren_family.born("dolev", 18)
seren_family.born("omri", 12)
seren_family.check_majority("dolev")
seren_family.check_majority("omri")
seren_family.family_presentation()


















