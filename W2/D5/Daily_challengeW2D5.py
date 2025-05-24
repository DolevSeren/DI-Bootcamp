# EX_1


# Answer the following questions:
#
# class is blueprint or template for creating objects. id defines a set of attributes and behaviors that the created object will have.
# What is a class? = class is blueprint or template for creating objects. id defines a set of attributes and behaviors that the created object will have.
# What is an instance? = is a specific object created from a class it contains real values for the class attributes and can use the classes methods.
# What is encapsulation? = is the concept of bundling data and methods that operate on that data into a single unit and restricting direct access to some of the objects components.
# What is abstraction? = is the concept of hiding complex implementation details and showing only the essential features of an object.
# What is inheritance? = allow a class to inherit attributes and methods from another class.
# What is multiple inheritance? = is when a class inherits from more than one class.
# What is polymorphism? = allows objects of different classes to be treated as an instances of the same class through a shared interface
# What is method resolution order or MRO? = is the order in which python looks for a method in a hierarchy of classes especially in multiple inheritance
# What is method resolution order or MRO? = class is blueprint or template for creating objects. id defines a set of attributes and behaviors that the created object will have.

import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []

    def shuffle(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            random_card = self.cards.pop()
            return random_card
        else:
            return None


deck = Deck()
deck.shuffle()
card = deck.deal()
print(card)





















