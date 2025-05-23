import random


class Game:
    def get_user_item(self):
        user_item = input("Please choose an item (rock/paper/scissors): ").lower()
        while user_item not in ["rock", "paper", "scissors"]:
            user_item = input("Invalid choice. Please choose again (rock/paper/scissors): ").lower()
        return user_item

    def get_computer_item(self):
        list_of_items = ["rock", "scissors", "paper"]
        computer_item = random.choice(list_of_items)
        return computer_item

    def get_game_result(self, user_item, computer_item):
        self.user_item = user_item
        self.computer_item = computer_item
        rules = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

        if self.user_item == self.computer_item:
            return "draw"

        elif rules[self.user_item] == self.computer_item:
            return "win"

        else:
            return "lose"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"\nYou chose: {user_item}")
        print(f"Computer chose: {computer_item}")
        print(f"Result: {result}\n")

        return result














