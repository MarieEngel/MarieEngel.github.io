#!/usr/bin/env python3

from _typeshed import WriteableBuffer
from data import stock
from datetime import datetime

name_input = ""


def get_user_name():
    """Gets the users name."""
    global name_input
    if not name_input:
        name_input = input("What is your user name?  ")
    return name_input


def greet_user():
    """Greets the user by name & displays the options to select from."""
    print(
        f"Hello, {get_user_name()}! \nWhat would you like to do? \n1. List items by warehouse \n2. Search an item and place an order \n3. Browse by Category \n4. Quit"
    )


def stock_of_warehouses(stock: list):
    """Prints the list of items and their total amount sorted by warehouse."""
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


def list_available_by_warehouse(stock: list, item_input: str, warehouse_num: int):
    return list(
        filter(
            lambda item: item_input.lower()
            == f"{item['state']} {item['category']}".lower()
            and item["warehouse"] == warehouse_num,
            stock,
        )
    )


def search(stock: list, item_input: str):
    """Prints the total availability, days in stock, warehouse with max availability.
    Returns the total availability."""
    available_w1 = list_available_by_warehouse(stock, item_input, 1)
    available_w2 = list_available_by_warehouse(stock, item_input, 2)

    result = {
        "Warehouse 1": available_w1,
        "Warehouse 2": available_w2,
        "Sum": len(available_w1) + len(available_w2),
    }

    return result


def print_search_results(search_results: dict):
    if search_results["Sum"] > 0:

        print(f"Amount available: {search_results['Sum']}")
        print("Location:")
        current_date = datetime.today().date()
        for item in search_results["Warehouse 1"] + search_results["Warehouse 2"]:
            days = (
                current_date
                - datetime.strptime(item["date_of_stock"], "%Y-%m-%d %H:%M:%S").date()
            ).days
            print(f"- Warehouse {item['warehouse']} (in stock for {days} days)")

        if (
            len(search_results["Warehouse 1"]) > 0
            and len(search_results["Warehouse 2"]) > 0
        ):
            if len(search_results["Warehouse 1"]) > len(search_results["Warehouse 2"]):
                print(
                    f"Maximum availability: {len(search_results['Warehouse 1'])} in Warehouse1"
                )
            else:
                print(
                    f"Maximum availability: {len(search_results['Warehouse 2'])} in Warehouse2"
                )
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
    # name_input = input("What is your user name?  ")
    # if name_input != None:
    #     print(
    #         f"Hello, {name_input}! \nWhat would you like to do? \n1. List items by warehouse \n2. Search an item and place an order \n3. Browse by Category \n4. Quit"
    # )
    get_user_name()

    greet_user()

    operation_input = None
    while operation_input != 4:
        operation_input = int(input("Please type the number of the operation: "))

        if operation_input == 1:
            stock_of_warehouses(stock)

        elif operation_input == 2:
            item_input = input("What is the name of the item?  ")
            search_results = search(stock, item_input)
            print_search_results(search_results)

            if search_results["Sum"] > 0:
                order_decision = input("Would you like to place an order? (y/n): ")

                if order_decision == "y":
                    order(item_input, search_results["Sum"])

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
