# #EX_1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dictionary = {"ten" : 10, "twenty" : 20, "thirty" : 30}

print(new_dictionary)

# # ex_2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0

for name, age in family.items():
    if age < 3:
        total_cost += 0
    elif age <= 12:
        total_cost += 10
    else:
        total_cost += 15
print("total cost: " + str(total_cost))

for name, age in family.items():
    if age < 3:
        print(name + " is a child ticket is free")
    elif age <= 12:
        print(name + " is a teenager ticket is 10")
    elif age > 12:
        print(name + " your an adult ticket is 15")

num_members = int(input("How many family members? "))
family = {}
for i in range(num_members):
    name = input(f"Enter the name of family member {i+1}: ")
    age = int(input(f"Enter the age of {name}: "))
    family[name] = age
total_cost = 0

for name, age in family.items():
    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15
    print(f"{name} pays ${cost}")
    total_cost += cost

print("Total cost for the family is:", total_cost)

# EX_3

brand = {"name" : "zara",
              "creation_date" : 1975,
                "creator_name" : "Amancio Ortega Gaona",
              "type_of_clothes" : ["men", "women", "children", "home"],
              "international_competitors" : ["Gap", "H&M", "Benetton"],
              "number_of_stores" : 7000,
              "major_color" : {"france" : "blue", "spain" : "red", "us" : ["pink", "green"]}
              }


brand["number_of_stores"] = 2
print("zara is for every one of these: ", brand["type_of_clothes"])
brand.update({"country_creation" : "spain"})
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
last_brand = brand["international_competitors"][-1]
print(last_brand)
print(brand["major_color"]["us"])
list_of_keys = list(brand.keys())
print(len(list_of_keys))
print(list_of_keys)

more_on_zara = {
    "creation_date" : 1975,
    "number_of_stores" : 7000,
}
brand.update(more_on_zara)
print(brand)

# Ex_4

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
new_dict = {value: index for index, value in enumerate(users)}
new_dict1 = {index: value for index, value in enumerate(users)}
print(new_dict)
print(new_dict1)
sorted_names = users.sort()
sorted_names_1 = {value: index for index, value in enumerate(users)}
print(sorted_names_1)

