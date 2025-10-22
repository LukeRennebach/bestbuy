class Product:
    """Represents a product with name, price, quantity, and active status."""

    def __init__(self, name, price, quantity):
        """Initialize a product with name, price, and quantity."""
        if not name or price < 0 or quantity < 0:
            raise Exception(
                "Invalid input: name must not be empty, price and quantity must be non-negative."
            )
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the product quantity, deactivating if it reaches zero."""
        if quantity < 0:
            raise Exception("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return True if the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Print product details."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """Buy a quantity of the product, reducing stock and returning total price."""
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise Exception("Quantity must be greater than 0.")
        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price
