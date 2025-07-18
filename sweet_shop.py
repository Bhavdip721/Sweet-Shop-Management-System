from sweet import Sweet
from typing import List, Optional

class SweetShop:
    """Manages a collection of sweets in a sweet shop."""

    def __init__(self, name):
        """
        Initialize a SweetShop.

        Args:
            name (str): Name of the sweet shop
        """
        self.name = name
        self.sweets = {}  # Dictionary to store sweets by name
    
    # add sweet in shop
    def add_sweet(self, sweet: Sweet):
        """
        Add a sweet to the shop.

        Args:
            sweet (Sweet): Sweet object to add

        Raises:
            ValueError: If sweet with same name already exists
        """
        if sweet.name in self.sweets:
            raise ValueError(f"Sweet '{sweet.name}' already exists in the shop")
        self.sweets[sweet.name] = sweet
