"""
Module containing the Product class and its properties.
"""

class Product:
    """ Defines all properties of a product instance """

    def __init__(self, name: str, price: float, quantity: int):
        """ Constructor that initializes a product instance """
        if not name:
            raise Exception("Product name is required!")

        self.name = name

        if price <= 0:
            raise Exception("Product price can't be negative or zero!")

        self.price = price

        if quantity <= 0:
            raise Exception("Product quantity can't be negative or zero!")

        self.quantity = quantity

        self.active = True


    def __str__(self):
        """ Method that returns a string representation of the product """

        return self.name


    def get_quantity(self) -> int:
        """ Returns the inventory's quantity of the product """

        return self.quantity


    def set_quantity(self, quantity: int) -> None:
        """ Sets the inventory's quantity of the product """
        if quantity < 0:
            raise Exception("Product quantity can't be negative!")

        if not self.active and quantity > 0:
            self.activate()

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:
        """ Returns True if the product is active """

        return self.active


    def activate(self) -> None:
        """ Set the product to active """
        self.active = True


    def deactivate(self) -> None:
        """ Set the product to inactive """
        self.active = False


    def show(self) -> None:
        """ Prints the product properties (name, price, quantity) """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity: int) -> float:
        """
        Executes the purchase of the product
        based on given quantity versus available quantity
        """
        if not self.is_active():
            raise Exception("Product is not active!")

        if self.quantity < 1:
            raise Exception("Product is out of stock!")

        if quantity < 1:
            raise Exception("Purchase quantity must be at least 1!")

        if quantity > self.quantity:
            raise Exception(f"Insufficient stock - Currently only {self.quantity} in stock!")

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return round(quantity * self.price, 2)
