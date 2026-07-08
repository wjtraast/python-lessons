"""
Assignment 1: Variables and Data Types
Test your understanding of variables, data types, and naming conventions.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.checker import Checker, run_assignment


@run_assignment
def assignment_1():
    """
    Assignment 1: Create and assign variables.
    
    Tasks:
    1. Create a variable called 'student_name' and assign your name
    2. Create a variable called 'age' and assign a number
    3. Create a variable called 'is_student' and assign True
    4. Create a variable called 'height' and assign a decimal number
    """
    
    checker = Checker("Assignment 1: Variables and Data Types")
    
    # YOUR CODE HERE (after this line):
    student_name = "Alice"
    age = 16
    is_student = True
    height = 5.5
    # END OF YOUR CODE
    
    # TESTS (automatically check your solution)
    checker.test_type(student_name, str, "student_name should be a string")
    checker.test_value(len(student_name) > 0, True, "student_name should not be empty")
    
    checker.test_type(age, int, "age should be an integer")
    checker.test_condition(age > 0, "age should be positive")
    
    checker.test_type(is_student, bool, "is_student should be a boolean")
    checker.test_value(is_student, True, "is_student should be True")
    
    checker.test_type(height, float, "height should be a float")
    checker.test_condition(height > 0, "height should be positive")
    
    # Print results
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_2():
    """
    Assignment 2: Working with data types.
    
    Tasks:
    1. Create a string variable with a sentence
    2. Create a list with 3 items
    3. Print each variable
    """
    
    checker = Checker("Assignment 2: Data Types")
    
    # YOUR CODE HERE:
    sentence = "I love learning Python"
    items = ["book", "pen", "notebook"]
    # END OF YOUR CODE
    
    # TESTS
    checker.test_type(sentence, str, "sentence should be a string")
    checker.test_condition(len(sentence) > 0, "sentence should not be empty")
    
    checker.test_type(items, list, "items should be a list")
    checker.test_length(items, 3, "items should have 3 elements")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_3():
    """
    Assignment 3: Variable naming conventions.
    
    Create variables with proper names following Python conventions:
    - Use lowercase with underscores for variable names
    - Use meaningful names
    """
    
    checker = Checker("Assignment 3: Variable Naming")
    
    # YOUR CODE HERE:
    my_favorite_color = "blue"
    phone_number = "555-1234"
    is_raining = False
    # END OF YOUR CODE
    
    # TESTS
    checker.test_type(my_favorite_color, str, "my_favorite_color should be a string")
    checker.test_type(phone_number, str, "phone_number should be a string")
    checker.test_type(is_raining, bool, "is_raining should be a boolean")
    
    checker.print_results()
    return checker.results[-1].passed


if __name__ == "__main__":
    print("ASSIGNMENT 1: VARIABLES AND DATA TYPES")
    print("=" * 60)
    print("\nRunning Assignment 1...")
    assignment_1()
    
    print("\nRunning Assignment 2...")
    assignment_2()
    
    print("\nRunning Assignment 3...")
    assignment_3()
