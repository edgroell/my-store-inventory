"""
Program: my-store-inventory
Author: Ed Groell
Date: 13-JUN-2025
"""

from src.core.features import (
    list_all_products_in_store,
    show_total_amount_in_store,
    make_order
)
from src.products import products
from src.stores import store
from utils.helpers import get_menu_choice

def start(store_selection: store.Store) -> None:
    """ Prints & executes the menu commands flow """
    menu = {
        0: ("0. Exit", None),
        1: ("1. List all products in store", list_all_products_in_store),
        2: ("2. Show total amount in store", show_total_amount_in_store),
        3: ("3. Make an order", make_order)
    }

    while True:
        print("\n   Store Menu")
        print("   ----------")
        for key in sorted(menu.keys()):
            print(menu[key][0])

        menu_choice = get_menu_choice()

        if menu_choice == 0:
            print("\nGoodbye!")
            break

        command = menu.get(menu_choice)
        if command and command[1]:
            command[1](store_selection)


def main():
    """ Initiates the program """
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store("best_buy", product_list)

    start(best_buy)


if __name__ == "__main__":
    main()
