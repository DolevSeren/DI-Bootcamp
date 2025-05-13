# # students = {"name": "john", "age": "20", "major": "computer since"}
# # print(students["age"])
# #
# # #basic dictionary
# #
# # rick_dict = {
# #     "first_name": "Rick",
# #     "last_name": "Sanchez"
# # }
# #
# # #more complex dictionary
# #
# # my_dog = {
# #     "name": "rufus",
# #     "age": "4",
# #     "good dog": True
# # }
# #
# # print(rick_dict["last name"])
# # print(rick_dict["age"])
# #
# # a_dict = {"color": "blue", "fruit": "apple", "pet": "dog"}
# #
# # for key, value in a_dict.items():
# #     print(key, "->" ,value)
#
# risk_dict = {
#     'first_name': 'Rick',
#     'last_name': 'Sanchez'
# }
#
# risk_dict["last_name"] = "SANCHEZ_2"
# risk_dict["age"] = 70
# risk_dict["hair_color"] = "white"
#
# print(risk_dict)
# print(risk_dict["last_name"])
# print(risk_dict["age"])
#
# del risk_dict["hair_color"]
#
# shirts = [
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'S',
#     'price': 20
#   },
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'M',
#     'price': 25
#   },
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'L',
#     'price': 30
#   },
# ]
#
# for shirt in shirts:
#   print(shirt["size"])
#
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
# user_a = {
#     'first_name': 'Bob',
#     'last_name': 'Ross',  # STOP HERE, EXPLAIN
#     'age': 53,  # EXPLAIN DATA TYPES AS VALUES
#     'address': 'Tel Aviv',  # STOP HERE EXPLAIN
#     'hobbies': ['painting', 'guitar'],  # STOP
#     'pets': [{'Rufus': 9}, {'Garfield': 8}],
#     'family': {
#         'partner': {
#             'first_name': 'Lior',
#             'last_name': 'Alon',
#             'age': 50
#         },
#         'children': [
#             {
#                 'first_name': 'Anna',
#                 'last_name': 'Ross',
#                 'age': 15,
#                 'sports': ['volleyball', 'soccer']
#             }
#         ]
#     }
# }
#
# print(user_a['first_name'])
# print(user_a['hobbies'][1])
# # print(user_a['pets'][0]['Rufus'])
#
# # students = {"name": "john", "age": "20", "major": "computer since"}
# # print(students["age"])
# #
# # #basic dictionary
# #
# # rick_dict = {
# #     "first_name": "Rick",
# #     "last_name": "Sanchez"
# # }
# #
# # #more complex dictionary
# #
# # my_dog = {
# #     "name": "rufus",
# #     "age": "4",
# #     "good dog": True
# # }
# #
# # print(rick_dict["last name"])
# # print(rick_dict["age"])
# #
# # a_dict = {"color": "blue", "fruit": "apple", "pet": "dog"}
# #
# # for key, value in a_dict.items():
# #     print(key, "->" ,value)
#
# risk_dict = {
#     'first_name': 'Rick',
#     'last_name': 'Sanchez'
# }
#
# risk_dict["last_name"] = "SANCHEZ_2"
# risk_dict["age"] = 70
# risk_dict["hair_color"] = "white"
#
# print(risk_dict)
# print(risk_dict["last_name"])
# print(risk_dict["age"])
#
# del risk_dict["hair_color"]
#
# shirts = [
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'S',
#     'price': 20
#   },
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'M',
#     'price': 25
#   },
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'L',
#     'price': 30
#   },
# ]
#
# for shirt in shirts:
#   print(shirt["size"])
#
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
# user_a = {
#     'first_name': 'Bob',
#     'last_name': 'Ross',  # STOP HERE, EXPLAIN
#     'age': 53,  # EXPLAIN DATA TYPES AS VALUES
#     'address': 'Tel Aviv',  # STOP HERE EXPLAIN
#     'hobbies': ['painting', 'guitar'],  # STOP
#     'pets': [{'Rufus': 9}, {'Garfield': 8}, ('katt', 6)],
#     'family': {
#         'partner': {
#             'first_name': 'Lior',
#             'last_name': 'Alon',
#             'age': 50
#         },
#         'children': [
#             {
#                 'first_name': 'Anna',
#                 'last_name': 'Ross',
#                 'age': 15,
#                 'sports': ['volleyball', 'soccer']
#             }
#         ]
#     }
# }
#
# # print(user_a['first_name'])
# # print(user_a['hobbies'][1])
# # print(user_a['pets'][2][0])
# #
# # for pets in user_a['pets']:
# #     print(pets[0])
#
# print(user_a['family']['partner']['last_name'])
# print(user_a['family']['children'][0]['sports'][0])
# print(user_a['family']['children'])
#
# user_a['first_name'] = "john"
#
# user_a['pets'][2] = ('garfield_2', 6)
#
# print(user_a)
#
# user_a['email'] = 'bib@gmail.com'
# print('email added: ', user_a['email'])
#
# del user_a['last_name']
# print(user_a)
#
# print('first_name' in user_a)
# print('rufus' in user_a.values())
# print(53 == user_a['age'])
#
# print('values: ', user_a.values())


sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]
for key in keys_to_remove:
  del sample_dict[key]


print(sample_dict)


