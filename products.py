class Product:
    """Represents a product with a name, price, quantity, and active status."""

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a new product instance.

        Args:
            name (str): The name of the product.
            price (float): The price per unit (must be non-negative).
            quantity (int): The initial stock quantity (must be non-negative).

        Raises:
            Exception: If the name is empty or if price/quantity are negative.
        """
        if not name or price < 0 or quantity < 0:
            raise Exception(
                "Invalid input: name must not be empty, and price and quantity "
                "must be non-negative."
            )

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Return the current quantity of the product.

        Returns:
            int: The current quantity in stock.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Set a new quantity for the product.

        If the quantity is set to zero, the product is automatically deactivated.

        Args:
            quantity (int): The new quantity (must be non-negative).

        Raises:
            Exception: If the provided quantity is negative.
        """
        if quantity < 0:
            raise Exception("Quantity cannot be negative.")

        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Check whether the product is active.

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """Activate the product, making it available for sale."""
        self.active = True

    def deactivate(self):
        """Deactivate the product, making it unavailable for sale."""
        self.active = False

    def show(self):
        """Print the product's details in a readable format."""
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def buy(self, desired_quantity: int) -> float:
        """
        Purchase a given quantity of the product.

        Reduces the available stock using the setter method to ensure that
        the product is deactivated automatically when the stock reaches zero.

        Args:
            desired_quantity (int): The amount to purchase (must be positive).

        Returns:
            float: The total price for the purchase.

        Raises:
            Exception: If the product is inactive, the quantity is invalid,
                       or there is not enough stock.
        """
        if not self.active:
            raise Exception("Product is not active.")
        if desired_quantity <= 0:
            raise Exception("Quantity must be greater than 0.")

        current_qty = self.get_quantity()
        if desired_quantity > current_qty:
            raise Exception("Not enough quantity in stock.")

        self.set_quantity(current_qty - desired_quantity)
        return float(self.price) * desired_quantity