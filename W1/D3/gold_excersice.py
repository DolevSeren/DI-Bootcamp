

# birthday = {"dolev" : "1996/11/26" ,
#             "yuval" : "1996/05/25",
#             "michael" : "1997/06/11",
#             "harry" : "1998/02/14",
#             "dana" : "1997/12/10"}
#
# print("welcome! you can look up the bday of any person in the dictionary")
# user_person_name = input("please provide a name/n")
# user_birthday = input("please provide a birthday (in the format “YYYY/MM/DD”)/n")
#
# user_input = input("please provide a name/n")
# if user_input in birthday:
#     print(birthday[user_input])
#
# if user_person_name not in birthday:
#     birthday[user_person_name] = user_birthday
#     print(birthday)

items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for key, value in items.items():
    print(f"{key}" + " price is " + str(value) + "$")

items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

total_cost = 0

for key in items:
    price = items[key]["price"]
    stock = items[key]["stock"]
    cost = price * stock
    total_cost += cost
    print(f"{key} price is {price}$ and for all the amount ({stock}) the cost is {cost}$")

print(f"\nTotal cost to buy everything: {total_cost}$")



