"""
Assignment 6: Lists and Tuples
Test your understanding of list and tuple operations.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.checker import Checker, run_assignment


@run_assignment
def assignment_1():
    """
    Assignment 1: List creation and access.
    
    Task: Create a list of 5 fruits and access specific elements.
    """
    
    checker = Checker("Assignment 6.1: List Creation")
    
    # YOUR CODE HERE:
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    first = fruits[0]
    last = fruits[-1]
    # END OF YOUR CODE
    
    # TESTS
    checker.test_length(fruits, 5, "List should have 5 fruits")
    checker.test_value(first, "apple", "First fruit should be apple")
    checker.test_value(last, "elderberry", "Last fruit should be elderberry")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_2():
    """
    Assignment 2: List modification.
    
    Task: Start with a list, add an item, remove an item.
    """
    
    checker = Checker("Assignment 6.2: List Modification")
    
    # YOUR CODE HERE:
    colors = ["red", "blue", "green"]
    colors.append("yellow")
    colors.remove("blue")
    # END OF YOUR CODE
    
    # TESTS
    checker.test_length(colors, 3, "List should have 3 colors after modification")
    checker.test_value("yellow" in colors, True, "yellow should be in list")
    checker.test_value("blue" not in colors, True, "blue should not be in list")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_3():
    """
    Assignment 3: List slicing.
    
    Task: Get specific portions of a list using slicing.
    """
    
    checker = Checker("Assignment 6.3: List Slicing")
    
    # YOUR CODE HERE:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first_three = numbers[0:3]
    last_two = numbers[-2:]
    middle = numbers[3:7]
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(first_three, [1, 2, 3], "First three should be [1, 2, 3]")
    checker.test_value(last_two, [9, 10], "Last two should be [9, 10]")
    checker.test_value(middle, [4, 5, 6, 7], "Middle should be [4, 5, 6, 7]")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_4():
    """
    Assignment 4: List operations.
    
    Task: Perform operations like sort, reverse, count.
    """
    
    checker = Checker("Assignment 6.4: List Operations")
    
    # YOUR CODE HERE:
    numbers = [5, 2, 8, 2, 9, 2]
    sorted_nums = sorted(numbers)
    reversed_nums = sorted(numbers, reverse=True)
    count_2 = numbers.count(2)
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(sorted_nums, [2, 2, 2, 5, 8, 9], "Should be sorted")
    checker.test_value(reversed_nums, [9, 8, 5, 2, 2, 2], "Should be sorted in reverse")
    checker.test_value(count_2, 3, "Should count 3 occurrences of 2")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_5():
    """
    Assignment 5: Tuples.
    
    Task: Create and work with tuples (immutable lists).
    """
    
    checker = Checker("Assignment 6.5: Tuples")
    
    # YOUR CODE HERE:
    coordinates = (10, 20)
    x, y = coordinates
    point_list = list(coordinates)
    # END OF YOUR CODE
    
    # TESTS
    checker.test_type(coordinates, tuple, "coordinates should be a tuple")
    checker.test_value(x, 10, "x should be 10")
    checker.test_value(y, 20, "y should be 20")
    checker.test_type(point_list, list, "point_list should be a list")
    checker.test_value(point_list, [10, 20], "point_list should contain [10, 20]")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_6():
    """
    Assignment 6: Sum and max/min of lists.
    
    Task: Calculate sum, maximum, and minimum of a list.
    """
    
    checker = Checker("Assignment 6.6: Sum and Extremes")
    
    # YOUR CODE HERE:
    scores = [85, 92, 78, 95, 88]
    total = sum(scores)
    highest = max(scores)
    lowest = min(scores)
    average = total / len(scores)
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(total, 438, "Sum should be 438")
    checker.test_value(highest, 95, "Highest should be 95")
    checker.test_value(lowest, 78, "Lowest should be 78")
    checker.test_condition(87.5 < average < 87.7, "Average should be around 87.6")
    
    checker.print_results()
    return checker.results[-1].passed


if __name__ == "__main__":
    print("ASSIGNMENT 6: LISTS AND TUPLES")
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
