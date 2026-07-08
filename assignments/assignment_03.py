"""
Assignment 3: Conditional Statements
Test your understanding of if, elif, and else statements.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.checker import Checker, run_assignment


@run_assignment
def assignment_1():
    """
    Assignment 1: Simple if statement.
    
    Task: Write code that checks if a number is positive.
    - If positive, set result to "positive"
    - Otherwise, set result to "not positive"
    """
    
    checker = Checker("Assignment 3.1: Simple If Statement")
    
    # YOUR CODE HERE:
    number = 10
    if number > 0:
        result = "positive"
    else:
        result = "not positive"
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(result, "positive", "10 should be positive")
    
    # Test with negative number
    number = -5
    if number > 0:
        result = "positive"
    else:
        result = "not positive"
    
    checker.test_value(result, "not positive", "-5 should be not positive")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_2():
    """
    Assignment 2: If-elif-else statement.
    
    Task: Create a grade checker.
    - score >= 90: grade = "A"
    - score >= 80: grade = "B"
    - score >= 70: grade = "C"
    - score < 70: grade = "F"
    """
    
    checker = Checker("Assignment 3.2: If-Elif-Else Statement")
    
    def get_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        else:
            return "F"
    
    # TESTS
    checker.test_value(get_grade(95), "A", "95 should get grade A")
    checker.test_value(get_grade(85), "B", "85 should get grade B")
    checker.test_value(get_grade(75), "C", "75 should get grade C")
    checker.test_value(get_grade(65), "F", "65 should get grade F")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_3():
    """
    Assignment 3: Nested if statements.
    
    Task: Check if someone can drive.
    - Must be 18 or older AND have a license
    - Set can_drive to True or False accordingly
    """
    
    checker = Checker("Assignment 3.3: Nested If Statements")
    
    # Test case 1: 20 years old with license
    age = 20
    has_license = True
    
    if age >= 18:
        if has_license:
            can_drive = True
        else:
            can_drive = False
    else:
        can_drive = False
    
    checker.test_value(can_drive, True, "20 year old with license can drive")
    
    # Test case 2: 17 years old with license
    age = 17
    has_license = True
    
    if age >= 18:
        if has_license:
            can_drive = True
        else:
            can_drive = False
    else:
        can_drive = False
    
    checker.test_value(can_drive, False, "17 year old cannot drive")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_4():
    """
    Assignment 4: Logical operators in conditionals.
    
    Task: Check if a number is even AND positive.
    """
    
    checker = Checker("Assignment 3.4: Logical Operators")
    
    def is_even_and_positive(num):
        if num > 0 and num % 2 == 0:
            return True
        else:
            return False
    
    # TESTS
    checker.test_value(is_even_and_positive(4), True, "4 is even and positive")
    checker.test_value(is_even_and_positive(3), False, "3 is not even")
    checker.test_value(is_even_and_positive(-4), False, "-4 is not positive")
    
    checker.print_results()
    return checker.results[-1].passed


if __name__ == "__main__":
    print("ASSIGNMENT 3: CONDITIONAL STATEMENTS")
    print("=" * 60)
    
    print("\nRunning Assignment 1...")
    assignment_1()
    
    print("\nRunning Assignment 2...")
    assignment_2()
    
    print("\nRunning Assignment 3...")
    assignment_3()
    
    print("\nRunning Assignment 4...")
    assignment_4()
