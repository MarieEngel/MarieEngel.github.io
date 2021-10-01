#!/usr/bin/env python3

"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2

# YOUR CODE STARTS HERE

# Get the user name

name_input = input("What is your name?  ")
if name_input != None:
    print(
        f"Hello, {name_input}! \nWhat would you like to do? \n1. List items by warehouse \n2. Search an item and place an order \n3. Quit"
    )
    operation_input = int(input("Please type the number of the operation: "))

if operation_input == 1:
    print(f"Items in warehouse1:\n{warehouse1}")
    print(f"Items in warehouse2:\n{warehouse2}")
    print(f"Thanks for your visit, {name_input}!")

elif operation_input == 2:
    item_input = input("What is the name of the item?  ")

    available_wh1 = 0
    available_wh2 = 0

    for item in warehouse1:
        if item == item_input:
            available_wh1 += 1

    for item in warehouse2:
        if item == item_input:
            available_wh2 += 1

    available = available_wh1 + available_wh2

    if available > 0:
        print(f"Amount available: {available}")
        if available_wh1 > 0 and available_wh2 > 0:
            print("Location: Both warehouses")
            if available_wh1 > available_wh2:
                print(
                    f"Maximum availability: {max(available_wh1, available_wh2)} in Warehouse1"
                )
            elif available_wh1 < available_wh2:
                print(
                    f"Maximum availability: {max(available_wh1, available_wh2)} in Warehouse2"
                )
            else:
                print(f"Both warehouses have the same amount of {item_input} in stock.")

        elif available_wh1 > 0:
            print("Location: Warehouse1")
        else:
            print("Location: Warehouse2")
    else:
        print("Sorry, not in stock.")

    order_decision = input(
        "Would you like to place an order?Please enter y for yes and n for no: "
    )
    if order_decision == "n":
        print(f"Thanks for your visit, {name_input}")


# print(len(warehouse1))
# print(warehouse1[-1])
# print(len(warehouse2))
# print(warehouse1[0])
# print(warehouse1[0])
# print(type(warehouse1[0]))

# Greet the user

# Show the menu and ask to pick a choice

# If they pick 1
#
# Else, if they pick 2
#
# Else, if they pick 3
#
# Else

# Thank the user for the visit
