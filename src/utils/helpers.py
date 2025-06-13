def get_menu_choice():
    while True:
        try:
            menu_choice = int(input("\nEnter command (0-3): ").strip())
            if 0 <= menu_choice <= 3:

                return menu_choice

            print("Please enter a number between 0 and 3!")

        except ValueError:
            print("Please enter a valid number (0-3)!")


def get_product_selection(store_selection):
    while True:
        product_selection = input("Which product # do you want? ").strip()
        if product_selection == "":
            return None

        try:
            product_selection_index = int(product_selection)
            range_products = len(store_selection.get_all_products())
            if 1 <= product_selection_index <= range_products:
                product_to_add = store_selection.get_all_products()[product_selection_index - 1]
                return product_to_add

            print("This is not a valid selection!")

        except ValueError:
            print("Please enter a valid number!")


def get_product_quantity(product_selection):
    while True:
        try:
            product_quantity = int(input(f"What amount of {product_selection} do you want? ").strip())
            if product_quantity <= 0:
                print("Please enter a positive number!")

            elif product_quantity > product_selection.get_quantity():
                print("Quantity requested exceeds inventory!")

            else:
                return product_quantity

        except ValueError:
            print("Please enter a valid number!")


def get_order_selection(store_selection):
    print("\nWhen you're done with your order, enter empty text.")
    order_selection = []

    while True:
        product_selection = get_product_selection(store_selection)
        if product_selection is None:

            break

        product_quantity = get_product_quantity(product_selection)
        if product_quantity is not None:
            order_selection.append((product_selection, product_quantity))
            print(f"\n>>> Added {product_selection} x {product_quantity}\n")
        else:
            print("Invalid quantity, please try adding the product again!")

    return order_selection


__all__ = [
    "get_menu_choice",
    "get_product_selection",
    "get_product_quantity",
    "get_order_selection"
]
