"""
Lesson 3: Conditional Statements
Learn how to make decisions with if, elif, and else.
"""

# SIMPLE IF STATEMENT
print("IF STATEMENT")
print("=" * 50)

age = 16

if age >= 18:
    print("You are an adult!")

print("Program continues...")


# IF-ELSE STATEMENT
print("\nIF-ELSE STATEMENT")
print("=" * 50)

score = 75

if score >= 50:
    print("You passed! ✓")
else:
    print("You failed! ✗")


# IF-ELIF-ELSE STATEMENT
print("\nIF-ELIF-ELSE STATEMENT")
print("=" * 50)

temperature = 25

if temperature < 0:
    print("It's freezing! ❄️")
elif temperature < 15:
    print("It's cold! 🧊")
elif temperature < 25:
    print("It's cool! 🌤️")
else:
    print("It's warm! ☀️")


# NESTED IF STATEMENTS
print("\nNESTED IF STATEMENTS")
print("=" * 50)

has_license = True
has_car = True

if has_license:
    if has_car:
        print("You can drive! 🚗")
    else:
        print("You need a car to drive.")
else:
    print("You need a driver's license.")


# COMPARISON OPERATORS IN IF
print("\nCOMPARISON OPERATORS IN IF")
print("=" * 50)

name = "Alice"
favorite_color = "blue"

if name == "Alice":
    print(f"{name} is here!")

if favorite_color != "red":
    print(f"Your favorite color is not red.")

if len(name) > 3:
    print(f"Your name has more than 3 letters.")


# LOGICAL OPERATORS IN IF
print("\nLOGICAL OPERATORS IN IF")
print("=" * 50)

age = 25
has_experience = True

if age >= 18 and has_experience:
    print("You can apply for this job! 💼")

is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("It's time to relax! 😎")

is_sunny = True

if not is_sunny:
    print("Take an umbrella!")
else:
    print("No umbrella needed.")


# CHECKING STRING VALUES
print("\nCHECKING STRING VALUES")
print("=" * 50)

choice = "pizza"

if choice == "pizza":
    print("Great choice! 🍕")
elif choice == "burger":
    print("Yummy! 🍔")
elif choice == "salad":
    print("Healthy! 🥗")
else:
    print("Unknown choice!")


# CHECKING MEMBERSHIP
print("\nCHECKING MEMBERSHIP")
print("=" * 50)

day = "Saturday"
weekend_days = ["Saturday", "Sunday"]

if day in weekend_days:
    print("It's the weekend!")

if "a" in "pizza":
    print("The letter 'a' is in 'pizza'")


# PRACTICE
print("\nPRACTICE")
print("=" * 50)

# Example 1: Grade checker
grade = 85

if grade >= 90:
    print("Grade: A 🌟")
elif grade >= 80:
    print("Grade: B 👍")
elif grade >= 70:
    print("Grade: C 👌")
else:
    print("Grade: F 😞")

# Example 2: Voter eligibility
voter_age = 17

if voter_age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")
