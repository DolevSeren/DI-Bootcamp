# Ex_1 =

print("hello world " * 4 )

# Ex_2 =

answer = (99**3)*8
print(answer)

# Ex_3 =

# >>> 5 < 3 = False
# >>> 3 == 3 True
# >>> 3 == "3" False
# >>> "3" > 3 Eror
# >>> "Hello" == "hello"

# Ex_4 =

computer_brand = "apple"
print("i have a " + computer_brand + " computer")

# Ex_5 =

name = "dolev"
age = "28"
shoe_size = "43"
info =  (f"my name is {name} im {age} years old. my shoes size is {shoe_size}")
print(info)

#Ex_6 =

a = 5
b = 4

if a > b:
    print("hello world")

#Ex_7 =

number = int(input("please provide a number"))
if number % 2 == 0:
    print("your number is even")
else:
    print("your numner is odd")

#Ex_8 =

name = input("what is your name?")
if name == "dolev":
    print("OMG We have the same name!")
else:
    print("thats a pretty name, though its not the prettiest")

height = int(input("please provide your height in cm"))
if height > 145:
    print("you can ride the roller coaster!")
else:
    print("you need to grow some more to ride")

# Ex_XP_GOLD

# Ex_1

print("hello world " * 4 , "I love python " * 4)

# Ex_2

month = (int(input("please provide a month(1-12)")))
if month in (3, 4, 5):
    print("its spring!")
elif month in (6, 7, 8):
    print("its summer")
elif month in (9, 10 , 11):
    print("its autumn")
else:
    print("its winter")





