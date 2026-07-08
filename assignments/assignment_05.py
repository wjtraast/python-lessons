"""
Assignment 5: Functions
Test your understanding of function creation and usage.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.checker import Checker, run_assignment


@run_assignment
def assignment_1():
    """
    Assignment 1: Simple function.
    
    Task: Create a function that returns the square of a number.
    Function name: square
    """
    
    checker = Checker("Assignment 5.1: Simple Function")
    
    # YOUR CODE HERE:
    def square(num):
        return num * num
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(square(5), 25, "square(5) should return 25")
    checker.test_value(square(10), 100, "square(10) should return 100")
    checker.test_value(square(-3), 9, "square(-3) should return 9")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_2():
    """
    Assignment 2: Function with multiple parameters.
    
    Task: Create a function that returns the sum of two numbers.
    Function name: add_numbers
    """
    
    checker = Checker("Assignment 5.2: Multiple Parameters")
    
    # YOUR CODE HERE:
    def add_numbers(a, b):
        return a + b
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(add_numbers(3, 4), 7, "add_numbers(3, 4) should return 7")
    checker.test_value(add_numbers(10, -5), 5, "add_numbers(10, -5) should return 5")
    checker.test_value(add_numbers(0, 0), 0, "add_numbers(0, 0) should return 0")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_3():
    """
    Assignment 3: Function that checks conditions.
    
    Task: Create a function that returns True if a number is even, False otherwise.
    Function name: is_even
    """
    
    checker = Checker("Assignment 5.3: Conditional Function")
    
    # YOUR CODE HERE:
    def is_even(num):
        return num % 2 == 0
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(is_even(4), True, "is_even(4) should return True")
    checker.test_value(is_even(7), False, "is_even(7) should return False")
    checker.test_value(is_even(0), True, "is_even(0) should return True")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_4():
    """
    Assignment 4: Function with loop.
    
    Task: Create a function that returns the sum of numbers from 1 to n.
    Function name: sum_to_n
    """
    
    checker = Checker("Assignment 5.4: Function with Loop")
    
    # YOUR CODE HERE:
    def sum_to_n(n):
        total = 0
        for i in range(1, n + 1):
            total += i
        return total
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(sum_to_n(5), 15, "sum_to_n(5) should return 15 (1+2+3+4+5)")
    checker.test_value(sum_to_n(10), 55, "sum_to_n(10) should return 55")
    checker.test_value(sum_to_n(1), 1, "sum_to_n(1) should return 1")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_5():
    """
    Assignment 5: Function with string manipulation.
    
    Task: Create a function that counts vowels in a string.
    Function name: count_vowels
    """
    
    checker = Checker("Assignment 5.5: String Function")
    
    # YOUR CODE HERE:
    def count_vowels(text):
        vowels = "aeiouAEIOU"
        count = 0
        for letter in text:
            if letter in vowels:
                count += 1
        return count
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(count_vowels("hello"), 2, "hello has 2 vowels")
    checker.test_value(count_vowels("aeiou"), 5, "aeiou has 5 vowels")
    checker.test_value(count_vowels("xyz"), 0, "xyz has 0 vowels")
    
    checker.print_results()
    return checker.results[-1].passed


if __name__ == "__main__":
    print("ASSIGNMENT 5: FUNCTIONS")
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
