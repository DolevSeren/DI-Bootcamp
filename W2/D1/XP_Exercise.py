from tokenize import group


class Cat:
    def __init__(self,name,  age):
        self.name = name
        self.age = age

    def oldest_cat(self, cats):
        oldest_age = 0
        #our_cat=''
        for cat in cats:
            if cat.age > oldest_age:
                oldest_age = cat.age
                our_cat = cat
        return our_cat

cat_dolev = Cat("dolev", 28)
cat_naomie = Cat("naomi", 24)
cat_emily = Cat("emily", 37)

cats = [cat_dolev, cat_naomie, cat_emily]
oldest_cat=cat_emily.oldest_cat(cats)
print(f'Our oldest cat is: {oldest_cat.name} and he is {oldest_cat.age}')


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} is barking")
        pass

    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high!")


davids_dog = Dog("rex", 15 )
print(davids_dog.__dict__)


sarahs_dog = Dog("zeevik", 40)
print(sarahs_dog.__dict__)

my_dogs = [sarahs_dog, davids_dog]

for dog in my_dogs:
    dog.jump()

for dog in my_dogs:
    dog.bark()

if sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}")
elif sarahs_dog.height < davids_dog.height:
    print(f"{sarahs_dog.name} is smaller than {davids_dog.name}")
else:
    print(f"{sarahs_dog.name} and {davids_dog.name} are the same size!")


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for song in self.lyrics:
            print(song)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

class Zoo:
    def __init__(self,zoo_name ):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)


    def get_animals(self):
        print(my_zoo.animals)

    def sell_animal(self, animal_sold):
         if animal_sold in self.animals:
             self.animals.remove(animal_sold)
             print(f"{animal_sold} , been sold")

    def sort_animals(self):
        self.animals.sort()
        grouped_animals = {}

        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = [animal]
            else:
                grouped_animals[first_letter].append(animal)
        return grouped_animals

    def get_groups(self):
        grouped_animals = self.sort_animals()
        for letter, animals in grouped_animals.items():
            print(f"{letter}: {animals}")













my_zoo = Zoo ("dolevs zoo",)
my_zoo.add_animal("babon")
my_zoo.add_animal("bear")
my_zoo.add_animal("cat")
my_zoo.add_animal("cougar")
my_zoo.add_animal("giraffe")
my_zoo.add_animal("lion")
my_zoo.add_animal("zebra")
my_zoo.get_animals()
my_zoo.sell_animal("lion")
my_zoo.get_groups()

dolevs_zoo = Zoo("dolevs zoo")
print(dolevs_zoo.__dict__)


