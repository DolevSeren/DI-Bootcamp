from game import Game

def get_user_menu_choice():
    user_menu_choice = input("please enter your choice - (play game, show scores, quit)")
    while user_menu_choice.lower() not in ["play game" , "show scores", "quit"]:
        user_menu_choice = input("invalid choice, please enter your choice - (play game, show scores, quit")
    return user_menu_choice.lower()

def print_result(results):
    print("\nScore Summary:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")



def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        choice = get_user_menu_choice()
        if choice == "play game":
            result = Game().play()
            if result == "win":
                results["win"] += 1

            if result == "loss":
                results["loss"] += 1

            if result == "draw":
                results["draw"] += 1


        elif choice == "show scores":
            print_result(results)


        elif choice == "quit":
            print_result(results)
            break



if __name__ == "__main__":
    main()





