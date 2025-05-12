# EX_1
from time import monotonic

my_fav_numbers = {"9", "99", "3", "8"}
my_fav_numbers.update("5", "6")
print(my_fav_numbers)
my_fav_numbers.remove("6")

friend_fav_numbers = {"6", "77", "81", "2"}
my_fav_numbers.update(friend_fav_numbers)
print(my_fav_numbers)

# EX_2
my_tuple_of_integers = ("1", "2", "3", "4")
temp_list = list(my_tuple_of_integers)
temp_list.extend(["5,", "6", "7"])
my_tuple_of_integers = tuple(temp_list)
print(my_tuple_of_integers)

# EX_3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("kiwi")
basket.insert(1, "Apples")
x = basket.count("Apples")
print(x)
basket.clear()
print(basket)

# EX_4

n = 1.5
while n < 5:
    print(n)
    n += 0.5

# EX_5

for i in range(1,21):
    print(i)

for index, value in enumerate(range(1, 21)):
    if index % 2 == 0:
        print(value)

# EX_6

name = "dolev"
user_name = input("what is your name?")

while name != user_name:
    print("this is not my name")
    if user_name == name:
        break
    else:
        user_name = input("what is your name?")

    # EX_7


fruits = input("please provide your favorite fruits, you can input several fruits, (separated by spaces)")
print(fruits.split(sep=' '))
pick_a_fruit = input("please pick a fruit")
if pick_a_fruit in fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# EX_8

end_asking = "quit"

topping =""

list_toppings = []

while topping != end_asking:

    topping = input("what topping do you want on your pizza?")
    if topping != end_asking:
        list_toppings.append(topping)
        print(f"adding {topping} to your pizza")

print("thats a great pizza! youve orderd + ", list_toppings )

pizza_price = 10
topping_price = len(list_toppings) * 2.5
pizza_price += topping_price

print(pizza_price)

# EX_9

total_cost = 0

num_people = int(input("How many people in the family want to buy a ticket? "))

for i in range(num_people):
    age = int(input(f"Enter the age of person {i+1}: "))
    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15
    total_cost += cost

print(f"The total cost for the tickets is: ${total_cost}")

# EX_10

sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

finish_sandwiches = []

for sandwich in sandwich_orders:
    print(f"i made your {sandwich} sandwich")
    finish_sandwiches.append(sandwich)

print("\nFinish sandwiches:", finish_sandwiches)

















