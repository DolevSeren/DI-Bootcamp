# EX_1

user_word = input("please enter a word")

out_dict = {}
for i, char in enumerate(user_word):
    if char in out_dict:
        out_dict[char].append(i)
    else:
        out_dict.update({char : [i]})

print(out_dict)

# ex_2


items_purchase = {"Apple": "$4",
                  "Honey": "$3",
                  "Fan": "$14",
                  "Bananas": "$4",
                  "Pan": "$100",
                  "Spoon": "$2"}
wallet = "$100"


wallet_clean = wallet.replace("$", "").replace(",", "")
wallet_amount = int(wallet_clean)

affordable_items = []

for item, price in items_purchase.items():
    clean_price = int(price.replace("$", "").replace(",", ""))


    if clean_price < wallet_amount:
        affordable_items.append(item)

if not affordable_items:
        print("Nothing")
else:
    affordable_items.sort()
    print(affordable_items)







