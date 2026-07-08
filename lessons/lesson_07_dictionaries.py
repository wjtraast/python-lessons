"""
Lesson 7: Dictionaries
Learn about dictionary data structures.
"""

# CREATING DICTIONARIES
print("CREATING DICTIONARIES")
print("=" * 50)

empty_dict = {}
person = {"name": "Alice", "age": 25, "city": "New York"}
student = {
    "name": "Bob",
    "age": 20,
    "grade": "A",
    "email": "bob@example.com"
}

print(f"Person: {person}")
print(f"Student: {student}")


# ACCESSING VALUES
print("\nACCESSING VALUES")
print("=" * 50)

print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")

# Using .get() method (safer)
print(f"Country: {person.get('country', 'Unknown')}")


# ADDING AND MODIFYING
print("\nADDING AND MODIFYING")
print("=" * 50)

book = {"title": "Python 101", "author": "John Doe"}
print(f"Before: {book}")

book["year"] = 2024
print(f"After adding year: {book}")

book["author"] = "Jane Doe"
print(f"After modifying author: {book}")


# REMOVING FROM DICTIONARIES
print("\nREMOVING FROM DICTIONARIES")
print("=" * 50)

student = {"name": "Charlie", "age": 22, "grade": "B"}
print(f"Before: {student}")

del student["grade"]
print(f"After delete: {student}")

removed = student.pop("age")
print(f"Popped age: {removed}, Dictionary: {student}")


# DICTIONARY KEYS, VALUES, ITEMS
print("\nKEYS, VALUES, ITEMS")
print("=" * 50)

person = {"name": "Alice", "age": 25, "city": "New York"}

print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")


# LOOPING THROUGH DICTIONARIES
print("\nLOOPING THROUGH DICTIONARIES")
print("=" * 50)

car = {"brand": "Toyota", "model": "Camry", "year": 2023}

print("Keys only:")
for key in car:
    print(f"  {key}: {car[key]}")

print("\nUsing .items():")
for key, value in car.items():
    print(f"  {key}: {value}")


# CHECKING IF KEY EXISTS
print("\nCHECKING IF KEY EXISTS")
print("=" * 50)

person = {"name": "Alice", "age": 25}

if "name" in person:
    print("Person has a name")

if "email" not in person:
    print("Person doesn't have an email")


# DICTIONARY METHODS
print("\nDICTIONARY METHODS")
print("=" * 50)

info = {"name": "Bob", "age": 20}

# Update dictionary
info.update({"city": "Boston", "age": 21})
print(f"After update: {info}")

# Clear dictionary
copy_info = info.copy()
copy_info.clear()
print(f"After clear: {copy_info}")

# Length
print(f"Number of items: {len(info)}")


# NESTED DICTIONARIES
print("\nNESTED DICTIONARIES")
print("=" * 50)

school = {
    "students": {
        "alice": {"age": 20, "grade": "A"},
        "bob": {"age": 21, "grade": "B"}
    },
    "location": "Boston"
}

print(f"Alice's grade: {school['students']['alice']['grade']}")


# PRACTICE
print("\nPRACTICE")
print("=" * 50)

# Example 1: Contact information
contact = {
    "name": "Alice Smith",
    "phone": "555-1234",
    "email": "alice@example.com"
}
print(f"Contact: {contact['name']} - {contact['email']}")

# Example 2: Score tracking
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
print(f"Alice's score: {scores['Alice']}")
print(f"Average score: {sum(scores.values()) / len(scores):.2f}")

# Example 3: Finding highest score
highest_student = max(scores, key=scores.get)
print(f"Highest scorer: {highest_student} with {scores[highest_student]} points")
