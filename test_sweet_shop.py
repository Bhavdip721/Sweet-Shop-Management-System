import unittest

class TestSweetShop(unittest.TestCase):
    #Test that a sweet shop can be created.
    
    def test_shop_creation(self):
        
        self.assertEqual(self.shop.name, "Sweet Dreams")
        self.assertEqual(len(self.shop.sweets), 3) # Now 3 sweets are added in setUp



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)