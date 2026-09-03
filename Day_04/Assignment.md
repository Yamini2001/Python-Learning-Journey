## Day 4 Practice Assignments: Dictionaries & Exception Handling

## Objective
Model key-value storage relations, implement robust custom exceptions, and design atomic transaction processing using try-except-finally blocks.

## Easy Assignments

## Assignment 1: Inventory Tracker for CDAC Bookstore
Scenario
The CDAC Bookstore needs a backend helper module to manage books and their quantities. The inventory is stored in a Python dictionary where keys are book titles (strings) and values are quantities in stock (non-negative integers).

## Problem Description
Write a function manage_bookstore_inventory(inventory, action, book_title, quantity=0) that handles inventory operations safely.

The action parameter can be one of three options: "add", "sell", or "lookup".
Add Action ("add"):
Add the specified quantity to the existing stock of book_title.
If the book is not in the inventory dictionary, add it as a new key with quantity as the value.
Sell Action ("sell"):
Decrease the stock of book_title by the specified quantity.
If the book is not found in the inventory, print a message: Error: Book '<book_title>' not found in inventory. and make no changes. (Do not let the program crash with a KeyError).
If the requested quantity to sell exceeds the stock available, print: Error: Insufficient stock for '<book_title>'. Available: <current_stock>. and make no changes.
If the stock reaches exactly 0 after a successful sale, remove the book key from the inventory entirely.
Lookup Action ("lookup"):
Look up the stock quantity of book_title and return it.
Use safe dictionary retrieval; if the book does not exist, return 0 without throwing a KeyError.
The function must return the updated/current inventory dictionary.

Example Walkthrough
# Initial Inventory
inventory = {"Python Basics": 10, "Learning AI": 5}

# 1. Add Stock
inventory = manage_bookstore_inventory(inventory, "add", "Python Basics", 5)
# Result: {"Python Basics": 15, "Learning AI": 5}

# 2. Sell Stock Safely (Missing Book)
inventory = manage_bookstore_inventory(inventory, "sell", "Data Science 101", 1)
# Console output: Error: Book 'Data Science 101' not found in inventory.

# 3. Sell Stock (Insufficient)
inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 10)
# Console output: Error: Insufficient stock for 'Learning AI'. Available: 5.

# 4. Sell Stock (Exactly Zero Stock)
inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 5)
# Result: {"Python Basics": 15}

---

## Assignment 2: Robust Phonebook Contact Registry
Scenario
You are writing a Command-Line Interface (CLI) contact registry that maps user names to their phone numbers. The program needs to validate user inputs robustly to prevent corrupted formatting or empty values from breaking the registry database.

**Problem Description**
Define a custom exception class named InvalidPhoneNumberError that inherits from Exception.
Write a function register_contact(phonebook, name, phone_input):
phonebook is a dictionary mapping contact names (strings) to their phone numbers (strings).
Validate the name parameter: it must be a non-empty string consisting only of alphabetic characters and spaces. If invalid, raise a standard ValueError with the message: "Contact name must be a non-empty alphabetic string."
Validate the phone_input parameter: it must consist only of digits. Check this by attempting to convert it to an integer using int().
If the conversion fails (raises a ValueError), catch that exception and raise your custom InvalidPhoneNumberError with the message: "Phone number must contain digits only."
If validations pass, store phone_input as a string in the phonebook under the key name (preserving any leading zeros).
Return the updated phonebook dictionary.
```
text

Example Walkthrough
contacts = {}

# 1. Valid Input
contacts = register_contact(contacts, "Alice", "0987654321")
# Result: {"Alice": "0987654321"}

# 2. Invalid Phone Number (Raises InvalidPhoneNumberError)
try:
    contacts = register_contact(contacts, "Bob", "123-456-789")
except InvalidPhoneNumberError as e:
    print(e)  # Output: Phone number must contain digits only.

# 3. Invalid Name (Raises ValueError)
try:
    contacts = register_contact(contacts, "Bob123", "9876543210")
except ValueError as e:
    print(e)  # Output: Contact name must be a non-empty alphabetic string.

```
---

## Medium Assignments
## Assignment 3: Course Feedback Compiler & Sanitizer

Scenario
Student feedback records contain ratings from 1 to 5 stars. Due to raw data entry issues, the feedback database has some course entries with list values that are empty, or lists containing invalid elements (such as string annotations like "Excellent" or None values).

## Problem Description
Write a function compile_feedback(ratings_dict) that processes course feedback:

The parameter ratings_dict is a dictionary where keys are course names (strings) and values are lists of ratings (which should be numeric but may contain invalid types).
The function must return a dictionary mapping each course name to its average rating, rounded to 2 decimal places.
Implement the following error handling criteria:
For each rating inside a course's list, attempt to convert it to a float. If a rating cannot be converted (throws a ValueError or TypeError), catch the exception, print a warning: "Warning: Invalid rating value '<val>' in course '<course>' skipped.", and continue processing the rest of the list.
If a course has no valid ratings (the list is empty or contains no convertible numbers), computing the average will trigger a division-by-zero error. Catch ZeroDivisionError, print a warning: "Warning: No valid ratings found for course '<course>'. Rating set to 0.0.", and assign the course an average rating of 0.0.
**Sample Input**:
feedback_data = {
    "Python Programming": [5, 4, "4", "Great", 5],
    "Machine Learning": [],
    "Deep Learning": ["Good", "Average", None]
}
**Expected Output**
Console Warnings Printed:

```
text

Warning: Invalid rating value 'Great' in course 'Python Programming' skipped.
Warning: No valid ratings found for course 'Machine Learning'. Rating set to 0.0.
Warning: Invalid rating value 'Good' in course 'Deep Learning' skipped.
Warning: Invalid rating value 'Average' in course 'Deep Learning' skipped.
Warning: Invalid rating value 'None' in course 'Deep Learning' skipped.
Warning: No valid ratings found for course 'Deep Learning'. Rating set to 0.0.
Returned Dictionary:

{
    "Python Programming": 4.5,
    "Machine Learning": 0.0,
    "Deep Learning": 0.0
}

```



