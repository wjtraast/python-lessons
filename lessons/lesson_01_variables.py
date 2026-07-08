"""
Lesson 1: Variables and Data Types
Learn about basic data types in Python.
"""

# VARIABLES
# A variable is a name that stores a value.

x = 5
name = "Alice"
is_happy = True

print(f"x = {x}")
print(f"name = {name}")
print(f"is_happy = {is_happy}")


# DATA TYPES

# 1. INTEGER (int) - whole numbers
age = 25
count = -10
zero = 0

print(f"\nIntegers: {age}, {count}, {zero}")


# 2. FLOAT (float) - decimal numbers
height = 5.75
pi = 3.14159
temperature = -40.5

print(f"Floats: {height}, {pi}, {temperature}")


# 3. STRING (str) - text
greeting = "Hello, Python!"
name = 'Alice'
empty_string = ""

print(f"Strings: {greeting}, {name}")


# 4. BOOLEAN (bool) - True or False
is_raining = False
is_student = True

print(f"Booleans: {is_raining}, {is_student}")


# NAMING RULES
# Variables must:
# - Start with a letter or underscore _
# - Contain only letters, numbers, and underscores
# - Be case-sensitive (x and X are different)

my_variable = "Good name"
_private = "Starts with underscore"
MY_CONSTANT = "UPPERCASE (usually for constants)"

# These are bad:
# 2bad = "Starts with number" (ERROR!)
# my-var = "Contains dash" (ERROR!)


# TYPE CHECKING
print(f"\nType of x: {type(x)}")
print(f"Type of height: {type(height)}")
print(f"Type of name: {type(name)}")
print(f"Type of is_happy: {type(is_happy)}")


# PRACTICE PROBLEMS:
# Try to understand what will be printed:
print("\n" + "="*50)
print("Practice:")
print("="*50)

animal = "dog"
legs = 4
is_pet = True
weight = 25.5

print(f"Animal: {animal}")
print(f"Legs: {legs}")
print(f"Is pet: {is_pet}")
print(f"Weight: {weight} kg")
