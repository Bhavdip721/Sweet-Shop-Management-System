# Sweet Shop Management System 
# Sweet Shop Management System

This project implements a comprehensive Sweet Shop Management System in Python, designed to help manage inventory, track sales, and provide insights into sweet stock. It includes a core logic for managing `Sweet` objects, a robust set of unit tests following Test-Driven Development (TDD) principles, a Command Line Interface (CLI) for direct interaction, and a Flask-based web application for a user-friendly graphical interface.

 --------------------------------------------------------------Home page--------------------------------------------------------------
 <img width="900" height="400" alt="home page" src="https://github.com/user-attachments/assets/ca10fba7-5362-4fa2-ba0c-46ca05e2b07e" />

--------------------------------------------------------------All sweet page-----------------------------------------------------------


<img width="672" height="446" alt="all_sweet_page" src="https://github.com/user-attachments/assets/915493bd-1385-4921-acdf-609954447265" />


---------------------------------------------------------------Add sweet page----------------------------------------------------------


<img width="664" height="358" alt="add_sweet_page" src="https://github.com/user-attachments/assets/d06fb6d8-2dea-464a-bcfe-4ef3b6da7d6d" />


---------------------------------------------------------------category page-----------------------------------------------------------


<img width="600" height="400" alt="category_page" src="https://github.com/user-attachments/assets/a57b3641-4a81-4896-9a88-7851ff7d02d6" />


--------------------------------------------------------------search sweet page--------------------------------------------------------


<img width="600" height="150" alt="search_sweet_page" src="https://github.com/user-attachments/assets/bd13ef10-41d5-42e5-91e5-9f3be6a3e934" />


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

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
## details about python module 

1. **`import json`**: 
   - **What it is**: A built-in Python module for working with JSON (JavaScript Object Notation) data.
   - **Role**: It allows you to parse JSON data into Python objects and convert Python objects back into JSON format. This is particularly useful for APIs that send and receive data in JSON format.

2. **`from flask import Flask`**: 
   - **What it is**: Part of the Flask web framework, this class is essential for creating a Flask application.
   - **Role**: You create an instance of the `Flask` class to start your web application, defining the routes and handling requests.

3. **`render_template_string`**: 
   - **What it is**: A function provided by Flask for rendering HTML templates.
   - **Role**: It allows you to render HTML directly from a string, which is useful for quick responses without needing separate HTML files.

4. **`request`**: 
   - **What it is**: An object in Flask that contains all the data sent by the client to the server.
   - **Role**: It provides access to form data, query parameters, and other request-related information, enabling you to handle user input effectively.

5. **`jsonify`**: 
   - **What it is**: A Flask function that converts Python data structures into JSON format.
   - **Role**: It is commonly used in API endpoints to return JSON responses, automatically setting the correct content type.

6. **`redirect`**: 
   - **What it is**: A function in Flask that redirects users to a different URL.
   - **Role**: It is often used after form submissions or when you want to navigate users to a different page within the application.

7. **`url_for`**: 
   - **What it is**: A Flask function that generates a URL to a specific function based on its name.
   - **Role**: It helps create dynamic links to routes in your application, avoiding hardcoded URLs and making your code more maintainable.

8. **`import sys`**: 
   - **What it is**: A built-in Python module that provides access to some variables used or maintained by the Python interpreter.
   - **Role**: It can be used for manipulating the Python runtime environment, such as reading command-line arguments or exiting the program.

9. **`import os`**: 
   - **What it is**: A built-in Python module that provides a way to interact with the operating system.
   - **Role**: It allows you to perform operations like reading or writing to the file system, accessing environment variables, and executing system commands.

10. **`from io import StringIO`**: 
    - **What it is**: A class from the `io` module that creates an in-memory stream for text I/O.
    - **Role**: It is useful for capturing output from functions or simulating file operations without creating actual files.

11. **`import subprocess`**: 
    - **What it is**: A built-in Python module that allows you to spawn new processes and connect to their input/output/error pipes.
    - **Role**: It is useful for running shell commands or external programs from within your Python code, enabling more complex interactions with the system.



---------------------------------------------------for TDD -------------------------------------------------------------
## `unittest` Module Overview

**`import unittest`**:
- **What it is**: The `unittest` module is a built-in Python library for creating and running unit tests. It is part of the standard library,
                  so no additional installation is required.

- **Role**: It provides a framework for writing and executing tests to ensure that individual units of code (like functions or methods) work as expected.
            This is crucial for maintaining code quality and catching bugs early in the development process.

### Key Features:
- **Test Case Creation**: You can create test cases by subclassing `unittest.TestCase`. Each method within the class that starts with `test_` is treated as a separate test.

- **Assertions**: The module provides various assertion methods (e.g., `assertEqual`, `assertTrue`, `assertRaises`) to check for expected outcomes in your tests.

- **Test Discovery**: It can automatically discover and run tests in your project, making it easy to manage large test suites.

- **Test Fixtures**: You can set up preconditions and clean up after tests using `setUp()` and `tearDown()` methods, which run before and after each test method, respectively.



---------------------------------------------------------------------------------AI--------------------------------------------------------------------

------------------------------------------ > v0 dev : V0. dev is an AI-powered platform that generates responsive and visually appealing user interfaces,
                                                      empowering developers to build stunning web applications without extensive coding.
