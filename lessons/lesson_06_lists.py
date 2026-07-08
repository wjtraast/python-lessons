"""
Lesson 6: Lists and Tuples
Learn about list and tuple data structures.
"""

# CREATING LISTS
print("CREATING LISTS")
print("=" * 50)

empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

print(f"Empty list: {empty_list}")
print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")


# ACCESSING LIST ELEMENTS
print("\nACCESSING LIST ELEMENTS")
print("=" * 50)

fruits = ["apple", "banana", "cherry", "date"]

print(f"First fruit: {fruits[0]}")
print(f"Second fruit: {fruits[1]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second to last: {fruits[-2]}")

# Slicing
print(f"First two: {fruits[0:2]}")
print(f"Last two: {fruits[-2:]}")
print(f"All except first: {fruits[1:]}")


# LIST LENGTH
print("\nLIST LENGTH")
print("=" * 50)

shopping = ["milk", "eggs", "bread", "butter"]
print(f"Items: {shopping}")
print(f"Number of items: {len(shopping)}")


# ADDING TO LISTS
print("\nADDING TO LISTS")
print("=" * 50)

colors = ["red", "blue"]
print(f"Before: {colors}")

colors.append("green")
print(f"After append: {colors}")

colors.extend(["yellow", "purple"])
print(f"After extend: {colors}")

colors.insert(0, "black")
print(f"After insert at 0: {colors}")


# REMOVING FROM LISTS
print("\nREMOVING FROM LISTS")
print("=" * 50)

items = ["a", "b", "c", "d", "c"]
print(f"Before: {items}")

items.remove("b")  # Remove first occurrence
print(f"After remove 'b': {items}")

items.remove("c")
print(f"After remove 'c': {items}")

popped = items.pop()  # Remove last item
print(f"Popped: {popped}, List: {items}")

popped = items.pop(0)  # Remove first item
print(f"Popped first: {popped}, List: {items}")


# CHECKING IF ITEM IS IN LIST
print("\nCHECKING IF ITEM IS IN LIST")
print("=" * 50)

numbers = [1, 2, 3, 4, 5]

if 3 in numbers:
    print("3 is in the list")

if 10 not in numbers:
    print("10 is not in the list")


# SORTING LISTS
print("\nSORTING LISTS")
print("=" * 50)

scores = [45, 89, 23, 67, 100]
print(f"Original: {scores}")

scores.sort()
print(f"Sorted: {scores}")

scores.sort(reverse=True)
print(f"Sorted (reversed): {scores}")

# Sorting strings
names = ["Charlie", "Alice", "Bob"]
names.sort()
print(f"Names sorted: {names}")


# COPYING LISTS
print("\nCOPYING LISTS")
print("=" * 50)

original = [1, 2, 3]
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

copy1.append(4)
print(f"Original: {original}")
print(f"Copy1: {copy1}")


# LOOPING THROUGH LISTS
print("\nLOOPING THROUGH LISTS")
print("=" * 50)

items = ["book", "pen", "notebook"]

print("Using for loop:")
for item in items:
    print(f"  - {item}")

print("\nUsing enumerate:")
for index, item in enumerate(items):
    print(f"  {index}: {item}")


# TUPLES
print("\nTUPLES - IMMUTABLE LISTS")
print("=" * 50)

# Creating tuples
empty_tuple = ()
single_tuple = (1,)  # Note the comma!
coordinates = (10, 20)
rgb = (255, 128, 0)

print(f"Coordinates: {coordinates}")
print(f"RGB: {rgb}")

# Accessing tuple elements
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")

# Tuples are immutable
print(f"Tuple length: {len(rgb)}")

# You CANNOT modify tuples:
# rgb[0] = 200  # This would cause an error!


# UNPACKING
print("\nUNPACKING")
print("=" * 50)

point = (5, 10)
x, y = point
print(f"Point ({x}, {y})")

rgb = (255, 128, 0)
r, g, b = rgb
print(f"RGB({r}, {g}, {b})")


# PRACTICE
print("\nPRACTICE")
print("=" * 50)

# Example 1: Sum of list
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print(f"Sum of {numbers} = {total}")

# Example 2: Find maximum
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")

# Example 3: List comprehension preview
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Example 4: Joining strings
words = ["Hello", "Python", "World"]
sentence = " ".join(words)
print(f"Sentence: {sentence}")
