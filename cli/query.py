#!/usr/bin/env python3

from typing import Callable
from data import stock
from datetime import datetime


def get_user_name():
    """Gets the users name."""
    return input("What is your user name?  ")


def greet_user(name: str):
    """Greets the user by name & displays the options to select from."""
    print(
        f"Hello, {name}! \nWhat would you like to do? \n1. List items by warehouse \n2. Search an item and place an order \n3. Browse by Category \n4. Quit"
    )


def search(stock: list, predicate: Callable[[dict], bool]):
    """Filters the items by warehouse and saves them in a dict [warehouse, list of items]."""
    result: dict[int, list] = {}

    for item in stock:
        if predicate(item):
            warehouse = item["warehouse"]
            if warehouse not in result:
                result[warehouse] = [item]
            else:
                result[warehouse].append(item)

    return result


def list_items_by_warehouse(warehouses: dict[int, list]):
    """Prints the list of items by warehouse and the total amount of items by warehouse."""
    for warehouse, items in warehouses.items():
        print(f"Warehouse {warehouse}: ")
        for item in items:
            print(f"- {item['state']} {item['category']}")

    for warehouse, items in warehouses.items():
        print(f"Total amount of items in Warehouse {warehouse}: {len(items)}")


def print_search_results(warehouses: dict[int, list], amount: int):
    """For the searched item prints for each item, in which warehouse and for how many days it has been stored."""
    if amount > 0:
        print(f"Amount available: {amount}")
        print("Location:")
        current_date = datetime.today().date()
        for items in warehouses.values():
            for item in items:
                days = (
                    current_date
                    - datetime.strptime(
                        item["date_of_stock"], "%Y-%m-%d %H:%M:%S"
                    ).date()
                ).days
                print(f"- Warehouse {item['warehouse']} (in stock for {days} days)")

        max_availability = 0
        max_warehouse = 0
        for warehouse, items in warehouses.items():
            if len(items) > max_availability:
                max_availability = len(items)
                max_warehouse = warehouse

        print(f"Maximum availability: {max_availability} in Warehouse {max_warehouse}")
    else:
        print("Location: Not in stock")


def order(item_input: str, sum_available: int):
    """Asks for the amount to order, compares with availability and prints the placed order."""
    order_amount = int(input(f"How many '{item_input}' would you like to order?  "))
    if order_amount > sum_available:
        order_amount_correction = input(
            f"Sorry, your order is exceeding our stock. Would you like to order {sum_available} '{item_input}' (y/n)? "
        )
        if order_amount_correction == "y":
            print(f"Your order has been placed: {sum_available} '{item_input}'")
    else:
        print(f"Your order has been placed: {order_amount} '{item_input}'")


def browse_categories(stock: list):
    """Prints the list of categories with id. Asks the category id to browse and prints the list items with location."""
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
    """Entry point to the program."""
    username = get_user_name()
    greet_user(username)

    operation_input = None
    while operation_input != 4:
        operation_input = int(input("Please type the number of the operation: "))

        if operation_input == 1:
            warehouses = search(stock, lambda i: True)
            list_items_by_warehouse(warehouses)

        elif operation_input == 2:
            item_input = input("What is the name of the item?  ")
            warehouses = search(
                stock,
                lambda i: f"{i['state']} {i['category']}".lower() == item_input.lower(),
            )

            amount = 0
            for items in warehouses.values():
                amount += len(items)
            print_search_results(warehouses, amount)

            if amount > 0:
                order_decision = input("Would you like to place an order? (y/n): ")

                if order_decision == "y":
                    order(item_input, amount)

        elif operation_input == 3:
            browse_categories(stock)

        elif operation_input == 4:
            pass
        else:
            print("Sorry, the operation entered is not valid.")
            break

    print()
    print(f"Thanks for your visit, {username}!")


if __name__ == "__main__":
    main()
