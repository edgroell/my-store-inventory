from src import products


class Store:

    def __init__(self, name, products_list=None):
        self.name = name
        self.products_list = list(products_list) if products_list is not None else []


    def __str__(self):

        return self.name


    def add_product(self, product):
        for existing_product in self.products_list:
            if existing_product.name == product.name:
                raise Exception(f"Product name '{product}' already exists - Not adding!")

        self.products_list.append(product)
        print(f"Product '{product}' added to the store '{self.name}'")


    def remove_product(self, product):
        try:
            self.products_list.remove(product)
            print(f"Product '{product}' removed from the store '{self.name}'")
        except ValueError as e:
            print(f"Product '{product}' not found in '{self.name}': {e}")


    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products_list:
            total_quantity += product.get_quantity()

        return total_quantity


    def get_all_products(self) -> list:
        all_active_products = []
        for product in self.products_list:
            if product.is_active():
                all_active_products.append(product)

        return all_active_products


    def order(self, shopping_list: list) -> float:
        total_cost = 0
        for product, quantity in shopping_list:
            if not isinstance(product, products.Product):
                print(f"Invalid product: {product}")
                continue

            if not isinstance(quantity, int) or quantity <= 0:
                print(f"Invalid quantity for '{product}'")
                continue

            store_product = None
            for p in self.products_list:
                if p.name == product.name:
                    store_product = p
                    break

            if store_product:
                try:
                    item_cost = store_product.buy(quantity)
                    total_cost += item_cost
                    print(f"Processed '{product}' x {quantity}")
                except Exception as e:
                    print(f"Failed to buy '{product}' x {quantity}: {e}")

            else:
                print(f"Product '{product}' not found in store inventory - Skipping!")

        return round(total_cost, 2)
