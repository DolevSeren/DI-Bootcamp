

two_D_list = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]



def display_board():
    for row in two_D_list:
        print(' | '.join(row))



def player_input(player):
    while True:
        print(f"player {player}, enter your move: ")
        row = int(input("Row (1-3): ")) - 1
        if row < 0 or row > 2:
            print("Number must be between 1 and 3")
            continue
        location = int(input("location (1-3: ")) - 1
        if location < 0 or location > 2:
            print("you have to provide a number between 0-2")
            continue
        if two_D_list[row][location] == ' ':
            two_D_list[row][location] = player
            break
        else:
            print("That spot is already taken. Try again.")

        display_board()




def check_win(board, player):
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

def check_tie(counter):
    if counter == 9:
        print("its a tie!")
        return True



def main(player):
    current_player = "O"
    counter = 0
    while True:
        display_board()

        if check_win(two_D_list, current_player):
            print(f"Player {current_player} wins!")
            break

        elif current_player == "O":
            current_player = "X"

        else:
            current_player = "O"

        player_input(current_player)

        counter += 1

        if check_tie(counter):
            break



main("player")










