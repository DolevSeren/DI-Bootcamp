# challenge 1

number = int(input("please provide a number"))
length = int(input("please provide a length"))

multiple_list = []

for i in range(1, length + 1):
    multiple_list.append(number * i)

print("The list of multiples is:", multiple_list)

# challenge 2

user_input = input("please provide a string")

new_string = ''
previous_char = ''

for current_char in user_input:
    if current_char != previous_char:
        new_string += current_char
    previous_char = current_char

print("your new string is ", new_string)






