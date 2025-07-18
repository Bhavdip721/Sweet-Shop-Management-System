   # report of Delight Manager Web Store 
# Sweet Shop Management System - Test Case and Functionality Report



This report outlines all the unit test cases implemented for the Sweet Shop Management System, detailing the specific functionality each test verifies. The tests are organized by the class they target: `Sweet` and `SweetShop`.

## 1. `Sweet` Class Test Cases (`scripts/test_sweet.py`)

The `TestSweet` class ensures the correct behavior and data integrity of individual sweet items.

*   **`test_sweet_creation`**
    *   **Functionality Tested**: Verifies that a sweet can be created with all required attributes (name, description, price, quantity, category) and is assigned a unique ID.
*   **`test_sweet_creation_with_invalid_price`**
    *   **Functionality Tested**: Confirms that creating a sweet with a negative price correctly raises a `ValueError`.
*   **`test_sweet_creation_with_invalid_quantity`**
    *   **Functionality Tested**: Confirms that creating a sweet with a negative quantity correctly raises a `ValueError`.
*   **`test_update_price`**
    *   **Functionality Tested**: Ensures the price of a sweet can be successfully updated to a new valid value.
*   **`test_update_price_invalid`**
    *   **Functionality Tested**: Checks that attempting to update a sweet's price to a negative value raises a `ValueError`.
*   **`test_update_quantity`**
    *   **Functionality Tested**: Ensures the quantity of a sweet can be successfully updated to a new valid value.
*   **`test_update_quantity_invalid`**
    *   **Functionality Tested**: Checks that attempting to update a sweet's quantity to a negative value raises a `ValueError`.
*   **`test_reduce_quantity`**
    *   **Functionality Tested**: Verifies that the quantity of a sweet can be reduced by a specified amount.
*   **`test_reduce_quantity_insufficient`**
    *   **Functionality Tested**: Confirms that attempting to reduce the quantity beyond available stock raises a `ValueError`.
*   **`test_is_available`**
    *   **Functionality Tested**: Checks if the `is_available` method correctly returns `True` when quantity is greater than 0 and `False` when quantity is 0.
*   **`test_to_dict`**
    *   **Functionality Tested**: Verifies that the `to_dict` method correctly converts the sweet object's attributes into a dictionary representation, including its ID.
*   **`test_get_details`**
    *   **Functionality Tested**: (Note: This test appears to be a placeholder or incomplete in the provided code, as it doesn't assert anything. It's intended to test retrieving sweet details.)
*   **`test_str_representation`**
    *   **Functionality Tested**: Ensures the `__str__` method provides the expected user-friendly string representation of the sweet, including its ID.
*   **`test_repr_representation`**
    *   **Functionality Tested**: Ensures the `__repr__` method provides the expected detailed string representation of the sweet for debugging purposes, including its ID.

## 2. `SweetShop` Class Test Cases (`scripts/test_sweet_shop.py`)

The `TestSweetShop` class validates the core inventory management functionalities of the sweet shop.

*   **`test_shop_creation`**
    *   **Functionality Tested**: Verifies that a `SweetShop` instance can be created with a name and that initial sweets are correctly added during setup.
*   **`test_add_sweet`**
    *   **Functionality Tested**: Ensures a new sweet can be successfully added to the shop's inventory.
*   **`test_add_duplicate_sweet`**
    *   **Functionality Tested**: Confirms that attempting to add a sweet with a name that already exists in the shop raises a `ValueError`.
*   **`test_remove_sweet`**
    *   **Functionality Tested**: Verifies that a sweet can be successfully removed from the shop by its name.
*   **`test_remove_nonexistent_sweet`**
    *   **Functionality Tested**: Checks that attempting to remove a sweet that does not exist in the shop raises a `ValueError`.
*   **`test_update_sweet`**
    *   **Functionality Tested**: Ensures that an existing sweet's details (price, quantity, description, category) can be updated.
*   **`test_update_nonexistent_sweet`**
    *   **Functionality Tested**: Confirms that attempting to update a sweet that does not exist in the shop raises a `ValueError`.
*   **`test_get_sweet`**
    *   **Functionality Tested**: Verifies that a sweet can be retrieved by its name, and that `None` is returned for non-existent sweets.
*   **`test_get_sweet_by_id`**
    *   **Functionality Tested**: Verifies that a sweet can be retrieved by its unique ID, and that `None` is returned for non-existent IDs.
*   **`test_search_sweets_by_name`**
    *   **Functionality Tested**: Checks that the `search_sweets` method correctly finds sweets based on a name query.
*   **`test_search_sweets_by_category`**
    *   **Functionality Tested**: Checks that the `search_sweets` method correctly finds sweets based on a category query.
*   **`test_get_sweets_by_category`**
    *   **Functionality Tested**: Verifies that all sweets belonging to a specific category can be retrieved.
*   **`test_sort_sweets_by_price`**
    *   **Functionality Tested**: Ensures that sweets can be sorted correctly in ascending order by their price.
*   **`test_sort_sweets_by_name`**
    *   **Functionality Tested**: Ensures that sweets can be sorted correctly in ascending alphabetical order by their name.
*   **`test_get_available_sweets`**
    *   **Functionality Tested**: Verifies that only sweets with a quantity greater than 0 are returned.
*   **`test_get_total_value`**
    *   **Functionality Tested**: Checks the accurate calculation of the total monetary value of all sweets in the inventory.
*   **`test_get_low_stock_sweets`**
    *   **Functionality Tested**: Ensures that sweets with quantities at or below a specified low-stock threshold are correctly identified.
*   **`test_get_all_sweets`**
    *   **Functionality Tested**: Verifies that a list of all sweets currently in the shop can be retrieved.
*   **`test_get_categories`**
    *   **Functionality Tested**: Checks that all unique categories present in the shop's inventory are correctly identified and returned.
*   **`test_str_representation`**
    *   **Functionality Tested**: Ensures the `__str__` method provides the expected string representation of the sweet shop (name and number of sweets).
*   **`test_len`**
    *   **Functionality Tested**: Verifies that the `__len__` method correctly returns the total number of unique sweet types in the shop.

This comprehensive suite of tests ensures that both the `Sweet` and `SweetShop` classes function reliably and meet their specified requirements.
