
# ============================================
# STUDENT MANAGEMENT SYSTEM
# A Python Mini Project
# ============================================

students = []
next_id = 1


def display_title():
    print("\n" + "=" * 50)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)


def pause():
    input("\nPress Enter to continue...")


def add_student():
    global next_id

    print("\n--- Add New Student ---")

    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    age_text = input("Enter age: ")
    if not age_text.isdigit():
        print("Please enter a valid age.")
        return

    age = int(age_text)
    if age < 1 or age > 120:
        print("Please enter a valid age.")
        return

    course = input("Enter course: ").strip()
    if not course:
        print("Course cannot be empty.")
        return

    email = input("Enter email: ").strip()

    student = {
        "id": next_id,
        "name": name,
        "age": age,
        "course": course,
        "email": email,
        "marks": [],
        "attendance": 0
    }

    students.append(student)
    print("\nStudent added successfully!")
    print("Student ID:", next_id)

    next_id += 1


def display_student(student):
    print("-" * 40)
    print("Student ID:", student["id"])
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])
    print("Email:", student["email"])

    if student["marks"]:
        print("Marks:", student["marks"])
        print("Average:", calculate_average(student))
    else:
        print("Marks: Not entered")

    print("Attendance:", str(student["attendance"]) + "%")
    print("-" * 40)


def view_all_students():
    print("\n--- All Students ---")

    if not students:
        print("No students registered yet.")
        return

    for student in students:
        display_student(student)


def search_student():
    print("\n--- Search Student ---")

    search_id = input("Enter student ID: ")

    if not search_id.isdigit():
        print("Invalid student ID.")
        return

    search_id = int(search_id)

    for student in students:
        if student["id"] == search_id:
            display_student(student)
            return

    print("Student not found.")


def search_by_name():
    print("\n--- Search by Name ---")

    name = input("Enter student name: ").strip().lower()
    found = False

    for student in students:
        if name in student["name"].lower():
            display_student(student)
            found = True

    if not found:
        print("No matching students found.")


def update_student():
    print("\n--- Update Student Details ---")

    student_id = input("Enter student ID: ")

    if not student_id.isdigit():
        print("Invalid ID.")
        return

    student_id = int(student_id)

    for student in students:
        if student["id"] == student_id:
            print("Leave a field empty to keep its current value.")

            name = input("New name: ").strip()
            age_text = input("New age: ").strip()
            course = input("New course: ").strip()
            email = input("New email: ").strip()

            if name:
                student["name"] = name

            if age_text:
                if age_text.isdigit() and 1 <= int(age_text) <= 120:
                    student["age"] = int(age_text)
                else:
                    print("Invalid age; keeping previous age.")

            if course:
                student["course"] = course

            if email:
                student["email"] = email

            print("Student details updated!")
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter student ID: ")

    if not student_id.isdigit():
        print("Invalid ID.")
        return

    student_id = int(student_id)

    for student in students:
        if student["id"] == student_id:
            confirm = input(
                "Are you sure you want to delete this student? (yes/no): "
            ).lower()

            if confirm == "yes":
                students.remove(student)
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled.")
            return

    print("Student not found.")


def add_marks():
    print("\n--- Add Student Marks ---")

    student_id = input("Enter student ID: ")

    if not student_id.isdigit():
        print("Invalid ID.")
        return

    student_id = int(student_id)

    for student in students:
        if student["id"] == student_id:
            mark_text = input("Enter marks out of 100: ")

            try:
                mark = float(mark_text)

                if mark < 0 or mark > 100:
                    print("Marks must be between 0 and 100.")
                    return

                student["marks"].append(mark)
                print("Marks added successfully!")

            except ValueError:
                print("Please enter a valid number.")

            return

    print("Student not found.")


def calculate_average(student):
    if not student["marks"]:
        return 0

    total = sum(student["marks"])
    average = total / len(student["marks"])

    return round(average, 2)


def view_result():
    print("\n--- Student Result ---")

    student_id = input("Enter student ID: ")

    if not student_id.isdigit():
        print("Invalid ID.")
        return

    student_id = int(student_id)

    for student in students:
        if student["id"] == student_id:
            if not student["marks"]:
                print("No marks available.")
                return

            average = calculate_average(student)

            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Average:", average)

            if average >= 90:
                grade = "A+"
            elif average >= 80:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 60:
                grade = "C"
            elif average >= 40:
                grade = "D"
            else:
                grade = "F"

            print("Grade:", grade)

            if average >= 40:
                print("Status: Pass")
            else:
                print("Status: Fail")

            return

    print("Student not found.")


def update_attendance():
    print("\n--- Update Attendance ---")

    student_id = input("Enter student ID: ")

    if not student_id.isdigit():
        print("Invalid ID.")
        return

    student_id = int(student_id)

    for student in students:
        if student["id"] == student_id:
            attendance_text = input(
                "Enter attendance percentage (0-100): "
            )

            try:
                attendance = float(attendance_text)

                if 0 <= attendance <= 100:
                    student["attendance"] = attendance
                    print("Attendance updated!")
                else:
                    print("Attendance must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

            return

    print("Student not found.")


def view_topper():
    print("\n--- Topper Details ---")

    students_with_marks = []

    for student in students:
        if student["marks"]:
            students_with_marks.append(student)

    if not students_with_marks:
        print("No marks available.")
        return

    topper = max(
        students_with_marks,
        key=calculate_average
    )

    print("Congratulations to the topper!")
    display_student(topper)


def show_statistics():
    print("\n--- Student Statistics ---")

    total_students = len(students)
    print("Total students:", total_students)

    if total_students == 0:
        print("No statistics available.")
        return

    total_age = 0
    students_with_marks = 0
    total_averages = 0

    for student in students:
        total_age += student["age"]

        if student["marks"]:
            students_with_marks += 1
            total_averages += calculate_average(student)

    average_age = total_age / total_students

    print("Average student age:", round(average_age, 2))
    print("Students with marks:", students_with_marks)

    if students_with_marks > 0:
        class_average = total_averages / students_with_marks
        print("Class average:", round(class_average, 2))


def list_courses():
    print("\n--- Available Courses ---")

    if not students:
        print("No courses available.")
        return

    courses = []

    for student in students:
        if student["course"] not in courses:
            courses.append(student["course"])

    for course in courses:
        count = 0

        for student in students:
            if student["course"] == course:
                count += 1

        print(course, "-", count, "student(s)")


def low_attendance_report():
    print("\n--- Low Attendance Report ---")

    found = False

    for student in students:
        if student["attendance"] < 75:
            display_student(student)
            found = True

    if not found:
        print("No students have attendance below 75%.")


def menu():
    while True:
        display_title()

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Search Student by Name")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Add Marks")
        print("8. View Result and Grade")
        print("9. Update Attendance")
        print("10. View Topper")
        print("11. Show Statistics")
        print("12. List Courses")
        print("13. Low Attendance Report")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            update_student()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            add_marks()
        elif choice == "8":
            view_result()
        elif choice == "9":
            update_attendance()
        elif choice == "10":
            view_topper()
        elif choice == "11":
            show_statistics()
        elif choice == "12":
            list_courses()
        elif choice == "13":
            low_attendance_report()
        elif choice == "0":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")

        pause()


# Program execution starts here.
if __name__ == "__main__":
    menu()
