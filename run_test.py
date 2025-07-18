#!/usr/bin/env python3
"""Test runner script for Sweet Shop Management System
Runs all tests and provides a comprehensive report"""
import unittest
import sys
import os
from io import StringIO

# Add the 'scripts' directory to sys.path to allow importing test modules
# This assumes run_tests.py is in the project root and test files are in a 'scripts' subdirectory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

# Import Sweet here to reset its ID counter before any tests run
from sweet import Sweet

def run_all_tests():
    """Run all test suites and return results."""
    
    # Reset Sweet ID counter at the start of all tests to ensure consistency
    Sweet._next_id = 1

    print("=" * 60)
    print("SWEET SHOP MANAGEMENT SYSTEM - TEST SUITE")
    print("=" * 60)
    print("Following TDD (Test-Driven Development) principles")
    print("Running comprehensive tests...\n")

    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add test modules
    try:
        # Import test modules
        from test_sweet import TestSweet
        from test_sweet_shop import TestSweetShop
        
        # Add tests to suite
        suite.addTests(loader.loadTestsFromTestCase(TestSweet))
        suite.addTests(loader.loadTestsFromTestCase(TestSweetShop))

        # Run tests with detailed output
        stream = StringIO()
        runner = unittest.TextTestRunner(stream=stream, verbosity=2)
        result = runner.run(suite)

        # Print results
        output = stream.getvalue()
        print(output)

        # Summary
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        print(f"Tests run: {result.testsRun}")
        print(f"Failures: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
        
        # Avoid division by zero if no tests were run
        if result.testsRun > 0:
            print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
        else:
            print("Success rate: N/A (No tests were run)")

        if result.failures:
            print(f"\nFAILURES ({len(result.failures)}):")
            for test, traceback in result.failures:
                print(f"- {test}: {traceback.split('AssertionError: ')[-1].split('\\n')[0] if 'AssertionError:' in traceback else 'Unknown failure'}")

        if result.errors:
            print(f"\nERRORS ({len(result.errors)}):")
            for test, traceback in result.errors:
                print(f"- {test}: {traceback.split('\\n')[-2] if len(traceback.split('\\n')) > 1 else 'Unknown error'}")

        if result.wasSuccessful():
            print("\n🎉 ALL TESTS PASSED! The Sweet Shop Management System is working correctly.")
            print("✅ TDD Implementation successful - all requirements met!")
        else:
            print("\n❌ Some tests failed. Please review the implementation.")

        return result.wasSuccessful()

    except ImportError as e:
        print(f"❌ Error importing test modules: {e}")
        print("Make sure 'sweet.py', 'sweet_shop.py' are in the root, and 'test_sweet.py', 'test_sweet_shop.py' are in the 'scripts' directory.")
        return False
    except Exception as e:
        print(f"❌ Unexpected error running tests: {e}")
        return False

def demonstrate_functionality():
    """Demonstrate the Sweet Shop functionality."""
    
    # Reset Sweet ID counter for demonstration to ensure predictable IDs
    Sweet._next_id = 1

    print("\n" + "=" * 60)
    print("FUNCTIONALITY DEMONSTRATION")
    print("=" * 60)

    try:
        from sweet_shop import SweetShop
        from sweet import Sweet

        # Create shop and add sample data
        demo_shop = SweetShop("Demo Sweet Shop")

        print("1. Creating sweets...")
        sweets_data = [
            ("Chocolate Bar", "Rich dark chocolate", 2.50, 100, "Chocolate"),
            ("Gummy Bears", "Fruity gummy bears", 1.50, 75, "Gummy"),
            ("Lollipop", "Rainbow lollipop", 1.00, 50, "Hard Candy")
        ]

        for name, desc, price, qty, cat in sweets_data:
            sweet = Sweet(name, desc, price, qty, cat)
            demo_shop.add_sweet(sweet)
            print(f"   ✅ Added: {sweet}")

        print(f"\n2. Shop status: {demo_shop}")

        print("\n3. Searching for 'chocolate'...")
        results = demo_shop.search_sweets("chocolate")
        for sweet in results:
            print(f"   🔍 Found: {sweet}")

        print("\n4. Sorting by price...")
        sorted_sweets = demo_shop.sort_sweets_by_price()
        for sweet in sorted_sweets:
            print(f"   💰 {sweet.name}: ${sweet.price:.2f}")

        print("\n5. Categories available:")
        categories = demo_shop.get_categories()
        for cat in categories:
            count = len(demo_shop.get_sweets_by_category(cat))
            print(f"   📂 {cat}: {count} sweets")

        print(f"\n6. Total inventory value: ${demo_shop.get_total_value():.2f}")

        print("\n7. Updating sweet...")
        demo_shop.update_sweet("Chocolate Bar", price=3.00, quantity=90)
        updated = demo_shop.get_sweet("Chocolate Bar")
        print(f"   ✏️  Updated: {updated}")

        print("\n8. Low stock check (threshold: 60)...")
        low_stock = demo_shop.get_low_stock_sweets(60)
        for sweet in low_stock:
            print(f"   ⚠️  Low stock: {sweet.name} ({sweet.quantity} left)")
            
        print("\n9. Retrieving sweet by ID (e.g., Chocolate Bar, ID 1)...")
        sweet_by_id = demo_shop.get_sweet_by_id(1)
        if sweet_by_id:
            print(f"   🆔 Found by ID: {sweet_by_id}")
        else:
            print("   🆔 Sweet with ID 1 not found.")


        print("\n✅ All functionality working correctly!")
        return True

    except Exception as e:
        print(f"❌ Error in demonstration: {e}")
        import traceback
        traceback.print_exc() # Print full traceback for debugging
        return False

if __name__ == "__main__":
    print("Sweet Shop Management System - TDD Test Runner")
    print("This system was built following Test-Driven Development principles")
    print("Tests were written first, then implementation followed\n")

    # Run tests
    tests_passed = run_all_tests()

    # Demonstrate functionality
    demo_success = demonstrate_functionality()

    # Final summary
    print("\n" + "=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)

    if tests_passed and demo_success:
        print("🎉 SUCCESS: Sweet Shop Management System is fully functional!")
        print("✅ All TDD tests pass")
        print("✅ All features working correctly")
        print("\nFeatures implemented:")
        print("• Add, update, delete sweets")
        print("• Search and filter functionality")
        print("• Sorting by multiple criteria")
        print("• Category management")
        print("• Inventory tracking and statistics")
        print("• Low stock alerts")
        print("• Comprehensive error handling")
        print("• CLI and Web interfaces (placeholders)") # Clarified as placeholders
    else:
        print("❌ Issues detected. Please review the implementation.")
        print(f"\nTo run the CLI interface: python sweet_shop_cli.py") # Corrected to sweet_shop_cli.py
        print(f"To run the web interface: (Not provided in this project)") # Clarified
        print(f"To run tests individually:")
        print(f"   python scripts/test_sweet.py")
        print(f"   python scripts/test_sweet_shop.py")
