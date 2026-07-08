"""
Lesson 5: Functions
Learn how to create and use functions.
"""

# DEFINING A FUNCTION
print("DEFINING A FUNCTION")
print("=" * 50)

def greet():
    """This is a simple greeting function."""
    print("Hello! Welcome to Python!")

# Calling the function
greet()
greet()  # You can call it multiple times!


# FUNCTION WITH PARAMETERS
print("\nFUNCTION WITH PARAMETERS")
print("=" * 50)

def greet_person(name):
    """Greet a specific person."""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")


# FUNCTION WITH MULTIPLE PARAMETERS
print("\nFUNCTION WITH MULTIPLE PARAMETERS")
print("=" * 50)

def add(a, b):
    """Add two numbers."""
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

add(5, 3)
add(10, 20)


# FUNCTION WITH RETURN VALUE
print("\nFUNCTION WITH RETURN VALUE")
print("=" * 50)

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

result = multiply(4, 5)
print(f"4 * 5 = {result}")

# You can use the return value immediately
print(f"6 * 7 = {multiply(6, 7)}")


# FUNCTION WITH DEFAULT PARAMETERS
print("\nFUNCTION WITH DEFAULT PARAMETERS")
print("=" * 50)

def greet_formal(name="Friend"):
    """Greet someone with a default name."""
    print(f"Good day, {name}!")

greet_formal()
greet_formal("Ms. Smith")


# FUNCTION THAT RETURNS MULTIPLE VALUES
print("\nFUNCTION RETURNING MULTIPLE VALUES")
print("=" * 50)

def get_info():
    """Return multiple values."""
    name = "Alice"
    age = 25
    city = "New York"
    return name, age, city

# Unpacking the returned values
name, age, city = get_info()
print(f"{name} is {age} years old and lives in {city}")


# DOCSTRINGS
print("\nDOCSTRINGS")
print("=" * 50)

def calculate_average(a, b, c):
    """
    Calculate the average of three numbers.
    
    Args:
        a: First number
        b: Second number
        c: Third number
    
    Returns:
        The average of the three numbers
    """
    return (a + b + c) / 3

average = calculate_average(10, 20, 30)
print(f"Average: {average}")


# VARIABLE SCOPE
print("\nVARIABLE SCOPE")
print("=" * 50)

x = "global"  # Global variable

def show_scope():
    y = "local"  # Local variable
    print(f"Inside function: x = {x}, y = {y}")

show_scope()
print(f"Outside function: x = {x}")
# print(y)  # This would cause an error - y doesn't exist here


# FUNCTION THAT MODIFIES LISTS
print("\nFUNCTION WITH LISTS")
print("=" * 50)

def add_to_list(my_list, item):
    """Add an item to a list."""
    my_list.append(item)

colors = ["red", "blue"]
print(f"Before: {colors}")

add_to_list(colors, "green")
print(f"After: {colors}")


# PRACTICE
print("\nPRACTICE")
print("=" * 50)

# Example 1: Simple calculator function
def calculate(a, b, operation):
    """Perform a calculation."""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

print(f"5 + 3 = {calculate(5, 3, 'add')}")
print(f"5 - 3 = {calculate(5, 3, 'subtract')}")
print(f"5 * 3 = {calculate(5, 3, 'multiply')}")
print(f"5 / 3 = {calculate(5, 3, 'divide')}")

# Example 2: Check if number is even
def is_even(num):
    """Check if a number is even."""
    return num % 2 == 0

print(f"\n4 is even: {is_even(4)}")
print(f"7 is even: {is_even(7)}")

# Example 3: Count occurrences
def count_vowels(text):
    """Count vowels in text."""
    vowels = "aeiouAEIOU"
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    return count

print(f"\nVowels in 'Hello World': {count_vowels('Hello World')}")
