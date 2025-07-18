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
    
      # serch sweet by name and category
      
    def test_search_sweets_by_name(self):
        """Test searching sweets by name."""
        results = self.shop.search_sweets("Chocolate")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Chocolate Bar")

    def test_search_sweets_by_category(self):
        """Test searching sweets by category."""
        results = self.shop.search_sweets("Gummy")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].category, "Gummy")  
        
        
        # test for sort by name,price 
        
    def test_sort_sweets_by_price(self):
        """Test sorting sweets by price."""
        sorted_sweets = self.shop.sort_sweets_by_price()
        prices = [sweet.price for sweet in sorted_sweets]
        self.assertEqual(prices, [1.00, 1.50, 2.50]) # Lollipop, Gummy, Chocolate

    def test_sort_sweets_by_name(self):
        """Test sorting sweets by name."""
        sorted_sweets = self.shop.sort_sweets_by_name()
        names = [sweet.name for sweet in sorted_sweets]
        self.assertEqual(names, ["Chocolate Bar", "Gummy Bears", "Rainbow Lollipop"])
        
        
    # test for avaliable sweet 
    
    def test_get_available_sweets(self):
        """Test getting only available sweets."""
        self.chocolate.update_quantity(0)  # Make unavailable
        available = self.shop.get_available_sweets()
        self.assertEqual(len(available), 2) # Gummy and Lollipop should be available
        self.assertNotIn(self.chocolate, available)
        self.assertIn(self.gummy, available)
        self.assertIn(self.lollipop, available)
        
        # test for total value 
    def test_get_total_value(self):
        """Test calculating total inventory value."""
        # chocolate: $2.50 * 100 = 250
        # gummy:     $1.50 * 50  = 75
        # lollipop:  $1.00 * 75  = 75
        total_value = self.shop.get_total_value()
        self.assertEqual(total_value, 250.00 + 75.00 + 75.00) # 400.00
        
        
     # test for low stock
    def test_get_low_stock_sweets(self):
        """Test getting sweets with low stock."""
        low_stock_sweet = Sweet("Low Stock", "Almost gone", 1.00, 5, "Test")
        self.shop.add_sweet(low_stock_sweet) # ID 4
        
        low_stock = self.shop.get_low_stock_sweets(threshold=10)
        self.assertEqual(len(low_stock), 1)
        self.assertEqual(low_stock[0].name, "Low Stock")

        # Test with a threshold that includes more items
        low_stock_higher_threshold = self.shop.get_low_stock_sweets(threshold=60)
        self.assertEqual(len(low_stock_higher_threshold), 2) # Gummy (50) and Low Stock (5)
        self.assertIn(self.gummy, low_stock_higher_threshold)
        self.assertIn(low_stock_sweet, low_stock_higher_threshold)

# test for all sweet and catogort wise all sweet 
    def test_get_all_sweets(self):
        """Test getting all sweets in the shop."""
        all_sweets = self.shop.get_all_sweets()
        self.assertEqual(len(all_sweets), 3)
        self.assertIn(self.chocolate, all_sweets)
        self.assertIn(self.gummy, all_sweets)
        self.assertIn(self.lollipop, all_sweets)

    def test_get_categories(self):
        """Test getting all unique categories."""
        categories = self.shop.get_categories()
        # Convert to set for comparison as order might not be guaranteed
        self.assertEqual(set(categories), {"Chocolate", "Gummy", "Hard Candy"})
     
     
     #  Test string representation of the sweet shop and  Test __len__ method for the number of sweets.
    def test_str_representation(self):
        
        expected = "Sweet Dreams - 3 sweets available"
        self.assertEqual(str(self.shop), expected)

    def test_len(self):
        
        self.assertEqual(len(self.shop), 3)
        self.shop.remove_sweet("Chocolate Bar")
        self.assertEqual(len(self.shop), 2)    

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)            