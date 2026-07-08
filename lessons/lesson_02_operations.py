"""
Lesson 2: Basic Operations and Math
Learn arithmetic, comparison, and logical operations.
"""

# ARITHMETIC OPERATIONS
print("ARITHMETIC OPERATIONS")
print("=" * 50)

a = 10
b = 3

# Addition
print(f"{a} + {b} = {a + b}")

# Subtraction
print(f"{a} - {b} = {a - b}")

# Multiplication
print(f"{a} * {b} = {a * b}")

# Division (always gives float)
print(f"{a} / {b} = {a / b}")

# Floor Division (rounds down)
print(f"{a} // {b} = {a // b}")

# Modulo (remainder)
print(f"{a} % {b} = {a % b}")

# Exponent (power)
print(f"{a} ** {b} = {a ** b}")


# COMPARISON OPERATIONS
print("\nCOMPARISON OPERATIONS")
print("=" * 50)

x = 5
y = 8

print(f"{x} == {y} ? {x == y}")  # Equal
print(f"{x} != {y} ? {x != y}")  # Not equal
print(f"{x} < {y} ? {x < y}")   # Less than
print(f"{x} > {y} ? {x > y}")   # Greater than
print(f"{x} <= {y} ? {x <= y}") # Less than or equal
print(f"{x} >= {y} ? {x >= y}") # Greater than or equal


# LOGICAL OPERATIONS
print("\nLOGICAL OPERATIONS")
print("=" * 50)

is_sunny = True
is_warm = False

# AND - both must be True
print(f"is_sunny AND is_warm: {is_sunny and is_warm}")

# OR - at least one must be True
print(f"is_sunny OR is_warm: {is_sunny or is_warm}")

# NOT - reverses the value
print(f"NOT is_sunny: {not is_sunny}")
print(f"NOT is_warm: {not is_warm}")


# OPERATOR PRECEDENCE (order of operations)
print("\nOPERATOR PRECEDENCE")
print("=" * 50)

result1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {result1}  (3*4 is done first)")

result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result2}  (parentheses first)")


# STRING OPERATIONS
print("\nSTRING OPERATIONS")
print("=" * 50)

first_name = "Alice"
last_name = "Smith"

# Concatenation (joining strings)
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# String repetition
print(f"Stars: {'*' * 10}")


# VARIABLE ASSIGNMENT WITH OPERATORS
print("\nVARIABLE ASSIGNMENT WITH OPERATORS")
print("=" * 50)

counter = 5
print(f"counter = {counter}")

counter += 3  # Same as counter = counter + 3
print(f"After += 3: {counter}")

counter -= 2  # Same as counter = counter - 2
print(f"After -= 2: {counter}")

counter *= 2  # Same as counter = counter * 2
print(f"After *= 2: {counter}")


# PRACTICE
print("\nPRACTICE")
print("=" * 50)

# What will these print?
print(f"10 + 5 * 2 = {10 + 5 * 2}")
print(f"True and False = {True and False}")
print(f"5 % 3 = {5 % 3}")
print(f"'Hello' + ' ' + 'World' = {'Hello' + ' ' + 'World'}")
