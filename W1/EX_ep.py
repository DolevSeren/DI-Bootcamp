import random
# EX_1


def display_message():
    print("I am learning about functions in Python.")


display_message()

# EX_2

def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("alice in wonderland")

# EX_3

def describe_city(city, country = "unknown" ):
    print(f"the city {city} is in {country}")

describe_city("tlv", "israel")
describe_city("Reykjavik", "Iceland") , describe_city("gala",  )

# EX_4



def input_number(user_number):
    number = random.randint(1, 100)
    if number == user_number:
        print("good guess!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {number}")

input_number(int(input("please provide a number between 1-100\n")))


# EX_4

def make_shirt(size = "large", text = "I Love Python"):
    print(f"the size of the shirt is {size} and the text on the shirt is {text}")

make_shirt()
make_shirt("medium",)
make_shirt(size="any size", text= "i love java")
make_shirt(size="small", text="Hello!")

magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]

def show_megicians(magician_names):
    for name in magician_names:
        print(name)

def make_great(magician_names):
    for index, each_magician in enumerate(magician_names):
        magician_names[index] = "the great " + each_magician
    print(magician_names)

show_megicians(magician_names)
make_great(magician_names)

def get_random_temp():
    random_numbers = random.uniform(-10, 40)
    if random_numbers < 0:
        print("its winter")
    elif 0 < random_numbers < 16:
        print("its fall")
    elif  16 < random_numbers < 23:
        print("its spring")
    elif  24 < random_numbers < 32:
        print("its summer")
    else:
        print("it’s really hot! Stay cool")
    return random_numbers

def main():
    random_temp = get_random_temp()
    print(f"The temperature right now is {random_temp} degrees Celsius.")
    if random_temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 < random_temp < 16:
        print("Quite chilly! Don’t forget your coat")
    elif  16 < random_temp < 23:
        print("nice weather")
    elif  24 < random_temp < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("it’s really hot! Stay cool")


main()





