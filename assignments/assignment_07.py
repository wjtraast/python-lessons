"""
Assignment 7: Dictionaries
Test your understanding of dictionary operations.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.checker import Checker, run_assignment


@run_assignment
def assignment_1():
    """
    Assignment 1: Dictionary creation and access.
    
    Task: Create a dictionary about a person and access values.
    """
    
    checker = Checker("Assignment 7.1: Dictionary Creation")
    
    # YOUR CODE HERE:
    person = {"name": "Alice", "age": 25, "city": "Boston"}
    name = person["name"]
    age = person["age"]
    # END OF YOUR CODE
    
    # TESTS
    checker.test_type(person, dict, "person should be a dictionary")
    checker.test_value(name, "Alice", "name should be Alice")
    checker.test_value(age, 25, "age should be 25")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_2():
    """
    Assignment 2: Dictionary modification.
    
    Task: Add new key-value pairs and modify existing ones.
    """
    
    checker = Checker("Assignment 7.2: Dictionary Modification")
    
    # YOUR CODE HERE:
    student = {"name": "Bob", "grade": "B"}
    student["age"] = 20
    student["grade"] = "A"
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(student["age"], 20, "age should be added")
    checker.test_value(student["grade"], "A", "grade should be modified to A")
    checker.test_length(student, 3, "Dictionary should have 3 keys")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_3():
    """
    Assignment 3: Dictionary methods.
    
    Task: Use keys(), values(), and items() methods.
    """
    
    checker = Checker("Assignment 7.3: Dictionary Methods")
    
    # YOUR CODE HERE:
    book = {"title": "Python 101", "author": "John", "year": 2024}
    keys = list(book.keys())
    values = list(book.values())
    items = list(book.items())
    # END OF YOUR CODE
    
    # TESTS
    checker.test_length(keys, 3, "Should have 3 keys")
    checker.test_condition("title" in keys, "title should be in keys")
    checker.test_condition(2024 in values, "2024 should be in values")
    checker.test_length(items, 3, "Should have 3 items")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_4():
    """
    Assignment 4: Looping through dictionaries.
    
    Task: Loop through dictionary and collect keys or values.
    """
    
    checker = Checker("Assignment 7.4: Looping Dictionaries")
    
    # YOUR CODE HERE:
    scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
    names = []
    for name in scores:
        names.append(name)
    
    total = 0
    for score in scores.values():
        total += score
    # END OF YOUR CODE
    
    # TESTS
    checker.test_length(names, 3, "Should have 3 names")
    checker.test_value(total, 274, "Total should be 274")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_5():
    """
    Assignment 5: Dictionary with get() method.
    
    Task: Safely access dictionary values with get().
    """
    
    checker = Checker("Assignment 7.5: Dictionary get() Method")
    
    # YOUR CODE HERE:
    config = {"host": "localhost", "port": 3000}
    host = config.get("host")
    timeout = config.get("timeout", 30)
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(host, "localhost", "host should be localhost")
    checker.test_value(timeout, 30, "timeout should default to 30")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_6():
    """
    Assignment 6: Dictionary operations.
    
    Task: Find max/min values, update dictionaries.
    """
    
    checker = Checker("Assignment 7.6: Dictionary Operations")
    
    # YOUR CODE HERE:
    prices = {"apple": 0.5, "banana": 0.3, "cherry": 1.0}
    most_expensive = max(prices, key=prices.get)
    least_expensive = min(prices, key=prices.get)
    highest_price = prices[most_expensive]
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(most_expensive, "cherry", "cherry is most expensive")
    checker.test_value(least_expensive, "banana", "banana is least expensive")
    checker.test_value(highest_price, 1.0, "cherry price is 1.0")
    
    checker.print_results()
    return checker.results[-1].passed


if __name__ == "__main__":
    print("ASSIGNMENT 7: DICTIONARIES")
    print("=" * 60)
    
    print("\nRunning Assignment 1...")
    assignment_1()
    
    print("\nRunning Assignment 2...")
    assignment_2()
    
    print("\nRunning Assignment 3...")
    assignment_3()
    
    print("\nRunning Assignment 4...")
    assignment_4()
    
    print("\nRunning Assignment 5...")
    assignment_5()
    
    print("\nRunning Assignment 6...")
    assignment_6()
