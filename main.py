#!/usr/bin/env python3
"""
Python Lessons - Interactive Learning System
A fun and interactive way to learn Python!

Author: Your Python Learning System
Date: 2024
"""

import os
import sys
import subprocess
from pathlib import Path


def clear_screen():
    """Clear the terminal screen."""
    os.system("clear" if os.name == "posix" else "cls")


def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 70)
    print(f" {title:^66} ")
    print("=" * 70 + "\n")


def print_menu(options, title="Menu"):
    """Print a formatted menu."""
    print_header(title)
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    print(f"\n  0. Back\n")


def run_lesson(lesson_num):
    """Run a lesson file."""
    lesson_file = f"lessons/lesson_{lesson_num:02d}_*.py"
    
    # Find the lesson file
    lesson_files = Path("lessons").glob(f"lesson_{lesson_num:02d}_*.py")
    lesson_files = list(lesson_files)
    
    if lesson_files:
        print_header(f"Lesson {lesson_num}")
        try:
            subprocess.run([sys.executable, str(lesson_files[0])], check=False)
        except Exception as e:
            print(f"Error running lesson: {e}")
        input("\nPress Enter to continue...")
    else:
        print(f"Lesson {lesson_num} not found!")
        input("\nPress Enter to continue...")


def run_assignment(assignment_num):
    """Run an assignment file."""
    assignment_file = Path(f"assignments/assignment_{assignment_num:02d}.py")
    
    if assignment_file.exists():
        print_header(f"Assignment {assignment_num}")
        try:
            subprocess.run([sys.executable, str(assignment_file)], check=False)
        except Exception as e:
            print(f"Error running assignment: {e}")
        input("\nPress Enter to continue...")
    else:
        print(f"Assignment {assignment_num} not found!")
        input("\nPress Enter to continue...")


def show_lessons_menu():
    """Show lessons menu."""
    while True:
        lessons = [
            "Variables and Data Types",
            "Basic Operations and Math",
            "Conditional Statements (if/else)",
            "Loops (for/while)",
            "Functions",
            "Lists and Tuples",
            "Dictionaries",
            "Files and Strings"
        ]
        
        print_menu(lessons, "📚 LESSONS")
        choice = input("Choose a lesson (0 to go back): ").strip()
        
        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(lessons):
            run_lesson(int(choice))
        else:
            print("Invalid choice! Please try again.")
            input("Press Enter to continue...")


def show_assignments_menu():
    """Show assignments menu."""
    while True:
        assignments = [
            "Variables and Data Types",
            "Basic Operations",
            "Conditional Statements",
            "Loops",
            "Functions",
            "Lists and Tuples",
            "Dictionaries",
            "Strings and File Handling"
        ]
        
        print_menu(assignments, "✅ ASSIGNMENTS - Practice What You Learned!")
        choice = input("Choose an assignment (0 to go back): ").strip()
        
        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(assignments):
            run_assignment(int(choice))
        else:
            print("Invalid choice! Please try again.")
            input("Press Enter to continue...")


def show_progress_tips():
    """Show learning tips and progress."""
    print_header("💡 LEARNING TIPS")
    
    tips = [
        "1. Start with Lesson 1 and work your way up gradually",
        "2. Read the lesson code carefully and understand each concept",
        "3. Complete the assignment after each lesson",
        "4. Don't worry if you don't pass all tests the first time!",
        "5. Review the lesson again if you get stuck on an assignment",
        "6. Try to understand WHY the tests pass or fail",
        "7. Once you pass an assignment, try to modify it and experiment!",
        "8. Ask questions and explore Python more on your own!"
    ]
    
    for tip in tips:
        print(f"  {tip}")
    
    print("\n")
    input("Press Enter to continue...")


def show_learning_path():
    """Show the recommended learning path."""
    print_header("🎯 RECOMMENDED LEARNING PATH")
    
    path = [
        "Week 1: Lesson 1 (Variables) → Assignment 1",
        "        Lesson 2 (Operations) → Assignment 2",
        "",
        "Week 2: Lesson 3 (Conditionals) → Assignment 3",
        "        Lesson 4 (Loops) → Assignment 4",
        "",
        "Week 3: Lesson 5 (Functions) → Assignment 5",
        "        Lesson 6 (Lists) → Assignment 6",
        "",
        "Week 4: Lesson 7 (Dictionaries) → Assignment 7",
        "        Lesson 8 (Files & Strings) → Assignment 8",
        "",
        "After completing all lessons and assignments, you'll have a solid",
        "foundation in Python programming! 🚀"
    ]
    
    for line in path:
        print(f"  {line}")
    
    print("\n")
    input("Press Enter to continue...")


def show_main_menu():
    """Show main menu."""
    while True:
        clear_screen()
        print("\n" + "=" * 70)
        print(r"""
        
        🐍 PYTHON LESSONS - LEARN PYTHON IN FUN AND QUICK STEPS! 🐍
        
        """)
        print("=" * 70 + "\n")
        
        menu_options = [
            "📚 Browse Lessons",
            "✅ Practice Assignments",
            "🎯 View Learning Path",
            "💡 Learning Tips",
            "ℹ️  About This System",
            "🚪 Exit"
        ]
        
        for i, option in enumerate(menu_options, 1):
            print(f"  {i}. {option}")
        
        print(f"\n")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            clear_screen()
            show_lessons_menu()
        elif choice == "2":
            clear_screen()
            show_assignments_menu()
        elif choice == "3":
            clear_screen()
            show_learning_path()
        elif choice == "4":
            clear_screen()
            show_progress_tips()
        elif choice == "5":
            clear_screen()
            show_about()
        elif choice == "6":
            print("\n✨ Thanks for learning Python! Keep coding! ✨\n")
            break
        else:
            print("Invalid choice! Please try again.")
            input("Press Enter to continue...")


def show_about():
    """Show about information."""
    print_header("ℹ️  ABOUT THIS LEARNING SYSTEM")
    
    about_text = [
        "This Python Learning System is designed to help beginners",
        "learn Python in simple, fun, and quick steps.",
        "",
        "FEATURES:",
        "  ✓ 8 Progressive Lessons (from basics to file handling)",
        "  ✓ 8 Interactive Assignments with self-correcting tests",
        "  ✓ Instant feedback on your code",
        "  ✓ Recommended learning path",
        "  ✓ Easy-to-follow code examples",
        "",
        "HOW TO USE:",
        "  1. Start with Lesson 1",
        "  2. Read and understand the code",
        "  3. Complete the corresponding assignment",
        "  4. Review feedback from the self-correcting tests",
        "  5. Move to the next lesson when ready",
        "",
        "WHAT YOU'LL LEARN:",
        "  • Variables and data types",
        "  • Arithmetic and logical operations",
        "  • Conditional statements (if/else)",
        "  • Loops (for and while)",
        "  • Functions and code organization",
        "  • Lists and tuples",
        "  • Dictionaries",
        "  • File handling and string manipulation",
        "",
        "GOOD LUCK! 🚀"
    ]
    
    for line in about_text:
        print(f"  {line}")
    
    print("\n")
    input("Press Enter to continue...")


def main():
    """Main entry point."""
    # Check if we're in the right directory
    if not Path("lessons").exists() or not Path("assignments").exists():
        print("Error: This script must be run from the python-lessons directory!")
        print("Current directory:", os.getcwd())
        sys.exit(1)
    
    # Show main menu
    show_main_menu()


if __name__ == "__main__":
    main()
