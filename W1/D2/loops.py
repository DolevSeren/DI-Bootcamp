# # LOOPS: FOR SND WHILE LOOPS
# from W1.D1.conditionals import user_number
#
# # FOR LOOP:
fruits = ["apple", "banana", "kiwi", "pear"]
#
# for each_fruit in fruits:
#     print(f"i love {each_fruit}")
# #
# for i in range(1,10):
#     print(i)
#
for i in range(len(fruits)+1):
    print(i)
#
# odd_nums = list(range(1, 11, 2))
# print(min(odd_nums))
# print(max(odd_nums))
# print(sum(odd_nums))
#
# # WHILE LOOP: CONDITION
#
num = 1
while num <= 10:
    if num == 5:
        break
    print(num)
    num += 1


# secret_number = 77
# user_number = int(input("pick a number"))
#
# while int(user_number) != secret_number:
#     print("not the number, try again, or type q to quit")
#     if user_number == "q":
#         print("exiting the game!")
#         break
#     else:
#         user_number = int(input("pick a number"))
# else:
#     print("you won!")
