# # xp gold
#
# list_1 = [1, 3, 5]
# list_2 = [2, 4, 6]
# combined = []
#
# for item in list_1:
#     combined.append(item)
#
# for items in list_2:
#     combined.append(items)
#
# print(combined)
#
# # list_1.extend(list_2)
# # print(list_1)
#
# for i in range(1500, 2500):
#     if i % 5 == 0:
#         print(i)
#     elif i % 7 == 0:
#         print(i)
#
# user_number_1 = int(input("please provide a number"))
# user_number_2 = int(input("please provide a number"))
# user_number_3 = int(input("please provide a number"))
# list_of_numbers = []
#
# list_of_numbers.extend([user_number_1, user_number_2, user_number_3])
# print(max(list_of_numbers))
#
#
# import string
#
# letters = string.ascii_lowercase
# vowels = ["a", "e", "i", "o", "u"]
# for letter in letters:
#     if letter in vowels:
#         print(letter + " vowlel")
#     else:
#         print(letter + " consonant")

# word_list = []
# for number in range(7):
#     user_word = input("please provide word")
#     word_list.append(user_word)
#
# ask_for_letter = input("please provide single character")
# for word in word_list:
#     if ask_for_letter in word:
#         index = word.index(ask_for_letter)
#         print("the letter is the ", index , " character in the word")
#     else:
#         print("letter in word not found")

#
# list_of_numbers = []
# for i in range(1, 1000001):
#     list_of_numbers.append(i)
# print(list_of_numbers)
# print(min(list_of_numbers))
# print(max(list_of_numbers))
# sum = sum(list_of_numbers)
# print(sum)

# list_of_num = []
# list_of_numbers = input("please provide couples of numbers seperated with commas:")
# x = list_of_numbers.split(",")
# list_of_num.extend(x)
# print(list_of_num)
#
# # num_list = list(list_of_numbers)
# # num_list.extend([list_of_num])
# my_tuple = tuple(list_of_num)
# print(my_tuple)

import random
number = int(input("please provide number between 1-9 or q to exit\n"))
random_number = random.randint(1, 9)
while number != "q":
    print(random_number)
    if number == random_number:
        print("good guess!")
    else:
        print("not the number, guess again ot type q to exit")
    number = int(input("please provide number between 1-9 or q to exit\n"))
    random_number = random.randint(1, 9)































