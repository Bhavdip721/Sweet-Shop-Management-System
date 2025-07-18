import unittest
from sweet import Sweet


class TestSweet(unittest.TestCase):
    
    # function for set data 
     def setUp(self):
        """Set up test fixtures before each test method."""
        # Reset the ID counter for consistent testing across runs
        Sweet._next_id = 1
        self.sweet = Sweet("Chocolate Bar", "Dark chocolate", 2.50, 100, "Chocolate")
        self.sweet2 = Sweet("Gummy Bears", "Fruity gummy candy", 1.50, 50, "Gummy")
    
    # test for creation sweet data
    
     def test_sweet_creation(self):
        """Test that a sweet can be created with all required attributes and a unique ID."""
        self.assertEqual(self.sweet.name, "Chocolate Bar")
        self.assertEqual(self.sweet.description, "Dark chocolate")
        self.assertEqual(self.sweet.price, 2.50)
        self.assertEqual(self.sweet.quantity, 100)
        self.assertEqual(self.sweet.category, "Chocolate")
        self.assertEqual(self.sweet.id, 1) # First sweet should have ID 1
        self.assertEqual(self.sweet2.id, 2) # Second sweet should have ID 2

     def test_sweet_creation_with_invalid_price(self):
        """Test that creating a sweet with negative price raises ValueError."""
        with self.assertRaises(ValueError):
            Sweet("Invalid Sweet", "Description", -1.0, 10, "Category")

     def test_sweet_creation_with_invalid_quantity(self):
        """Test that creating a sweet with negative quantity raises ValueError."""
        with self.assertRaises(ValueError):
            Sweet("Invalid Sweet", "Description", 2.0, -5, "Category")

    # test for update or reduce of price or quantity
    
     def test_update_price(self):
        """Test updating sweet price."""
        self.sweet.update_price(3.00)
        self.assertEqual(self.sweet.price, 3.00)

     def test_update_price_invalid(self):
        """Test that updating with invalid price raises ValueError."""
        with self.assertRaises(ValueError):
            self.sweet.update_price(-1.0)

     def test_update_quantity(self):
        """Test updating sweet quantity."""
        self.sweet.update_quantity(150)
        self.assertEqual(self.sweet.quantity, 150)
        
     def test_update_quantity_invalid(self):
        """Test that updating with invalid quantity raises ValueError."""
        with self.assertRaises(ValueError):
            self.sweet.update_quantity(-10)

     def test_reduce_quantity(self):
        """Test reducing sweet quantity."""
        self.sweet.reduce_quantity(20)
        self.assertEqual(self.sweet.quantity, 80)

     def test_reduce_quantity_insufficient(self):
        """Test that reducing quantity beyond available raises ValueError."""
        with self.assertRaises(ValueError):
            self.sweet.reduce_quantity(150)


if __name__ == '__main__':
  
    unittest.main(argv=['first-arg-is-ignored'], exit=False)