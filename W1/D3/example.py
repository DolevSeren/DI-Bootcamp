dolev_dict = {
    "name" : "Dolev",
    "age" : 20,
    "city" : "tlv",
    "wight" : 70
}
michael_dict = {
    "hight" : 175,
    "wight" : 45
}

# changing the value if it find it in the other dictionary, adding if not excist.
dolev_dict.update(michael_dict)
print(dolev_dict)
print(michael_dict)


# print(dolev_dict["name"])
# dolev_dict["age"] = 30
# print(dolev_dict["age"])
# dolev_dict["eye_color"] = "green"
# print(dolev_dict)
# del dolev_dict["eye_color"]
# print(dolev_dict)
#
# print(dolev_dict.keys())


# sample_dict = {
#    "class":{
#       "student":{
#          "name":"Mike",
#          "marks":{
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
#
# print(sample_dict["class"]["student"]["marks"]["history"])

shirts = [
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'S',
    'price': 20
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'M',
    'price': 25
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'L',
    'price': 30
  },
]
#
# # its a dictionary inside the list so we need to run over the list (iterating) and use loop.
#
# # provide the sizes of each shirt
# for shirt in shirts:
#     print(shirt["size"])
#
# # provide only the key of the dictionary
# for shirt in shirts:
#     print(shirt.keys())
#
# # provide only the values without the keys
# for shirt in shirts:
#     print(shirt.values())
#
# provide the all info in tuples (key, value)
for shirt in shirts:
    print(shirt.items())


# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
#
# }
# keys_to_remove = ["name", "salary"]
#
# for key in keys_to_remove:
#   if key in sample_dict:
#     del sample_dict[key]
#
# print(sample_dict)

# my_books = {
#   "title": "Harry Potter",
#   "author": "JK Rowling",
# }
#
# for x, y in my_books.items():
#     print("the " + x + " is " + y)
#
# # it will iterate over each item, wnd it will print the item and the index location
# for item in enumerate('abcd'):
#     print(item)
#
# for (index_count, letter) in enumerate('abcd'):
#     print('At index {} the letter is {}'.format(index_count, letter))
#
# # >>
# # At index 0 the letter is a
# # At index 1 the letter is b
# # At index 2 the letter is c
# # At index 3 the letter is d
#
# # takes several lists (or other collections) and joins the matched elements according to their position.
# list1 = [1,2,3]
# list2 = ['a','b','c']
# list3 = [1.1, 2.2, 3.3, 4.4, 5.5]
#
# for item in zip(list1, list2, list3): # only go as far it is possible
#     print(item)
# >>
# (1, 'a', 1.1)
# (2, 'b', 2.2)
# (3, 'c', 3.3)
#
# # while else
# x = 0
# while x < 2:
#     print(f'x is {x}')
#     x += 1
# else:
#     print('x is bigger than 2')
# >>
# x is 0
# x is 1
# x is bigger than 2
#
# # break, continue, pass
# for letter in 'Leonardo': # loop that check letters in Leonardo
#     if letter == 'a': #condition
#         break #break
#     print(letter, end='') # end='' showing each letter next to the other
#
# # >> Leon
#
# while True:
#     s = input('Enter something : ')
#     if s == 'quit':
#         break
#     print('Length of the string is', len(s))
# print('Done')
#
# # pass let you passs an eror if you dont want to fill everything now
# for item in [1,2,3]:
#     # comment
#     pass # to avoid the error
#
# print('Finish the script')
# # >> Finish the script
#
#
# family_age = {'Lea': 12, 'Mark': 25, 'George': 50}
# new_year = 1
# new_family_age = {name: age+new_year for (name, age) in family_age.items()}
# print(new_family_age)

# >> {'Lea': 13, 'Mark': 26, 'George': 51}





