"""
Assignment 8: Strings and File Handling
Test your understanding of string operations and basic file handling.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.checker import Checker, run_assignment
import os
import tempfile


@run_assignment
def assignment_1():
    """
    Assignment 1: String methods.
    
    Task: Use string methods like upper(), lower(), split(), etc.
    """
    
    checker = Checker("Assignment 8.1: String Methods")
    
    # YOUR CODE HERE:
    text = "Hello Python World"
    upper_text = text.upper()
    lower_text = text.lower()
    words = text.split()
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(upper_text, "HELLO PYTHON WORLD", "upper() should work")
    checker.test_value(lower_text, "hello python world", "lower() should work")
    checker.test_value(words, ["Hello", "Python", "World"], "split() should work")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_2():
    """
    Assignment 2: String searching and replacing.
    
    Task: Find substrings and replace text.
    """
    
    checker = Checker("Assignment 8.2: String Search and Replace")
    
    # YOUR CODE HERE:
    sentence = "I love Python and Python is great"
    count = sentence.count("Python")
    replaced = sentence.replace("Python", "Java")
    index = sentence.find("great")
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(count, 2, "Python appears 2 times")
    checker.test_condition("Java" in replaced and "Python" not in replaced, "Replace should work")
    checker.test_value(index, 30, "great starts at index 30")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_3():
    """
    Assignment 3: String joining and stripping.
    
    Task: Join strings and remove whitespace.
    """
    
    checker = Checker("Assignment 8.3: Join and Strip")
    
    # YOUR CODE HERE:
    words = ["apple", "banana", "cherry"]
    joined = "-".join(words)
    
    text_with_spaces = "  hello world  "
    stripped = text_with_spaces.strip()
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(joined, "apple-banana-cherry", "join() should work")
    checker.test_value(stripped, "hello world", "strip() should remove spaces")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_4():
    """
    Assignment 4: String checking.
    
    Task: Check string properties like isdigit(), isalpha(), startswith(), etc.
    """
    
    checker = Checker("Assignment 8.4: String Checking")
    
    # YOUR CODE HERE:
    is_digit = "12345".isdigit()
    is_alpha = "hello".isalpha()
    starts_with = "python".startswith("py")
    ends_with = "python".endswith("on")
    # END OF YOUR CODE
    
    # TESTS
    checker.test_value(is_digit, True, "12345 is all digits")
    checker.test_value(is_alpha, True, "hello is all letters")
    checker.test_value(starts_with, True, "python starts with py")
    checker.test_value(ends_with, True, "python ends with on")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_5():
    """
    Assignment 5: String formatting.
    
    Task: Format strings using f-strings and format().
    """
    
    checker = Checker("Assignment 8.5: String Formatting")
    
    # YOUR CODE HERE:
    name = "Alice"
    age = 25
    height = 5.75
    
    formatted1 = f"My name is {name}, I am {age} years old"
    formatted2 = "Height: {:.2f}".format(height)
    # END OF YOUR CODE
    
    # TESTS
    checker.test_condition("Alice" in formatted1 and "25" in formatted1, "f-string should work")
    checker.test_condition("5.75" in formatted2, "format() should work")
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_6():
    """
    Assignment 6: File writing and reading.
    
    Task: Write to a file and read it back.
    """
    
    checker = Checker("Assignment 8.6: File Operations")
    
    # YOUR CODE HERE:
    # Create a temporary file for testing
    test_file = os.path.join(tempfile.gettempdir(), "test_lesson.txt")
    
    # Write to file
    with open(test_file, "w") as f:
        f.write("Python is fun!\n")
        f.write("Let's learn together!\n")
    
    # Read from file
    with open(test_file, "r") as f:
        content = f.read()
    
    with open(test_file, "r") as f:
        lines = f.readlines()
    
    # END OF YOUR CODE
    
    # TESTS
    checker.test_condition("Python is fun" in content, "File should contain written text")
    checker.test_length(lines, 2, "File should have 2 lines")
    checker.test_condition("Let's learn" in lines[1], "Second line should be correct")
    
    # Clean up
    os.remove(test_file)
    
    checker.print_results()
    return checker.results[-1].passed


@run_assignment
def assignment_7():
    """
    Assignment 7: File appending.
    
    Task: Append content to a file.
    """
    
    checker = Checker("Assignment 8.7: File Appending")
    
    # YOUR CODE HERE:
    test_file = os.path.join(tempfile.gettempdir(), "append_test.txt")
    
    # Write initial content
    with open(test_file, "w") as f:
        f.write("Line 1\n")
    
    # Append content
    with open(test_file, "a") as f:
        f.write("Line 2\n")
        f.write("Line 3\n")
    
    # Read all content
    with open(test_file, "r") as f:
        all_lines = f.readlines()
    
    # END OF YOUR CODE
    
    # TESTS
    checker.test_length(all_lines, 3, "File should have 3 lines")
    checker.test_value(all_lines[0].strip(), "Line 1", "First line should be correct")
    checker.test_value(all_lines[2].strip(), "Line 3", "Third line should be correct")
    
    # Clean up
    os.remove(test_file)
    
    checker.print_results()
    return checker.results[-1].passed


if __name__ == "__main__":
    print("ASSIGNMENT 8: STRINGS AND FILE HANDLING")
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
    
    print("\nRunning Assignment 7...")
    assignment_7()
