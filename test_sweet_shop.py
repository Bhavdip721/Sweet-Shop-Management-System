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
        self.shop.add_sweet(self.gummy)
        self.shop.add_sweet(self.lollipop)
        
        
      #Test that a sweet shop can be created.
    def test_shop_creation(self):
        
        self.assertEqual(self.shop.name, "Sweet Dreams")
        self.assertEqual(len(self.shop.sweets), 3) # Now 3 sweets are added in setUp



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)