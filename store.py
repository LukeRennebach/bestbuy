class Store:
    """Represents a store managing a collection of products."""

    def __init__(self, products):
        self._products = products

    def add_product(self, product):
        """Add a product to the store."""
        self._products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        self._products.remove(product)

    def get_total_quantity(self):
        """Return the total quantity of all products."""
        return sum(product.quantity for product in self._products)

    def get_all_products(self):
        """Return a list of all active products."""
        return [product for product in self._products if product.is_active()]

    def order(self, shopping_list):
        """Process an order and return the total price."""
        total = 0
        for product, amount in shopping_list:
            total += product.buy(amount)
        return total