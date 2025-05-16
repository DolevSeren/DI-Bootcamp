#ARGS and KWARGS

# def say_hello(language, user_name):
#     if language == "EN":
#         print(f"hello, {user_name}")
#
#     say_hello()
#
#     def print_names(*args):
#         for name in args:
#             print(f"hello {name}")
#         if not args:
#             print("please add name and say hello")
#
#
#     print_names()
#
# def user_info(**kwargs):
#     for info in kwargs.values():
#         print(info)
#
# user_info(name = "dolev", age = "35", address = "tlv")

# def tasks_manager(*args):
#     if args:
#         for arg in args:
#             print(f"today i need to do {arg}")
#     else:
#         print("please pass a task as argument")
#
#
# tasks_manager("go to gym", "go to office")

def party_planner(*args, **kwargs):
    if args:
        print('You need to buy: ')
        for arg in args:
            print(arg)
    else:
        print('there is no food to buy' )

    if kwargs:
        print('Party details: ')
        for key, value in kwargs.items():
            print(f' {key} : \n {value}')
    else:
        print("there is no details for this party")

party_planner("bamba " "cola" ,adress = "ben yehuda - tlv", time = "7pm", ticket_price = [20, 200, 400])
party_planner("bamba, cola")
party_planner(address =  ["tlv ben yehuda", "raanna"])

