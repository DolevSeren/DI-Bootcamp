# EX_1

# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount
#
#     def __str__(self):
#         return f"{self.amount} {self.currency}s"
#
#     def __int__(self):
#         return self.amount
#
#     def __repr__(self):
#         return f'{self.amount} {self.currency}'
#
#     def __add__(self, other):
#         if isinstance(other, int):
#             return Currency(self.currency, self.amount + other)
#         elif isinstance(other, Currency):
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#             return Currency(self.currency, self.amount + other.amount)
#         else:
#             raise TypeError("Unsupported type for addition")
#
#     def __iadd__(self, other):
#         if isinstance(other, Currency):
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add {self.currency} to {other.currency}")
#             self.amount += other.amount
#         elif isinstance(other, int):
#             self.amount += other
#         else:
#             raise TypeError("Cannot add between Currency type <dollar> and <shekel>")
#         return self
#
#
#
#
# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)
#
# #the comment is the expected output
# str(c1)
# # '5 dollars'
#
# int(c1)
# # 5
#
# repr(c1)
# # '5 dollars'
#
# print(c1 + 5)
# # # 10
#
# print(c1 + c2)
# # 15
#
# print(c1)
# # 5 dollars
#
# c1 += 5
# print(c1)
# # # 10 dollars
#
# c1 += c2
# print(c1)
# # 20 dollars
#
# print(c1 + c3)
# # TypeError: Cannot add between Currency type <dollar> and <shekel>


import string
import random

letters = string.ascii_lowercase + string.ascii_uppercase
new_word = ""
while len(new_word) < 5:
    new_word += (random.choice(letters))
print(new_word)


from datetime import date

def today_date():
    today = date.today()
    print("Today's date:", today)

today_date()

from datetime import datetime

def time_until_january_first():
    now = datetime.now()
    next_year = now.year + 1
    jan_first = datetime(year=next_year, month=1, day=1)
    time_left = jan_first - now
    print("Time left until January 1st:", time_left)

time_until_january_first()

from datetime import datetime

def minutes_lived(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    now = datetime.now()
    difference = now - birthdate
    minutes = difference.total_seconds() / 60
    print(f"You have lived approximately {int(minutes)} minutes.")


minutes_lived("1996-11-26")







