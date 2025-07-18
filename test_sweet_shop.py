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
    
     # test for if serch sweet in shop is get or not
             
    def test_get_sweet(self):
        """Test getting a sweet by name."""
        retrieved = self.shop.get_sweet("Chocolate Bar")
        self.assertEqual(retrieved.name, "Chocolate Bar")
        self.assertIsNone(self.shop.get_sweet("Non-existent Sweet"))

        # self.assertEqual(retrieved.name, "Vanilla Ice Cream", "This assertion is an intentional 'red case' and is expected to fail.")

 
    def test_get_sweet_by_id(self):
        """Test getting a sweet by its unique ID."""
        # IDs are 1, 2, 3 for chocolate, gummy, lollipop respectively due to setUp
        retrieved_chocolate = self.shop.get_sweet_by_id(self.chocolate.id)
        self.assertEqual(retrieved_chocolate.name, "Chocolate Bar")
        self.assertEqual(retrieved_chocolate.id, self.chocolate.id)

        retrieved_gummy = self.shop.get_sweet_by_id(self.gummy.id)
        self.assertEqual(retrieved_gummy.name, "Gummy Bears")
        self.assertEqual(retrieved_gummy.id, self.gummy.id)

        self.assertIsNone(self.shop.get_sweet_by_id(999)) # Test non-existent ID
        
    def test_get_sweets_by_category(self):
        """Test getting sweets by category."""
        chocolate_sweets = self.shop.get_sweets_by_category("Chocolate")
        self.assertEqual(len(chocolate_sweets), 1)
        self.assertEqual(chocolate_sweets[0].name, "Chocolate Bar")
    
        
                 
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)            