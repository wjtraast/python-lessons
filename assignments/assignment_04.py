"""
Assignment 4: Loops
Test your understanding of for and while loops.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.checker import Checker, run_assignment


@run_assignment
def assignment_1():
    """
    Assignment 1: For loop basics.
    
    Task: Use a for loop to create a list of numbers from 1 to 5.
    """
    
    checker = Checker("Assignment 4.1: For Loop Basics")
    
    # YOUR CODE HERE:
    numbers = []
    for i in range(1, 6):
        numbers.append(i)
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(numbers, [1, 2, 3, 4, 5], "numbers should be [1, 2, 3, 4, 5]")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_2():
    """
    Assignment 2: For loop with string.
    
    Task: Count vowels in a word using a loop.
    """
    
    checker = Checker("Assignment 4.2: Count Vowels")
    
    # YOUR CODE HERE:
    word = "hello"
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for letter in word:
        if letter in vowels:
            vowel_count += 1
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(vowel_count, 2, "hello has 2 vowels (e, o)")
    
    # Test with another word
    word = "python"
    vowel_count = 0
    for letter in word:
        if letter in vowels:
            vowel_count += 1
    
    checker.test_value(vowel_count, 1, "python has 1 vowel (o)")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_3():
    """
    Assignment 3: While loop.
    
    Task: Use a while loop to sum numbers from 1 to 10.
    """
    
    checker = Checker("Assignment 4.3: While Loop")
    
    # YOUR CODE HERE:
    total = 0
    counter = 1
    while counter <= 10:
        total += counter
        counter += 1
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(total, 55, "Sum of 1 to 10 should be 55")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_4():
    """
    Assignment 4: Loop with break statement.
    
    Task: Find the first number divisible by 7 in range 1-50.
    """
    
    checker = Checker("Assignment 4.4: Break Statement")
    
    # YOUR CODE HERE:
    result = None
    for num in range(1, 51):
        if num % 7 == 0:
            result = num
            break
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(result, 7, "First number divisible by 7 is 7")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_5():
    """
    Assignment 5: Nested loops.
    
    Task: Create a multiplication table (2x2).
    Result should be [[1,2], [2,4], [1,3], [2,6]]
    """
    
    checker = Checker("Assignment 4.5: Nested Loops")
    
    # YOUR CODE HERE:
    table = []
    for i in range(1, 3):
        for j in range(1, 3):
            table.append([i, j*i])
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(table, [[1, 1], [1, 2], [2, 1], [2, 2]], "Should create multiplication table")
    checker.test_length(table, 4, "Table should have 4 rows")
    
    checker.print_results()
    return checker.results[-1].passed


if __name__ == "__main__":
    print("ASSIGNMENT 4: LOOPS")
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
