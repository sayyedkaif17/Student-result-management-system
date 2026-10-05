import numpy as np

students = []

def add_student():
    name = input("Enter Student Name: ")

    python_marks = int(input("Enter Python Marks: "))
    math_marks = int(input("Enter Math Marks: "))
    english_marks = int(input("Enter English Marks: "))

    marks = np.array([python_marks, math_marks, english_marks])

    total = np.sum(marks)
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"

    student = {
        "Name": name,
        "Total": total,
        "Percentage": round(percentage, 2),
        "Grade": grade
    }

    students.append(student)

    print("\nStudent Added Successfully!")

def view_students():
    if len(students) == 0:
        print("\nNo Student Records Found!")
        return

    print("\n----- STUDENT RESULTS -----")

    for s in students:
        print(f"""
Name       : {s['Name']}
Total      : {s['Total']}
Percentage : {s['Percentage']}%
Grade      : {s['Grade']}
----------------------------
""")

def search_student():
    search_name = input("Enter Student Name to Search: ")

    found = False

    for s in students:
        if s["Name"].lower() == search_name.lower():
            print("\nStudent Found!")
            print(f"""
Name       : {s['Name']}
Total      : {s['Total']}
Percentage : {s['Percentage']}%
Grade      : {s['Grade']}
""")
            found = True
            break

    if not found:
        print("Student Not Found!")

while True:
    print("""
===== STUDENT RESULT MANAGEMENT SYSTEM =====

1. Add Student
2. View All Students
3. Search Student
4. Exit
""")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")