# FUNCTION
#syntax

# def function_name():
#     '''discribe what this function does''' #docs strings
#     print("i am a function")
#
# function_name()
# print(function_name.__doc__)

# create a function called greeting that prints "hello" in your mother tounge
# then call the function and run the file

#passing arguments to the function
def greeting(language = "PT",user_name = "dolev"):
    if language == "PT":
        print(f"ola {user_name}")
    elif language == "RU":
        print(f"priviat {user_name}")
    elif language == "HEB":
        print(f"shalom {user_name}")
    else:
        print("undefined language")

#keyword arguments
greeting(user_name = "ilia", language="RU")
greeting("RU", "EMILY")
greeting(user_name = "yuval")
greeting()


# create a function called country_source that receives a country name as argument
# and print the capital of that country. make sure the country name argument default
# Baku

def country_source(country_name = "BAKU"):
    if country_name == "israel":
        print("jerusalem")
    elif country_name == "italy":
        print("rome")
    elif country_name == "spain":
        print("madrid")
    elif country_name == "BAKU":
        print("theed")
    else:
        print("country doesnt excist in my world")

country_source()
country_source("israel")
country_source("italy")
country_source("peru")

def calculation(nume1, num2):
    result = nume1 + num2
    return result

countries = ["brazil", "israel", "italy", "spain"]

def country_info(countries):
    for country in countries:
        if country == "brazil":
            return country

print(country_info(countries))

# print(calculation(5, 4))
# calculation_result = calculation(5, 4)
# print(calculation_result + 10)



# def say_hello(hello_language):
#     if hello_language == "HEB":
#         print("shalom")
#     elif hello_language == "ESP":
#         print("HOLA QUE TAL")
#
# say_hello("ESP")
#
# "Hello sunshine".replace("sunshine", "pretty")

# SCOPES
# global scope: on the file in general
#local scope: indented block(if statement, a for loop, a function...)

# global_var = 100
# def calculation(a,b):
#     addition = a+b
#     subtraction = a-b
#
#     return addition, subtraction
#
# additional, substraction = calculation(5,7)
# print(additional, substraction)
# print(global_var)

def greet(name):
    return "Hello, " + name

message = greet("Alice")

greet()

