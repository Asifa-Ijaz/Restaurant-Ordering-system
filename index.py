menu = {
    'Pizza' : 500,
    'Pasta' : 300,
    'Zinger burger' : 400,
    'Salad' : 80,
}

print("welcome to Restaurant")
print(menu)

order_total = 0

item_1 = input("Enter the item you want to order :")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} not available yet!!")

another_order =input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter another item you want to order :")
    if item_2 in menu:
     order_total += menu[item_2]
     print(f"Ordered Item {item_2} has been added to order")
    else:
     print("ordered item is not available!!")

print(f"The total amount of items is {order_total}")
print("Thank you for ordering!")