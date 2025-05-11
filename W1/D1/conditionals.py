#IF STATMENT


# Syntax
# if condition:
#     <indented block of code>


# secret_number = 55
# user_number = int(input("guess a number"))
# if user_number == secret_number:
#     print("congrats")
# elif user_number == 7:
#     print("oh, that's my fav number!")
# else:
#     print("nope, better luck next time!")


user_number = int(input("please pick a number between 1-100"))

if user_number % 3 == 0 and user_number % 5 == 0:
    print("fizzbuzz")
elif user_number % 5 == 0:
    print("buzz")
elif user_number % 3 == 0:
    print("fizz")


else:
    print("enter a valid number")







