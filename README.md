# 🐍 Python Lessons - Learn Python in Fun and Quick Steps!

A comprehensive, beginner-friendly Python learning system with interactive lessons, assignments, and self-correcting tests. Perfect for anyone wanting to learn Python from scratch!

## ✨ Features

- **8 Progressive Lessons**: From variables to file handling
- **8 Interactive Assignments**: Practice with instant feedback
- **Self-Correcting Mechanism**: Automatic validation of your code
- **Interactive Menu System**: Easy navigation through content
- **Recommended Learning Path**: Structured progression
- **Clear Examples**: Simple, fun, and practical code examples

## 📁 Directory Structure

```
python-lessons/
├── lessons/                 # Educational lesson files
│   ├── lesson_01_variables.py
│   ├── lesson_02_operations.py
│   ├── lesson_03_conditionals.py
│   ├── lesson_04_loops.py
│   ├── lesson_05_functions.py
│   ├── lesson_06_lists.py
│   ├── lesson_07_dictionaries.py
│   └── lesson_08_files.py
├── assignments/             # Practice assignments with tests
│   ├── assignment_01.py
│   ├── assignment_02.py
│   ├── assignment_03.py
│   ├── assignment_04.py
│   ├── assignment_05.py
│   ├── assignment_06.py
│   ├── assignment_07.py
│   └── assignment_08.py
├── utils/                   # Helper modules
│   ├── checker.py          # Self-correcting mechanism
│   └── runner.py           # Code execution utilities
├── main.py                  # Interactive menu system
└── README.md               # This file
```

## 🚀 Quick Start

### Running the Interactive Menu

The easiest way to get started is using the interactive menu system:

```bash
python main.py
```

This will open an interactive menu where you can:
- Browse lessons
- Practice assignments
- View your learning path
- Get learning tips

### Running Individual Lessons

To run a specific lesson:

```bash
python lessons/lesson_01_variables.py
```

### Running Individual Assignments

To run a specific assignment with self-checking tests:

```bash
python assignments/assignment_01.py
```

## 📚 Lesson Overview

### Lesson 1: Variables and Data Types
Learn about:
- Creating variables
- Data types (int, float, str, bool)
- Variable naming conventions
- Type checking

**Assignment**: Create variables, understand data types

### Lesson 2: Basic Operations and Math
Learn about:
- Arithmetic operations (+, -, *, /, //, %, **)
- Comparison operations (==, !=, <, >, <=, >=)
- Logical operations (and, or, not)
- Operator precedence

**Assignment**: Perform arithmetic and logical operations

### Lesson 3: Conditional Statements
Learn about:
- if, elif, else statements
- Nested conditions
- Logical operators in conditions
- Membership testing (in, not in)

**Assignment**: Write decision-making code with conditions

### Lesson 4: Loops
Learn about:
- for loops with range()
- Looping through strings and lists
- while loops
- break and continue statements
- Nested loops
- enumerate() function

**Assignment**: Practice loops, counting, and iteration

### Lesson 5: Functions
Learn about:
- Defining functions
- Parameters and return values
- Default parameters
- Docstrings
- Variable scope

**Assignment**: Create and use functions

### Lesson 6: Lists and Tuples
Learn about:
- Creating and accessing lists
- List methods (append, extend, remove, sort)
- List slicing
- Tuples (immutable lists)
- Unpacking
- List operations (sum, max, min)

**Assignment**: Work with lists, perform list operations

### Lesson 7: Dictionaries
Learn about:
- Creating dictionaries
- Accessing and modifying values
- Dictionary methods (keys, values, items, get, pop)
- Looping through dictionaries
- Nested dictionaries

**Assignment**: Create and manipulate dictionaries

### Lesson 8: File Handling and Strings
Learn about:
- String methods (upper, lower, split, replace, strip)
- String searching and formatting
- Reading files
- Writing to files
- File operations (append, read, write)

**Assignment**: Work with strings and files

## 💡 How to Use This System

### Step 1: Start with Lesson 1
```bash
python lessons/lesson_01_variables.py
```
- Read the code carefully
- Understand each concept
- Try to predict what the code will do

### Step 2: Complete the Corresponding Assignment
```bash
python assignments/assignment_01.py
```
- Follow the instructions in the comments
- Write your code in the marked section
- The system will automatically check your answers!

### Step 3: Review the Results
The assignment will show you:
- ✓ Passed tests (green checkmarks)
- ✗ Failed tests (with expected vs actual values)
- Overall score

### Step 4: Keep Learning
Once you pass an assignment, move on to the next lesson!

## 🎯 Recommended Learning Path

**Week 1:**
- Monday: Lesson 1 → Assignment 1
- Tuesday: Lesson 2 → Assignment 2

**Week 2:**
- Monday: Lesson 3 → Assignment 3
- Tuesday: Lesson 4 → Assignment 4

**Week 3:**
- Monday: Lesson 5 → Assignment 5
- Tuesday: Lesson 6 → Assignment 6

**Week 4:**
- Monday: Lesson 7 → Assignment 7
- Tuesday: Lesson 8 → Assignment 8

## 📖 Understanding the Self-Correcting System

### How It Works

Each assignment has a built-in checker that automatically tests your code:

```python
from utils.checker import Checker

checker = Checker("Assignment Name")

# Your code goes here
result = 2 + 2

# Tests automatically validate your code
checker.test_value(result, 4, "2 + 2 should equal 4")

# Print results
checker.print_results()
```

### Reading the Results

```
==================================================
Assignment: Assignment 1: Variables and Data Types
==================================================
1. ✓ PASS: student_name should be a string
2. ✓ PASS: student_name should not be empty
3. ✗ FAIL: age should be an integer
   Expected: type int
   Got: type float
4. ✓ PASS: age should be positive

==================================================
Score: 3/4 tests passed
👍 Good job! Keep going!
==================================================
```

## 🔧 What's Inside utils/

### checker.py
Contains the `Checker` class with methods to test:
- `test_value()` - Check if values are equal
- `test_type()` - Check if values are correct type
- `test_length()` - Check if sequences have correct length
- `test_condition()` - Check if boolean conditions are true

### runner.py
Contains utilities for:
- Safe code execution
- Function testing
- Output capture

## 🎓 Tips for Success

1. **Read first, code second**: Always read the lesson before writing code
2. **Understand why**: Make sure you understand why the tests pass or fail
3. **Experiment**: After passing an assignment, try modifying the code
4. **Ask yourself**: "What if I change this? What would happen?"
5. **Don't skip**: Complete assignments even if they seem easy
6. **Review**: Go back to previous lessons if you get stuck
7. **Practice**: Try writing simple programs using what you learned

## 💪 Going Further

After completing all 8 lessons and assignments:

- Try combining concepts (e.g., use loops with lists)
- Build simple projects (calculator, to-do list, etc.)
- Explore Python documentation
- Look at other Python code and try to understand it
- Start learning more advanced topics

## ❓ Frequently Asked Questions

**Q: I got a test wrong. What should I do?**
A: Review the expected vs actual output. Look back at the lesson for the concept you're struggling with.

**Q: Can I run the assignments without using main.py?**
A: Yes! You can run any assignment directly with `python assignments/assignment_XX.py`

**Q: Is the order important?**
A: Yes! Each lesson builds on previous ones. Start with Lesson 1.

**Q: What if I want to experiment with the code?**
A: Great idea! Copy the code, modify it, and see what happens. This is the best way to learn!

**Q: Can I share my solutions?**
A: Absolutely! Show someone else what you learned!

## 📝 License

This learning system is created to help beginners learn Python.

## 🤝 Contributing

Found a bug or have suggestions? Feel free to improve this system!

---

**Happy Learning! 🚀** 

Remember: The best way to learn programming is by doing. Don't just read the lessons - write code, experiment, and have fun!
