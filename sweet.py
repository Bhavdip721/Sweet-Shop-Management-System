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