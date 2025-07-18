from sweet_shop import SweetShop
from sweet import Sweet
import sys
import subprocess
import os # Import os for path manipulation

class SweetShopCLI:
    """Command Line Interface for Sweet Shop Management System."""

    def __init__(self):
        self.shop = SweetShop("Sweet Dreams Candy Store")
        # Reset Sweet ID counter at the start of CLI to ensure predictable IDs for sample data
        Sweet._next_id = 1
        self.load_sample_data()

    def load_sample_data(self):
        """Load some sample sweets for demonstration."""
        sample_sweets = [
            Sweet("Chocolate Bar", "Rich dark chocolate bar", 2.50, 100, "Chocolate"),
            Sweet("Gummy Bears", "Colorful fruity gummy bears", 1.50, 75, "Gummy"),
            Sweet("Rainbow Lollipop", "Multi-colored swirl lollipop", 1.00, 50, "Hard Candy"),
            Sweet("Marshmallows", "Soft fluffy marshmallows", 2.00, 30, "Soft Candy"),
            Sweet("Chocolate Truffles", "Premium chocolate truffles", 4.50, 25, "Chocolate"),
            Sweet("Sour Worms", "Tangy sour gummy worms", 1.75, 60, "Gummy"),
            Sweet("Peppermint Candy", "Classic peppermint hard candy", 0.75, 80, "Hard Candy"),
            Sweet("Caramel Chews", "Creamy caramel chews", 2.25, 40, "Soft Candy")
        ]

        for sweet in sample_sweets:
            self.shop.add_sweet(sweet)

        print(f"Welcome to {self.shop.name}!")
        print(f"Loaded {len(sample_sweets)} sample sweets.\n")

    def display_menu(self):
        """Display the main menu."""
        print("\n" + "="*50)
        print("SWEET SHOP MANAGEMENT SYSTEM")
        print("="*50)
        print("1. View All Sweets")
        print("2. Add New Sweet")
        print("3. Update Sweet")
        print("4. Delete Sweet")
        print("5. Search Sweets")
        print("6. Sort Sweets")
        print("7. View by Category")
        print("8. View Available Sweets Only")
        print("9. View Low Stock Sweets")
        print("10. View Shop Statistics")
        print("11. Run Tests")
        print("0. Exit")
        print("="*50)

    def view_all_sweets(self):
        """Display all sweets in the shop."""
        sweets = self.shop.get_all_sweets()
        if not sweets:
            print("No sweets available in the shop.")
            return

        print(f"\nAll Sweets in {self.shop.name}:")
        print("-" * 80)
        # Added 'ID' column to the display
        print(f"{'ID':<4} {'Name':<20} {'Price':<8} {'Qty':<6} {'Category':<15} {'Description'}")
        print("-" * 80)

        for sweet in sweets:
            # Display sweet.id
            print(f"{sweet.id:<4} {sweet.name:<20} ${sweet.price:<7.2f} {sweet.quantity:<6} {sweet.category:<15} {sweet.description}")

    def add_sweet(self):
        """Add a new sweet to the shop."""
        print("\nAdd New Sweet:")
        try:
            name = input("Enter sweet name: ").strip()
            if not name:
                print("Sweet name cannot be empty.")
                return

            description = input("Enter description: ").strip()
            price = float(input("Enter price: $"))
            quantity = int(input("Enter quantity: "))
            category = input("Enter category: ").strip()

            sweet = Sweet(name, description, price, quantity, category)
            self.shop.add_sweet(sweet)
            print(f"Successfully added '{name}' to the shop!")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def update_sweet(self):
        """Update an existing sweet."""
        name = input("Enter the name of the sweet to update: ").strip()
        sweet = self.shop.get_sweet(name)

        if not sweet:
            print(f"Sweet '{name}' not found.")
            return

        print(f"\nCurrent details for '{name}':")
        print(f"ID: {sweet.id}") # Display ID for clarity
        print(f"Description: {sweet.description}")
        print(f"Price: ${sweet.price:.2f}")
        print(f"Quantity: {sweet.quantity}")
        print(f"Category: {sweet.category}")

        print("\nEnter new values (press Enter to keep current value):")

        try:
            updates = {}

            new_desc = input(f"Description [{sweet.description}]: ").strip()
            if new_desc:
                updates['description'] = new_desc

            new_price = input(f"Price [${sweet.price:.2f}]: ").strip()
            if new_price:
                updates['price'] = float(new_price)

            new_qty = input(f"Quantity [{sweet.quantity}]: ").strip()
            if new_qty:
                updates['quantity'] = int(new_qty)

            new_cat = input(f"Category [{sweet.category}]: ").strip()
            if new_cat:
                updates['category'] = new_cat

            if updates:
                self.shop.update_sweet(name, **updates)
                print(f"Successfully updated '{name}'!")
            else:
                print("No changes made.")

        except ValueError as e:
            print(f"Error: {e}")

    def delete_sweet(self):
        """Delete a sweet from the shop."""
        name = input("Enter the name of the sweet to delete: ").strip()

        try:
            sweet = self.shop.remove_sweet(name)
            print(f"Successfully deleted '{sweet.name}' (ID: {sweet.id}) from the shop!")
        except ValueError as e:
            print(f"Error: {e}")

    def search_sweets(self):
        """Search for sweets."""
        query = input("Enter search term (name, description, or category): ").strip()

        if not query:
            print("Search term cannot be empty.")
            return

        results = self.shop.search_sweets(query)

        if not results:
            print(f"No sweets found matching '{query}'.")
            return

        print(f"\nSearch results for '{query}':")
        print("-" * 80)
        # Added 'ID' column
        print(f"{'ID':<4} {'Name':<20} {'Price':<8} {'Qty':<6} {'Category':<15} {'Description'}")
        print("-" * 80)

        for sweet in results:
            # Display sweet.id
            print(f"{sweet.id:<4} {sweet.name:<20} ${sweet.price:<7.2f} {sweet.quantity:<6} {sweet.category:<15} {sweet.description}")

    def sort_sweets(self):
        """Sort and display sweets."""
        print("\nSort Options:")
        print("1. By Name (A-Z)")
        print("2. By Name (Z-A)")
        print("3. By Price (Low to High)")
        print("4. By Price (High to Low)")
        print("5. By Quantity (Low to High)")
        print("6. By Quantity (High to Low)")

        try:
            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                sweets = self.shop.sort_sweets_by_name()
                title = "Sweets sorted by Name (A-Z)"
            elif choice == 2:
                sweets = self.shop.sort_sweets_by_name(reverse=True)
                title = "Sweets sorted by Name (Z-A)"
            elif choice == 3:
                sweets = self.shop.sort_sweets_by_price()
                title = "Sweets sorted by Price (Low to High)"
            elif choice == 4:
                sweets = self.shop.sort_sweets_by_price(reverse=True)
                title = "Sweets sorted by Price (High to Low)"
            elif choice == 5:
                sweets = self.shop.sort_sweets_by_quantity()
                title = "Sweets sorted by Quantity (Low to High)"
            elif choice == 6:
                sweets = self.shop.sort_sweets_by_quantity(reverse=True)
                title = "Sweets sorted by Quantity (High to Low)"
            else:
                print("Invalid choice.")
                return

            print(f"\n{title}:")
            print("-" * 80)
            # Added 'ID' column
            print(f"{'ID':<4} {'Name':<20} {'Price':<8} {'Qty':<6} {'Category':<15} {'Description'}")
            print("-" * 80)

            for sweet in sweets:
                # Display sweet.id
                print(f"{sweet.id:<4} {sweet.name:<20} ${sweet.price:<7.2f} {sweet.quantity:<6} {sweet.category:<15} {sweet.description}")

        except ValueError:
            print("Invalid input. Please enter a number.")

    def view_by_category(self):
        """View sweets by category."""
        categories = self.shop.get_categories()

        if not categories:
            print("No categories available.")
            return

        print("\nAvailable Categories:")
        sorted_categories = sorted(list(categories)) # Convert set to list and sort for consistent display
        for i, category in enumerate(sorted_categories, 1):
            print(f"{i}. {category}")

        try:
            choice = int(input("Enter category number: ")) - 1
            if 0 <= choice < len(sorted_categories):
                selected_category = sorted_categories[choice]
                sweets = self.shop.get_sweets_by_category(selected_category)

                print(f"\nSweets in '{selected_category}' category:")
                print("-" * 80)
                # Added 'ID' column
                print(f"{'ID':<4} {'Name':<20} {'Price':<8} {'Qty':<6} {'Description'}")
                print("-" * 80)

                for sweet in sweets:
                    # Display sweet.id
                    print(f"{sweet.id:<4} {sweet.name:<20} ${sweet.price:<7.2f} {sweet.quantity:<6} {sweet.description}")
            else:
                print("Invalid category selection.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def view_available_sweets(self):
        """View only available sweets."""
        sweets = self.shop.get_available_sweets()

        if not sweets:
            print("No sweets are currently available.")
            return

        print("\nAvailable Sweets (In Stock):")
        print("-" * 80)
        # Added 'ID' column
        print(f"{'ID':<4} {'Name':<20} {'Price':<8} {'Qty':<6} {'Category':<15} {'Description'}")
        print("-" * 80)

        for sweet in sweets:
            # Display sweet.id
            print(f"{sweet.id:<4} {sweet.name:<20} ${sweet.price:<7.2f} {sweet.quantity:<6} {sweet.category:<15} {sweet.description}")

    def view_low_stock(self):
        """View sweets with low stock."""
        try:
            threshold_input = input("Enter stock threshold (default 10): ").strip()
            threshold = int(threshold_input) if threshold_input else 10
            
            sweets = self.shop.get_low_stock_sweets(threshold)

            if not sweets:
                print(f"No sweets with stock <= {threshold}.")
                return

            print(f"\nSweets with Low Stock (<= {threshold}):")
            print("-" * 80)
            # Added 'ID' column
            print(f"{'ID':<4} {'Name':<20} {'Price':<8} {'Qty':<6} {'Category':<15} {'Description'}")
            print("-" * 80)

            for sweet in sweets:
                # Display sweet.id
                print(f"{sweet.id:<4} {sweet.name:<20} ${sweet.price:<7.2f} {sweet.quantity:<6} {sweet.category:<15} {sweet.description}")

        except ValueError:
            print("Invalid threshold value. Please enter a number.")

    def view_statistics(self):
        """Display shop statistics."""
        total_sweets = len(self.shop)
        available_sweets = len(self.shop.get_available_sweets())
        total_value = self.shop.get_total_value()
        categories = self.shop.get_categories()
        low_stock = len(self.shop.get_low_stock_sweets())

        print(f"\n{self.shop.name} - Statistics:")
        print("=" * 40)
        print(f"Total Sweet Types: {total_sweets}")
        print(f"Available Sweet Types: {available_sweets}")
        print(f"Out of Stock: {total_sweets - available_sweets}")
        print(f"Total Inventory Value: ${total_value:.2f}")
        print(f"Number of Categories: {len(categories)}")
        print(f"Low Stock Items: {low_stock}")
        print(f"Categories: {', '.join(sorted(categories))}")

    def run_tests(self):
        """Run the test suites using the dedicated test runner."""
        # Add the current directory to sys.path to find run_tests.py
        # and ensure scripts subdirectory is also in path for test modules
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir) # Assuming sweet_shop_cli.py is in project root
        
        # Ensure project root is in sys.path for sweet.py and sweet_shop.py
        if project_root not in sys.path:
            sys.path.insert(0, project_root)
        
        # Ensure scripts directory is in sys.path for test_sweet.py and test_sweet_shop.py
        scripts_dir = os.path.join(project_root, 'scripts')
        if scripts_dir not in sys.path:
            sys.path.insert(0, scripts_dir)

        try:
            # Dynamically import the run_all_tests function from run_tests.py
            from run_tests import run_all_tests
            run_all_tests()
        except ImportError as e:
            print(f"Error: Could not import test runner. Make sure 'run_tests.py' is in the project root and test files are in 'scripts' subdirectory. Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while running tests: {e}")
            import traceback
            traceback.print_exc()

    def run(self):
        """Main application loop."""
        while True:
            self.display_menu()

            try:
                choice = input("\nEnter your choice (0-11): ").strip()

                if choice == '0':
                    print("Thank you for using Sweet Shop Management System!")
                    break
                elif choice == '1':
                    self.view_all_sweets()
                elif choice == '2':
                    self.add_sweet()
                elif choice == '3':
                    self.update_sweet()
                elif choice == '4':
                    self.delete_sweet()
                elif choice == '5':
                    self.search_sweets()
                elif choice == '6':
                    self.sort_sweets()
                elif choice == '7':
                    self.view_by_category()
                elif choice == '8':
                    self.view_available_sweets()
                elif choice == '9':
                    self.view_low_stock()
                elif choice == '10':
                    self.view_statistics()
                elif choice == '11':
                    self.run_tests()
                else:
                    print("Invalid choice. Please try again.")

                input("\nPress Enter to continue...")

            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                input("Press Enter to continue...")

if __name__ == "__main__":
    app = SweetShopCLI()
    app.run()
