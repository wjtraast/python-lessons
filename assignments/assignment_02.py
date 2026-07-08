"""
Assignment 2: Basic Operations
Test your understanding of arithmetic, comparison, and logical operations.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.checker import Checker, run_assignment


@run_assignment
def assignment_1():
    """
    Assignment 1: Arithmetic operations.
    
    Tasks:
    1. Add 15 and 10, store result in 'sum_result'
    2. Subtract 5 from 20, store result in 'diff_result'
    3. Multiply 3 and 7, store result in 'product'
    4. Divide 20 by 4, store result in 'quotient'
    """
    
    checker = Checker("Assignment 2.1: Arithmetic Operations")
    
    # YOUR CODE HERE:
    sum_result = 15 + 10
    diff_result = 20 - 5
    product = 3 * 7
    quotient = 20 / 4
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(sum_result, 25, "15 + 10 should equal 25")
    checker.test_value(diff_result, 15, "20 - 5 should equal 15")
    checker.test_value(product, 21, "3 * 7 should equal 21")
    checker.test_value(quotient, 5.0, "20 / 4 should equal 5.0")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_2():
    """
    Assignment 2: Comparison operations.
    
    Create boolean variables with comparisons:
    - is_10_greater_than_5: Check if 10 > 5
    - is_3_equal_to_3: Check if 3 == 3
    - is_20_less_than_10: Check if 20 < 10
    """
    
    checker = Checker("Assignment 2.2: Comparison Operations")
    
    # YOUR CODE HERE:
    is_10_greater_than_5 = 10 > 5
    is_3_equal_to_3 = 3 == 3
    is_20_less_than_10 = 20 < 10
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(is_10_greater_than_5, True, "10 > 5 should be True")
    checker.test_value(is_3_equal_to_3, True, "3 == 3 should be True")
    checker.test_value(is_20_less_than_10, False, "20 < 10 should be False")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_3():
    """
    Assignment 3: Logical operations.
    
    Create boolean variables using AND, OR, NOT:
    - and_result: True AND False
    - or_result: True OR False
    - not_result: NOT True
    """
    
    checker = Checker("Assignment 2.3: Logical Operations")
    
    # YOUR CODE HERE:
    and_result = True and False
    or_result = True or False
    not_result = not True
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(and_result, False, "True AND False should be False")
    checker.test_value(or_result, True, "True OR False should be True")
    checker.test_value(not_result, False, "NOT True should be False")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_4():
    """
    Assignment 4: Modulo and exponent operations.
    
    Tasks:
    1. Find remainder of 17 divided by 5, store in 'remainder'
    2. Calculate 2 to the power of 8, store in 'power_result'
    """
    
    checker = Checker("Assignment 2.4: Modulo and Exponent")
    
    # YOUR CODE HERE:
    remainder = 17 % 5
    power_result = 2 ** 8
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(remainder, 2, "17 % 5 should equal 2")
    checker.test_value(power_result, 256, "2 ** 8 should equal 256")
    
    checker.print_results()
    return checker.results[-1].passed


if __name__ == "__main__":
    print("ASSIGNMENT 2: BASIC OPERATIONS")
    print("=" * 60)
    
    print("\nRunning Assignment 1...")
    assignment_1()
    
    print("\nRunning Assignment 2...")
    assignment_2()
    
    print("\nRunning Assignment 3...")
    assignment_3()
    
    print("\nRunning Assignment 4...")
    assignment_4()
