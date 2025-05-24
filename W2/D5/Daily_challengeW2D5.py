

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
            print(len(self.cards))
            print(random_card)
        else:
            return None

    def play(self):
        while len(self.cards) > 0:
            self.deal()

deck = Deck()
deck.shuffle()
card = deck.deal()
print(card)
deck.play()





















