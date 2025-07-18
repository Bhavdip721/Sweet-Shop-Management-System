# for implement function for test in test_sweet

class Sweet:
    """Represents a sweet item in the shop."""

    _next_id = 1  # Class-level counter for unique IDs

    def __init__(self, name, description, price, quantity, category):
        """
        Initialize a Sweet object.

        Args:
            name (str): Name of the sweet
            description (str): Description of the sweet
            price (float): Price per unit
            quantity (int): Available quantity
            category (str): Category of the sweet

        Raises:
            ValueError: If price is negative or quantity is negative
        """
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.id = Sweet._next_id  # Assign unique ID
        Sweet._next_id += 1       # Increment for the next sweet

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.category = category
        
        # function for update or reduce of price and quantity vaild
    def update_price(self, new_price):
        """
        Update the price of the sweet.

        Args:
            new_price (float): New price for the sweet

        Raises:
            ValueError: If new_price is negative
        """
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.price = new_price

    def update_quantity(self, new_quantity):
        """
        Update the quantity of the sweet.

        Args:
            new_quantity (int): New quantity for the sweet

        Raises:
            ValueError: If new_quantity is negative
        """
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = new_quantity

    def reduce_quantity(self, amount):
        """
        Reduce the quantity of the sweet.

        Args:
            amount (int): Amount to reduce

        Raises:
            ValueError: If amount exceeds available quantity
        """
        if amount > self.quantity:
            raise ValueError("Cannot reduce quantity beyond available stock")
        self.quantity -= amount
        
        
        # function for cheaking sweet available 
    def is_available(self):
        """
        Check if the sweet is available (quantity > 0).

        Returns:
            bool: True if available, False otherwise
        """
        return self.quantity > 0