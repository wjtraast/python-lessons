"""
Lesson 8: File Handling and Strings
Learn how to work with files and manipulate strings.
"""

# STRING OPERATIONS
print("STRING METHODS")
print("=" * 50)

text = "Hello Python World"

print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")

# Find and replace
print(f"Find 'Python': {text.find('Python')}")
print(f"Count 'o': {text.count('o')}")
print(f"Replace 'Python' with 'Java': {text.replace('Python', 'Java')}")


# STRING SPLITTING AND JOINING
print("\nSTRING SPLITTING AND JOINING")
print("=" * 50)

sentence = "Hello World Python"
words = sentence.split()
print(f"Words: {words}")

csv_data = "apple,banana,cherry"
items = csv_data.split(",")
print(f"Items: {items}")

# Joining
joined = " - ".join(["red", "green", "blue"])
print(f"Joined: {joined}")


# STRING CHECKING
print("\nSTRING CHECKING")
print("=" * 50)

email = "alice@example.com"

if "@" in email:
    print("This looks like an email")

if email.endswith(".com"):
    print("This is a .com email")

word = "python"
if word.isalpha():
    print("This contains only letters")

number_str = "12345"
if number_str.isdigit():
    print("This contains only digits")


# STRING STRIPPING
print("\nSTRING STRIPPING")
print("=" * 50)

text = "  Hello World  "
print(f"Original: '{text}'")
print(f"Stripped: '{text.strip()}'")
print(f"Left stripped: '{text.lstrip()}'")
print(f"Right stripped: '{text.rstrip()}'")


# STRING FORMATTING
print("\nSTRING FORMATTING")
print("=" * 50)

name = "Alice"
age = 25
height = 5.75

# F-strings (modern way)
print(f"Name: {name}, Age: {age}, Height: {height:.2f}")

# Format method
print("Name: {}, Age: {}".format(name, age))

# Percentage formatting (old way)
print("Name: %s, Age: %d" % (name, age))


# FILE READING
print("\nFILE READING")
print("=" * 50)

# Example: Reading a file
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# Reading line by line
# with open("example.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# Reading all lines into a list
# with open("example.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)

print("(File reading would be demonstrated with actual files)")


# FILE WRITING
print("\nFILE WRITING")
print("=" * 50)

# Writing to a file
# with open("output.txt", "w") as file:
#     file.write("Hello, World!\n")
#     file.write("This is Python!\n")

# Appending to a file
# with open("output.txt", "a") as file:
#     file.write("New line appended!\n")

print("(File writing would be demonstrated with actual files)")


# PRACTICE WITH FILES
print("\nPRACTICE - FILE OPERATIONS")
print("=" * 50)

# Example: Creating and reading a simple file
import os

# Create a test file
test_file = "test.txt"
with open(test_file, "w") as f:
    f.write("Python is awesome!\n")
    f.write("Let's learn together!\n")

# Read and display
with open(test_file, "r") as f:
    content = f.read()
    print("File content:")
    print(content)

# Count lines
with open(test_file, "r") as f:
    lines = f.readlines()
    print(f"Number of lines: {len(lines)}")

# Clean up
os.remove(test_file)
print("Test file cleaned up.")


# STRING MANIPULATION PRACTICE
print("\nSTRING MANIPULATION PRACTICE")
print("=" * 50)

# Example 1: Password validation
password = "MyPassword123"
is_strong = len(password) >= 8 and any(c.isdigit() for c in password)
print(f"Password '{password}' is strong: {is_strong}")

# Example 2: Parse CSV line
csv_line = "Alice,25,Engineer"
data = csv_line.split(",")
print(f"Name: {data[0]}, Age: {data[1]}, Job: {data[2]}")

# Example 3: Clean user input
user_input = "  hello world  "
cleaned = user_input.strip().lower()
print(f"Cleaned input: '{cleaned}'")

# Example 4: Count words
text = "Python is fun and Python is powerful"
word_count = len(text.split())
python_count = text.lower().count("python")
print(f"Total words: {word_count}")
print(f"'Python' appears: {python_count} times")
