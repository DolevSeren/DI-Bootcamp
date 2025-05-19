#Try and Except block

hello = 'Hello World'

if hello == 'Hello World':
    print('Thats right')



# board = ['-','-','-',
#          '-','-','-',
#          '-','-','-',]

# def player_input(current_player):
#     valid = False
#     while not valid:
#         position = input('enter position 1-9: ')
#         try:
#             position = int(position) - 1
#             if 0 <= position < 9 and board[position] == '-':
#                 board[position] = current_player
#                 print(board)
#                 valid = True
#             else:
#                 print('position not in the range 1-9. ')
#         except:
#             print('Please enter a number')
#             continue


# player_input('X')

my_list = [2,3,1,2,'jhddcjhbd',42,1,5,3,]

try:
    print('from try block: ', sum(my_list))
except:
    clean_list = []
    for element in my_list:
        if isinstance(element, int):
            clean_list.append(element)
            output = sum(clean_list)
            print('from except block', output)




