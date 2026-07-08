"""
Lesson 4: Loops
Learn how to repeat code with for and while loops.
"""

# FOR LOOP - loop a specific number of times
print("FOR LOOP")
print("=" * 50)

for i in range(5):
    print(f"Count: {i}")

print()

# FOR LOOP with range(start, stop, step)
for i in range(1, 6):
    print(f"Number: {i}")

print()

# FOR LOOP with step
for i in range(0, 10, 2):
    print(f"Even number: {i}")

print()

# FOR LOOP with countdown
for i in range(5, 0, -1):
    print(f"Countdown: {i}")
print("Blastoff! 🚀")


# LOOPING THROUGH STRINGS
print("\nLOOPING THROUGH STRINGS")
print("=" * 50)

word = "Python"
for letter in word:
    print(letter)

print()

# LOOPING THROUGH LISTS
print("LOOPING THROUGH LISTS")
print("=" * 50)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}s")

print()

# LOOPING WITH INDEX
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")


# WHILE LOOP - loop while condition is true
print("\nWHILE LOOP")
print("=" * 50)

count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

print()

# WHILE LOOP - user input example
print("WHILE LOOP - USER INPUT")
print("=" * 50)

password = ""
correct_password = "secret123"

# This is a simulation - normally you'd use input()
# password = input("Enter password: ")
# Simulating: if you were to use input() in real code

attempts = 0
while attempts < 3:
    print(f"Attempt {attempts + 1}")
    attempts += 1


# BREAK STATEMENT - exit the loop early
print("\nBREAK STATEMENT")
print("=" * 50)

for i in range(10):
    if i == 5:
        print("Found 5! Stopping...")
        break
    print(i)


# CONTINUE STATEMENT - skip to next iteration
print("\nCONTINUE STATEMENT")
print("=" * 50)

for i in range(5):
    if i == 2:
        print("Skipping 2...")
        continue
    print(f"Number: {i}")


# NESTED LOOPS
print("\nNESTED LOOPS")
print("=" * 50)

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}", end="  ")
    print()

print()

# Pattern with nested loops
for i in range(1, 4):
    for j in range(i):
        print("*", end="")
    print()


# LOOP WITH ENUMERATE
print("\nLOOP WITH ENUMERATE")
print("=" * 50)

animals = ["cat", "dog", "bird"]
for index, animal in enumerate(animals):
    print(f"{index}: {animal}")


# PRACTICE
print("\nPRACTICE")
print("=" * 50)

# Example 1: Print numbers 1 to 10
print("Numbers 1 to 10:")
for num in range(1, 11):
    print(num, end=" ")
print()

# Example 2: Sum numbers
total = 0
for i in range(1, 6):
    total += i
print(f"\nSum of 1 to 5: {total}")

# Example 3: Times table
print("\nTimes table for 3:")
for i in range(1, 11):
    print(f"3 x {i} = {3 * i}")

# Example 4: Count to 10 with while loop
print("\nCountdown from 3:")
count = 3
while count > 0:
    print(count)
    count -= 1
print("Go!")
