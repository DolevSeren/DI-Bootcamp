# Lists: orderd sequence
from idlelib.replace import replace

#A list is a sequence of elements.

#Syntax
some_list = list("item 1") # to convert other sequence in a list
other_list = ["item 1"] # the best way to create an empty list

print(len(some_list))

# accessing by index
print(some_list[1])

# methods for lists
some_list.append("A")
print(some_list)

some_list.extend(["b", "c" , "d"]) # let you add more than one element each time

# create an empty list called names and add 4 names of your fav:

list_of_players = []
list_of_players.extend(["stav toriel", "makarich", "robi levkovic", "shahar pivan"])

print(list_of_players)


num_list = list(range(1,8))
print(num_list)

print(num_list[2:6])
print(num_list[:5])
copied_list = num_list[:]
print(copied_list)
copied_list = num_list.copy()
print(copied_list)

# other = insert(where, what)
# remove(what) remove the first occurrence of the element
# deleting some elements
del num_list[3]
print(num_list)


num_list.pop()
print(num_list)

poped_el = num_list.pop()
print(poped_el)
print(num_list)

fruits = ["banana" , "orange", "mango", "apple"]
# sorted() - put in order - create new list
sorted_fruits = sorted(fruits)
print(sorted_fruits)
print(fruits)
# sort() - changing the original list
fruits.sort()
print(fruits)

# index(element) and it returns you the index of the element

list1 = [5, 10, 15, 20, 25, 50, 20]

if list1.index(20):
    index_found = list1.index(20)
    list1.insert(index_found, 200)
    list1.remove(20)
    print(list1)
else:
    print("element not found")











