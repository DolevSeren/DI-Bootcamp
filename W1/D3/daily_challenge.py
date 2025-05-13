# EX_1

user_input = input("please enter a word")
list(user_input)

new_dict = {value: index for index, value in enumerate(user_input)}
print(new_dict)


# ex_2


items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet = "$100"


wallet_clean = wallet.replace("$", "")
wallet_amount = int(wallet_clean)

affordable_items = []

for item, price in items_purchase.items():
    clean_price = price.replace("$", "")
    clean_price2 = clean_price.replace(",", "")
    price_value = int(clean_price2)

    if price_value <= wallet_amount:
        affordable_items.append(item)

if not affordable_items:
        print("Nothing")
else:
    affordable_items.sort()
    print(affordable_items)







