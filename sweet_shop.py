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


   #perform upadte and remove in eists and non exist sweet in shop
   
    def remove_sweet(self, name: str) -> Sweet:
        """
        Remove a sweet from the shop.

        Args:
            name (str): Name of the sweet to remove

        Returns:
            Sweet: The removed sweet object

        Raises:
            ValueError: If sweet doesn't exist
        """
        if name not in self.sweets:
            raise ValueError(f"Sweet '{name}' not found in the shop")
        return self.sweets.pop(name)

    def update_sweet(self, name: str, **kwargs):
        """
        Update a sweet's details.

        Args:
            name (str): Name of the sweet to update
            **kwargs: Attributes to update (price, quantity, description, category)

        Raises:
            ValueError: If sweet doesn't exist
        """
        if name not in self.sweets:
            raise ValueError(f"Sweet '{name}' not found in the shop")

        sweet = self.sweets[name]

        if 'price' in kwargs:
            sweet.update_price(kwargs['price'])
        if 'quantity' in kwargs:
            sweet.update_quantity(kwargs['quantity'])
        if 'description' in kwargs:
            sweet.description = kwargs['description']
        if 'category' in kwargs:
            sweet.category = kwargs['category']
            
    # function for get sweet by id,name,categroy
    
    
    def get_sweet(self, name: str) -> Optional[Sweet]:
        """
        Get a sweet by name.

        Args:
            name (str): Name of the sweet

        Returns:
            Sweet or None: Sweet object if found, None otherwise
        """
        return self.sweets.get(name)  
    
    
    
    def get_sweet_by_id(self, sweet_id: int) -> Optional[Sweet]:
        """
        Get a sweet by its unique ID.

        Args:
            sweet_id (int): The unique ID of the sweet.

        Returns:
            Sweet or None: Sweet object if found, None otherwise.
        """
        for sweet in self.sweets.values():
            if sweet.id == sweet_id:
                return sweet
        return None  
        
        
    def get_sweets_by_category(self, category: str) -> List[Sweet]:
        """
        Get all sweets in a specific category.

        Args:
            category (str): Category to filter by

        Returns:
            List[Sweet]: List of sweets in the category
        """
        return [sweet for sweet in self.sweets.values()
                if sweet.category.lower() == category.lower()]
        
        
        # search function  for sweet
        
    def search_sweets(self, query: str) -> List[Sweet]:
        """
        Search for sweets by name, description, or category.

        Args:
            query (str): Search query

        Returns:
            List[Sweet]: List of matching sweets
        """
        query_lower = query.lower()
        results = []

        for sweet in self.sweets.values():
            if (query_lower in sweet.name.lower() or
                query_lower in sweet.description.lower() or
                query_lower in sweet.category.lower()):
                results.append(sweet)

        return results
    
    
    # function for sort sweet by name,id ,price,quantity
    
    def sort_sweets_by_id(self, reverse: bool = False) -> List[Sweet]:
        """
        Get sweets sorted by their ID.
        Args:
            reverse (bool): If True, sort in descending order. Defaults to False (ascending).
        Returns:
            List[Sweet]: Sorted list of sweets.
        """
        return sorted(self.sweets.values(), key=lambda x: x.id, reverse=reverse)

           

    def sort_sweets_by_price(self, reverse: bool = False) -> List[Sweet]:
        """
        Get sweets sorted by price.

        Args:
            reverse (bool): If True, sort in descending order

        Returns:
            List[Sweet]: Sorted list of sweets
        """
        return sorted(self.sweets.values(), key=lambda x: x.price, reverse=reverse)

    def sort_sweets_by_name(self, reverse: bool = False) -> List[Sweet]:
        """
        Get sweets sorted by name.

        Args:
            reverse (bool): If True, sort in descending order

        Returns:
            List[Sweet]: Sorted list of sweets
        """
        return sorted(self.sweets.values(), key=lambda x: x.name.lower(), reverse=reverse)

    def sort_sweets_by_quantity(self, reverse: bool = False) -> List[Sweet]:
        """
        Get sweets sorted by quantity.

        Args:
            reverse (bool): If True, sort in descending order

        Returns:
            List[Sweet]: Sorted list of sweets
        """
        return sorted(self.sweets.values(), key=lambda x: x.quantity, reverse=reverse)