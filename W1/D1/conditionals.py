# CONDITIONALS : IF STATEMENTS

#SYNTAX
# if condition:
#     <indented block of code>

secret_number = 55
user_number = int(input('Guess a number: '))

if user_number == secret_number:
    print('Congrats, you won!')

elif user_number == 7:
    print('Oh, that\'s my fav number')

else:
    print('Sorry, not the same number')

#exercise
number = int(input('add a number from 0 to 100: '))

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')

elif number % 5 == 0:
    print('Buzz')

elif number % 3 == 0:
    print('fizz')

else:
    print('not valid')