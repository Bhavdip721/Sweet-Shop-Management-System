import unittest
from sweet_shop import SweetShop
from sweet import Sweet

class TestSweetShop(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures before each test method."""
        # Reset Sweet ID counter for consistent testing across runs
        Sweet._next_id = 1
        self.shop = SweetShop("Sweet Dreams")
        self.chocolate = Sweet("Chocolate Bar", "Dark chocolate", 2.50, 100, "Chocolate")
        self.gummy = Sweet("Gummy Bears", "Fruity gummy bears", 1.50, 50, "Gummy")
        self.lollipop = Sweet("Rainbow Lollipop", "Colorful lollipop", 1.00, 75, "Hard Candy")
        self.shop.add_sweet(self.chocolate)
        self.shop.add_sweet(self.gummy)
        self.shop.add_sweet(self.lollipop)

    def test_shop_creation(self):
        """Test that a sweet shop can be created."""
        self.assertEqual(self.shop.name, "Sweet Dreams")
        self.assertEqual(len(self.shop.sweets), 3) # Now 3 sweets are added in setUp
    
    
    # test for add vaild sweet in shop
    def test_add_sweet(self):
        """Test adding a sweet to the shop."""
        new_sweet = Sweet("Jelly Beans", "Assorted flavors", 3.00, 70, "Jelly")
        self.shop.add_sweet(new_sweet)
        self.assertEqual(len(self.shop.sweets), 4)
        self.assertIn("Jelly Beans", self.shop.sweets)

    def test_add_duplicate_sweet(self):
        """Test that adding a duplicate sweet raises ValueError."""
        with self.assertRaises(ValueError):
            self.shop.add_sweet(Sweet("Chocolate Bar", "Another chocolate", 2.00, 10, "Chocolate"))
            
            
            
     # test for upadte or reduce sweet property like price or quantity is availble in shop 
     
    def test_remove_sweet(self):
        """Test removing a sweet from the shop."""
        removed = self.shop.remove_sweet("Chocolate Bar")
        self.assertEqual(len(self.shop.sweets), 2)
        self.assertEqual(removed.name, "Chocolate Bar")
        self.assertNotIn("Chocolate Bar", self.shop.sweets)

    def test_remove_nonexistent_sweet(self):
        """Test that removing a non-existent sweet raises ValueError."""
        with self.assertRaises(ValueError):
            self.shop.remove_sweet("Non-existent Sweet")

    def test_update_sweet(self):
        """Test updating a sweet's details."""
        self.shop.update_sweet("Chocolate Bar", price=3.00, quantity=120)
        updated_sweet = self.shop.get_sweet("Chocolate Bar")
        self.assertEqual(updated_sweet.price, 3.00)
        self.assertEqual(updated_sweet.quantity, 120)

    def test_update_nonexistent_sweet(self):
        """Test that updating a non-existent sweet raises ValueError."""
        with self.assertRaises(ValueError):
            self.shop.update_sweet("Non-existent Sweet", price=2.00) 
            
            
                 
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)            