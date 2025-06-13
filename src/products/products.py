class Product:

    def __init__(self, name, price, quantity):
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

        return self.name


    def get_quantity(self) -> int:

        return self.quantity


    def set_quantity(self, quantity: int) -> None:
        if quantity < 0:
            raise Exception("Product quantity can't be negative!")

        if not self.active and quantity > 0:
            self.activate()

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:

        return self.active


    def activate(self) -> None:
        self.active = True


    def deactivate(self) -> None:
        self.active = False


    def show(self) -> None:
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity: int) -> float:
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
