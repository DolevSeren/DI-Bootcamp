# BASIC VALUE TYPES

#STRINGS: is a sequence of chars that represents text in python"
'Hello Python'

# STRINGS METHODS
# print('hello python'.capitalize())
# print('hello python'.upper())
# print('HELLO PYTHON'.lower())

# print('Goodnight Moon'.replace('Moon', 'Honey'))

# 3 strings: SEQUENCE of chars: IT ALLOW US TO USE INDEXES (POSITIONS)
# greetings = 'Hello Python'
# # print(greetings[6:12]) #slicing a string
# print(greetings[2])

# #   exercise
# description = "strings are..."

# print(description.upper())
# print(description.replace('are', 'is'))
# print(description[:7])

#NUMBERS: INTEGER, FLOAT, COMPLEX
# a = 5 #int
# b = 2.7 #float

# c = 5 + 3
# print(c)
# d = 5 - 2
# print(5 - 2)

# print(5*2)
# print(5**2)

print(10/2)
print(11//2) #floor division
print(11%2) #modulus division
print(round(10/3 , 2))


# TYPE CASTING
# my_age = 35

# print('Hello, my name is Juliana, I am ' + str(my_age) + ' years old')

# price = '150'

# result = int(price) + 5
# print(result)

# user_age = int(input('What is your age? '))
# print(user_age + 50)

# BOOLEANS: True or False values

# COMPARISON OPERATORS
# print(3 > 4)
# print(3 < 4)
# print(3 <= 4)
# print(4 <= 4)
# print(4 == 4)
# print(4 == '4')

#COMPARISON KEY WORDS
# print('JS' is 'Python')
# print('Python' is 'Python')
# print('Python' is not 'Python')

a = 3000
b = 3000


print(a == b) #True
print(a is b) #
print(id(a))
print(id(b))

print(bool(1))

#exercise
bank_balance = '33000'
phone_number = 532287514

print(type(int(bank_balance)))
print(type(str(phone_number)))
print(type(bank_balance))

#STRING FORMATING: F string

print(f'your bank balance is {bank_balance}, therefore you can take a loan.')

#before f-strings - i.e before python 3 we used format():
name = 'Juliana'
age = 35

message = 'My names is {}, I am {} years old'.format(name, age)
print(message)

user_name = 'Juliana'
welcome_message = f'{user_name}, welcome'

#VARIBLES: NAMING
my_address = 'Ramat Gan'

# VARIABLES THAT ARE CONSTANT
PI = 3.14
TEUDAT_ZEUT = 256666651

#INCREMENTING VARIABLES
score = 0
score += 5
print(score)

my_string = 'Julian'
my_string += 'a'
print(my_string)

