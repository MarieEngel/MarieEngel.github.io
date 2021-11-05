#!/usr/bin/env python3

"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import stock
from datetime import datetime

## defining functions


def stock_of_warehouses():
    result_w1 = []
    result_w2 = []
    for item in stock:
        if item["warehouse"] == 1:
            result_w1.append(item)
        if item["warehouse"] == 2:
            result_w2.append(item)
    print("Warehouse 1: ")
    for item in result_w1:
        print(f"- {item['state']} {item['category']}")
    print()
    print("Warehouse 2: ")
    for item in result_w2:
        print(f"- {item['state']} {item['category']}")

    # total amount of items in stock on each warehouse:

    print(f"Total amount of items in Warehouse 1: {len(result_w1)}")
    print(f"Total amount of items in Warehouse 2: {len(result_w2)}")


# - Zweite function

# if op = 1:
#     erste function
# if op = 2:
#     erste function

# def greeting():
name_input = input("What is your user name?  ")
if name_input != None:
    print(
        f"Hello, {name_input}! \nWhat would you like to do? \n1. List items by warehouse \n2. Search an item and place an order \n3. Browse by Category \n4. Quit"
    )
# while loop to come back to operation selection after operation 1 or 2
operation_input = None  #  condition variable needs to be defined before the loop
while operation_input != 4:
    operation_input = int(input("Please type the number of the operation: "))

    # If they pick 1

    if operation_input == 1:
        stock_of_warehouses()

    # # Else, if they pick 2
    ### Make case insensitive:
    ### def search
    ### def make case insensitive <-- decorator
    elif operation_input == 2:
        item_input = input("What is the name of the item?  ")
        available_w1 = []
        available_w2 = []
        for item in stock:
            if item_input.lower() == f"{item['state']} {item['category']}".lower():
                if item["warehouse"] == 1:
                    available_w1.append(item)
                if item["warehouse"] == 2:
                    available_w2.append(item)

        sum_w1 = len(available_w1)
        sum_w2 = len(available_w2)
        sum_available = sum_w1 + sum_w2

        if sum_available > 0:  # both warehouses
            print(f"Amount available: {sum_available}")
            print("Location:")
            current_date = datetime.today().date()
            for item in available_w1 + available_w2:
                days = (
                    current_date
                    - datetime.strptime(
                        item["date_of_stock"], "%Y-%m-%d %H:%M:%S"
                    ).date()
                ).days
                print(f"- Warehouse {item['warehouse']} (in stock for {days} days)")

            if sum_w1 > 0 and sum_w2 > 0:
                if sum_w1 > sum_w2:  # maximum
                    print(f"Maximum availability: {sum_w1} in Warehouse1")
                else:
                    print(f"Maximum availability: {sum_w2} in Warehouse2")

            print()
            # ## def order
            # order decision:
            order_decision = input("Would you like to place an order? (y/n): ")

            if order_decision == "y":
                order_amount = int(
                    input(f"How many '{item_input}' would you like to order?  ")
                )
                if order_amount > sum_available:
                    order_amount_correction = input(
                        f"Sorry, your order is exceeding our stock. Would you like to order {sum_available} '{item_input}' (y/n)? "
                    )
                    if order_amount_correction == "y":
                        print(
                            f"Your order has been placed: {sum_available} '{item_input}'"
                        )
                else:
                    print(f"Your order has been placed: {order_amount} '{item_input}'")
        else:
            print("Location: Not in stock")
    ## browse by category
    # Else if they pick 3: browse by category
    elif operation_input == 3:
        categories = {}
        for item in stock:
            key = item["category"]
            if key not in categories:
                categories[key] = 1
            else:
                categories[key] += 1

        categories_list = []
        for pair in categories.items():
            categories_list.append(pair)

        for (i, category) in enumerate(categories_list, start=1):
            print(f"{i}. {category[0]} ({category[1]})")

        choice_input = int(input("Type the number of the category to browse: "))

        chosen_category = categories_list[(choice_input - 1)]
        print(f"List of '{chosen_category[0]}' available: ")

        for item in stock:
            if item["category"] == chosen_category[0]:
                print(
                    f"{item['state']} {item['category']}, Warehouse {item['warehouse']}"
                )
    # def  goodbye
    # Else, if they pick 4
    elif operation_input == 4:
        pass  # to avoid having  "Thanks for your visit" displayed twice
    else:
        print("Sorry, the operation entered is not valid.")
        break  #  to get out of the loop

# Thank the user for the visit
print()
print(f"Thanks for your visit, {name_input}!")
