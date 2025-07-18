import unittest



class TestSweet(unittest.TestCase):
    
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




if __name__ == '__main__':
  
    unittest.main(argv=['first-arg-is-ignored'], exit=False)