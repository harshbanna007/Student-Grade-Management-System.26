from functions import (
    add_student,
    update_student,
    delete_student,
    display_all_students,
    search_student
)

from validation import validate_grade
from data import student_grade


def main():
    while True:
        print("\n=== Student Grade Management System ===")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Search Student")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            name = input("Enter student name = ").strip()

            if name:
                grade = validate_grade()
                add_student(student_grade, name, grade)
            else:
                print("Student name cannot be empty!")

        elif choice == 2:
            name = input("Enter student name = ").strip()

            if name:
                grade = validate_grade()
                update_student(student_grade, name, grade)
            else:
                print("Student name cannot be empty!")

        elif choice == 3:
            name = input("Enter student name = ").strip()

            if name:
                delete_student(student_grade, name)
            else:
                print("Student name cannot be empty!")

        elif choice == 4:
            display_all_students(student_grade)

        elif choice == 5:
            name = input("Enter student name = ").strip()

            if name:
                search_student(student_grade, name)
            else:
                print("Student name cannot be empty!")

        elif choice == 6:
            print("Closing the program....")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()