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
# Greet the user
# Show the menu and ask to pick a choice

name_input = input("What is your user name?  ")
if name_input != None:
    print(
        f"Hello, {name_input}! \nWhat would you like to do? \n1. List items by warehouse \n2. Search an item and place an order \n3. Quit"
    )

    # operation_input = None
    # while operation_input != 3:
operation_input = int(input("Please type the number of the operation: "))

# If they pick 1
# bullet list
if operation_input == 1:
    print("Items in Warehouse 1:")
    for item in warehouse1:
        print(f"- {item}")
    print()
    print("Items in Warehouse 2:")
    for item in warehouse2:
        print(f"- {item}")

# Else, if they pick 2
elif operation_input == 2:
    item_input = input("What is the name of the item?  ")

    available_wh1 = 0
    available_wh2 = 0

    # count items in warehouse1:
    for item in warehouse1:
        if item == item_input:
            available_wh1 += 1

    # count items in warehouse2:
    for item in warehouse2:
        if item == item_input:
            available_wh2 += 1

    # sum of available items
    available = available_wh1 + available_wh2

    # give the location of the item or "Not in stock"
    if available > 0:  # both warehouses
        print(f"Amount available: {available}")
        if available_wh1 > 0 and available_wh2 > 0:
            print("Location: Both warehouses")
            if available_wh1 > available_wh2:  # maximum
                print(
                    f"Maximum availability: {max(available_wh1, available_wh2)} in Warehouse1"
                )
            elif available_wh1 < available_wh2:
                print(
                    f"Maximum availability: {max(available_wh1, available_wh2)} in Warehouse2"
                )
            else:
                print(f"Both warehouses have the same amount of {item_input} in stock.")

        elif available_wh1 > 0:  # warehouse1 or warehouse#
            print("Location: Warehouse1")
        else:
            print("Location: Warehouse2")

        # order decision:
        order_decision = input("Would you like to place an order? (y/n): ")

        if order_decision == "y":
            order_amount = int(
                input(f"How many {item_input} would you like to order?  ")
            )
            if order_amount > available:
                order_amount_correction = input(
                    f"Sorry, your order is exceeding our stock. Would you like to order {available} {item_input} (y/n)? "
                )
                if order_amount_correction == "y":
                    print(f"Your order has been placed: {available} {item_input}")
            else:
                print(f"Your order has been placed: {order_amount} {item_input}")
    else:
        print("Sorry, not in stock.")

# Else, if they pick 3
elif operation_input == 3:
    pass  # to avoid having  "Thanks for your visit" displayed twice
else:
    print("Sorry, the operation entered is not valid.")
    # break

    # Thank the user for the visit
print()
print(f"Thanks for your visit, {name_input}!")


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
