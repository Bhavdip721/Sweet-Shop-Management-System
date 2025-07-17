# Sweet Shop Management System 
# Sweet Shop Management System

This project implements a comprehensive Sweet Shop Management System in Python, designed to help manage inventory, track sales, and provide insights into sweet stock. It includes a core logic for managing `Sweet` objects, a robust set of unit tests following Test-Driven Development (TDD) principles, a Command Line Interface (CLI) for direct interaction, and a Flask-based web application for a user-friendly graphical interface.

 --------------------------------------------------------------Home page--------------------------------------------------------------
 <img width="953" height="475" alt="home page" src="https://github.com/user-attachments/assets/ca10fba7-5362-4fa2-ba0c-46ca05e2b07e" />

--------------------------------------------------------------All sweet page-----------------------------------------------------------
<img width="672" height="446" alt="all_sweet_page" src="https://github.com/user-attachments/assets/915493bd-1385-4921-acdf-609954447265" />

---------------------------------------------------------------Add sweet page----------------------------------------------------------
<img width="664" height="358" alt="add_sweet_page" src="https://github.com/user-attachments/assets/d06fb6d8-2dea-464a-bcfe-4ef3b6da7d6d" />

---------------------------------------------------------------category page-----------------------------------------------------------
<img width="650" height="447" alt="category_page" src="https://github.com/user-attachments/assets/a57b3641-4a81-4896-9a88-7851ff7d02d6" />

--------------------------------------------------------------search sweet page--------------------------------------------------------

<img width="710" height="185" alt="search_sweet_page" src="https://github.com/user-attachments/assets/bd13ef10-41d5-42e5-91e5-9f3be6a3e934" />


---------------------------------------------------------------statistics_page---------------------------------------------------------
<img width="646" height="439" alt="statistics_page" src="https://github.com/user-attachments/assets/aa6dc6f0-dd14-434f-9b6f-59464262471c" />












## Features

*   **Sweet Management**: Add, update, and delete sweet items.
*   **Inventory Tracking**: Keep track of quantities for each sweet.
*   **Unique IDs**: Each sweet is assigned a unique ID.
*   **Search & Filter**: Search sweets by name, description, or category.
*   **Sorting**: Sort sweets by name, price, quantity, or ID.
*   **Category Management**: Organize sweets into different categories.
*   **Availability Check**: Easily identify available and out-of-stock sweets.
*   **Low Stock Alerts**: Identify sweets with quantities below a specified threshold.
*   **Shop Statistics**: View total inventory value, number of sweet types, available types, and more.
*   **Error Handling**: Robust error handling for invalid inputs and operations.
*   **Command Line Interface (CLI)**: Interact with the system via a text-based menu.
*   **Web Application (Flask)**: A simple web interface for managing sweets.
*   **Comprehensive Testing**: Extensive unit tests ensure the reliability and correctness of the core logic.

## Project Structure

\`\`\`
.
├── sweet.py                # Defines the Sweet class
├── sweet_shop.py           # Defines the SweetShop class (core logic)
├── main.py                 # Command Line Interface (CLI) application
├── web_app.py              # Flask web application
├── run_tests.py            # Script to run all unit tests and provide a report
└── scripts/
    ├── test_sweet.py       # Unit tests for the Sweet class
    └── test_sweet_shop.py  # Unit tests for the SweetShop class
\`\`\`

## How to Run

### Prerequisites

*   Python 3.x
*   For the web application, you need Flask:
    \`\`\`bash
    pip install Flask
    \`\`\`

### Running the CLI Application

To start the command-line interface:

\`\`\`bash
python main.py
\`\`\`

Follow the on-screen menu to interact with the sweet shop.

### Running the Web Application

To start the Flask web application:

\`\`\`bash
python web_app.py
\`\`\`

Once started, open your web browser and navigate to `http://localhost:5000` to access the web interface.

### Running Tests

To execute all unit tests and view a detailed report:

\`\`\`bash
python run_tests.py
\`\`\`

This script will run tests for both `Sweet` and `SweetShop` classes and provide a summary of the results.

You can also run individual test files:

\`\`\`bash
python scripts/test_sweet.py
python scripts/test_sweet_shop.py
\`\`\`

## Core Classes and Their Functions

### `Sweet` Class (`sweet.py`)

Represents an individual sweet item with attributes like name, description, price, quantity, category, and a unique ID.

#### Functions:

*   `__init__(self, name, description, price, quantity, category)`: Initializes a new Sweet object.
*   `update_price(self, new_price)`: Updates the price of the sweet.
*   `update_quantity(self, new_quantity)`: Updates the quantity of the sweet.
*   `reduce_quantity(self, amount)`: Reduces the quantity of the sweet.
*   `is_available(self)`: Checks if the sweet is currently in stock (quantity > 0).
*   `to_dict(self)`: Returns a dictionary representation of the sweet.
*   `__str__(self)`: Provides a user-friendly string representation of the sweet.
*   `__repr__(self)`: Provides a detailed string representation for debugging.

### `SweetShop` Class (`sweet_shop.py`)

Manages a collection of `Sweet` objects, providing methods for inventory management and data retrieval.

#### Functions:

*   `__init__(self, name)`: Initializes a new SweetShop with a given name.
*   `add_sweet(self, sweet)`: Adds a new sweet to the shop.
*   `remove_sweet(self, name)`: Removes a sweet by its name.
*   `update_sweet(self, name, **kwargs)`: Updates details of an existing sweet.
*   `get_sweet(self, name)`: Retrieves a sweet by its name.
*   `get_sweet_by_id(self, sweet_id)`: Retrieves a sweet by its unique ID.
*   `search_sweets(self, query)`: Searches for sweets matching a query in name, description, or category.
*   `get_sweets_by_category(self, category)`: Retrieves all sweets belonging to a specific category.
*   `sort_sweets_by_id(self, reverse=False)`: Returns sweets sorted by their ID.
*   `sort_sweets_by_price(self, reverse=False)`: Returns sweets sorted by price.
*   `sort_sweets_by_name(self, reverse=False)`: Returns sweets sorted by name.
*   `sort_sweets_by_quantity(self, reverse=False)`: Returns sweets sorted by quantity.
*   `get_available_sweets(self)`: Returns a list of all sweets currently in stock.
*   `get_total_value(self)`: Calculates the total monetary value of all sweets in inventory.
*   `get_low_stock_sweets(self, threshold=10)`: Returns sweets with quantity at or below the given threshold.
*   `get_all_sweets(self)`: Returns a list of all sweets in the shop.
*   `get_categories(self)`: Returns a list of all unique categories present in the shop.
*   `__str__(self)`: Provides a string representation of the sweet shop.
*   `__len__(self)`: Returns the total number of sweet types in the shop.

### `SweetShopCLI` Class (`main.py`)

The command-line interface for the Sweet Shop Management System.

#### Functions:

*   `__init__(self)`: Initializes the CLI and loads sample data.
*   `load_sample_data(self)`: Populates the shop with initial sweet data.
*   `display_menu(self)`: Displays the main menu options to the user.
*   `view_all_sweets(self)`: Displays a formatted list of all sweets.
*   `add_sweet(self)`: Prompts user for sweet details and adds a new sweet.
*   `update_sweet(self)`: Prompts user to select a sweet and update its details.
*   `delete_sweet(self)`: Prompts user for a sweet name and deletes it.
*   `search_sweets(self)`: Prompts user for a search term and displays results.
*   `sort_sweets(self)`: Prompts user for sorting criteria and displays sorted sweets.
*   `view_by_category(self)`: Allows viewing sweets filtered by category.
*   `view_available_sweets(self)`: Displays only sweets that are in stock.
*   `view_low_stock(self)`: Displays sweets with quantities below a user-defined threshold.
*   `view_statistics(self)`: Shows various statistics about the shop's inventory.
*   `run_tests(self)`: Executes the unit test suite.
*   `run(self)`: The main loop for the CLI application.

### Flask Web Application (`web_app.py`)

Provides a web-based interface for managing the sweet shop.

#### Functions (Routes):

*   `load_sample_data()`: (Helper function) Loads initial sweet data into the shop.
*   `home()`: Renders the home page with shop statistics and featured sweets.
*   `view_sweets()`: Displays all sweets with sorting options.
*   `add_sweet()`: Handles displaying the add sweet form and processing new sweet submissions.
*   `search()`: Handles displaying the search form and showing search results.
*   `categories()`: Displays sweets grouped by their categories.
*   `statistics()`: Shows detailed shop statistics, including low stock alerts.
*   `edit_sweet(name)`: Handles displaying the edit sweet form and processing updates for a specific sweet.
*   `delete_sweet(name)`: Deletes a sweet by its name.

### Test Runner Script (`run_tests.py`)

A utility script to execute all unit tests and provide a consolidated report.

#### Functions:

*   `run_all_tests()`: Discovers and runs all tests from `test_sweet.py` and `test_sweet_shop.py`, printing a detailed report and summary.
*   `demonstrate_functionality()`: Provides a simple demonstration of core `SweetShop` functionalities.
\`\`\`
\`\`\`

```python file="run_tests.py"
# This script will be executed to generate the test report.
# It is included in the CodeProject above.

