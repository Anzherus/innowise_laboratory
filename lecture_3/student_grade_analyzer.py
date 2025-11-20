"""
Student Grade Analyzer
A comprehensive system for managing and analyzing student grades.
"""

from typing import List, Dict, Union

# Constants
MAX_GRADE = 100
MIN_GRADE = 0
EXIT_COMMAND = 'done'

def main() -> None:
    """
    Main function for the Student Grade Analyzer program.
    """
    students = []  # List to store student dictionaries
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_new_student(students)
        elif choice == "2":
            add_grades_for_student(students)
        elif choice == "3":
            show_report(students)
        elif choice == "4":
            find_top_performer(students)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")


def display_menu() -> None:
    """Display the main menu exactly as shown in the example."""
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit program")


def add_new_student(students: List[Dict]) -> None:
    """
    Add a new student to the students list.
    """
    name = input("Enter student name: ").strip()
    
    if not name:
        print("Error: Student name cannot be empty.")
        return
    
    # Check if student already exists
    if any(student["name"].lower() == name.lower() for student in students):
        print(f"Student '{name}' already exists.")
        return
    
    # Create new student dictionary
    new_student = {
        "name": name,
        "grades": []
    }
    students.append(new_student)
    print(f"Student '{name}' added successfully.")


def add_grades_for_student(students: List[Dict]) -> None:
    """
    Add grades for an existing student.
    """
    if not students:
        print("No students available. Please add a student first.")
        return
    
    name = input("Enter student name: ").strip()
    
    # Find the student
    student = next((s for s in students if s["name"].lower() == name.lower()), None)
    
    if not student:
        print(f"Student '{name}' not found.")
        return
    
    print(f"Adding grades for {student['name']}.")
    
    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip().lower()
        
        if grade_input == EXIT_COMMAND:
            break
        
        try:
            grade = int(grade_input)
            if MIN_GRADE <= grade <= MAX_GRADE:
                student["grades"].append(grade)
                print(f"Grade {grade} added successfully.")
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_average(grades: List[int]) -> Union[float, str]:
    """
    Calculate the average of grades.
    """
    if not grades:
        return "N/A"
    
    try:
        average = sum(grades) / len(grades)
        return round(average, 1)
    except ZeroDivisionError:
        return "N/A"


def show_report(students: List[Dict]) -> None:
    """
    Generate and display comprehensive student performance report.
    """
    if not students:
        print("No students available.")
        return
    
    print("\n--- Student Report ---")
    
    valid_averages = []
    
    for student in students:
        avg = calculate_average(student["grades"])
        
        if avg == "N/A":
            print(f"{student['name']}'s average grade is N/A.")
        else:
            print(f"{student['name']}'s average grade is {avg}.")
            valid_averages.append(avg)
    
    if valid_averages:
        max_avg = max(valid_averages)
        min_avg = min(valid_averages)
        overall_avg = sum(valid_averages) / len(valid_averages)
        
        print("---")
        print(f"Max Average: {max_avg}")
        print(f"Min Average: {min_avg}")
        print(f"Overall Average: {overall_avg:.1f}")
    else:
        print("No students with grades to calculate statistics.")


def find_top_performer(students: List[Dict]) -> None:
    """
    Find and display the student with the highest average grade.
    """
    if not students:
        print("No students available.")
        return
    
    students_with_grades = [
        (student, calculate_average(student["grades"]))
        for student in students
        if student["grades"]
    ]
    
    if not students_with_grades:
        print("No students with grades available.")
        return
    
    top_student, top_avg = max(
        students_with_grades,
        key=lambda x: x[1]
    )
    
    print(f"The student with the highest average is {top_student['name']} with a grade of {top_avg}.")


if __name__ == "__main__":
    main()