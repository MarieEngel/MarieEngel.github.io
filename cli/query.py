#!/usr/bin/env python3

"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import stock
from datetime import datetime


def stock_of_warehouses(stock):
    result_w1 = list(filter(lambda item: item["warehouse"] == 1, stock))
    result_w2 = list(filter(lambda item: item["warehouse"] == 2, stock))
    print("Warehouse 1: ")
    for item in result_w1:
        print(f"- {item['state']} {item['category']}")
    print()
    print("Warehouse 2: ")
    for item in result_w2:
        print(f"- {item['state']} {item['category']}")

    print(f"Total amount of items in Warehouse 1: {len(result_w1)}")
    print(f"Total amount of items in Warehouse 2: {len(result_w2)}")


def search(stock, item_input):
    available_w1 = list(
        filter(
            lambda item: item_input.lower()
            == f"{item['state']} {item['category']}".lower()
            and item["warehouse"] == 1,
            stock,
        )
    )
    available_w2 = list(
        filter(
            lambda item: item_input.lower()
            == f"{item['state']} {item['category']}".lower()
            and item["warehouse"] == 2,
            stock,
        )
    )

    sum_w1 = len(available_w1)
    sum_w2 = len(available_w2)
    sum_available = sum_w1 + sum_w2

    if sum_available > 0:
        print(f"Amount available: {sum_available}")
        print("Location:")
        current_date = datetime.today().date()
        for item in available_w1 + available_w2:
            days = (
                current_date
                - datetime.strptime(item["date_of_stock"], "%Y-%m-%d %H:%M:%S").date()
            ).days
            print(f"- Warehouse {item['warehouse']} (in stock for {days} days)")

        if sum_w1 > 0 and sum_w2 > 0:
            if sum_w1 > sum_w2:
                print(f"Maximum availability: {sum_w1} in Warehouse1")
            else:
                print(f"Maximum availability: {sum_w2} in Warehouse2")

        else:
            print("Location: Not in stock")
    return sum_available


def order(item_input, sum_available):
    order_amount = int(input(f"How many '{item_input}' would you like to order?  "))
    if order_amount > sum_available:
        order_amount_correction = input(
            f"Sorry, your order is exceeding our stock. Would you like to order {sum_available} '{item_input}' (y/n)? "
        )
        if order_amount_correction == "y":
            print(f"Your order has been placed: {sum_available} '{item_input}'")
    else:
        print(f"Your order has been placed: {order_amount} '{item_input}'")


def browse_categories(stock):
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
            print(f"{item['state']} {item['category']}, Warehouse {item['warehouse']}")


def main():
    name_input = input("What is your user name?  ")
    if name_input != None:
        print(
            f"Hello, {name_input}! \nWhat would you like to do? \n1. List items by warehouse \n2. Search an item and place an order \n3. Browse by Category \n4. Quit"
        )

    operation_input = None
    while operation_input != 4:
        operation_input = int(input("Please type the number of the operation: "))

        if operation_input == 1:
            stock_of_warehouses(stock)

        elif operation_input == 2:
            item_input = input("What is the name of the item?  ")
            sum_available = search(stock, item_input)

            order_decision = input("Would you like to place an order? (y/n): ")

            if order_decision == "y":
                order(item_input, sum_available)

        elif operation_input == 3:
            browse_categories(stock)

        elif operation_input == 4:
            pass
        else:
            print("Sorry, the operation entered is not valid.")
            break

    print()
    print(f"Thanks for your visit, {name_input}!")


if __name__ == "__main__":
    main()
