import unittest
from sweet_shop import SweetShop
from sweet import Sweet

class TestSweetShop(unittest.TestCase):
  
    # set data
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Reset Sweet ID counter for consistent testing across runs
        Sweet._next_id = 1
        self.shop = SweetShop("Sweet Dreams")
        self.chocolate = Sweet("Chocolate Bar", "Dark chocolate", 2.50, 100, "Chocolate")
        self.gummy = Sweet("Gummy Bears", "Fruity gummy bears", 1.50, 50, "Gummy")
        self.lollipop = Sweet("Rainbow Lollipop", "Colorful lollipop", 1.00, 75, "Hard Candy")
        self.shop.add_sweet(self.chocolate)
        # self.shop.add_sweet(self.gummy)
        # self.shop.add_sweet(self.lollipop)
        
        
      #Test that a sweet shop can be created.
    def test_shop_creation(self):
        
        self.assertEqual(self.shop.name, "Sweet Dreams")
        self.assertEqual(len(self.shop.sweets), 1) 

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



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)