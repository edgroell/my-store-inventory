"""
Module containing all menu commands.
"""

from src.stores import store
from src.utils.helpers import get_order_selection

def list_all_products_in_store(store_selection: store.Store) -> None:
    """ Prints all products available in the store """
    print("\n" + "-" * 60)
    for i, product_item in enumerate(store_selection.get_all_products()):
        print(f"{i+1}. ", end="")
        f"{product_item.show()}"
    print("-" * 60)


def show_total_amount_in_store(store_selection: store.Store) -> None:
    """ Prints the total quantity of all items in the store's inventory """
    store_total = store_selection.get_total_quantity()
    print("\n" + "-" * 60)
    print(f"Total of {store_total} items in {store_selection} inventory")
    print("-" * 60)


def make_order(store_selection: store.Store) -> None:
    """ Coordinates the purchase process """
    list_all_products_in_store(store_selection)
    shopping_list = get_order_selection(store_selection)
    print()
    total_cost = store_selection.order(shopping_list)
    print("\n" + "-" * 60)
    print(f">>> Order processed for a total amount of ${total_cost}")
    print("-" * 60)


__all__ = [
    "list_all_products_in_store",
    "show_total_amount_in_store",
    "make_order"
]
