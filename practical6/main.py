from student import get_student
from result import calculate_result

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    student = get_student()
    calculate_result(student)

    students.append(student)

# Sort by total marks
students.sort(key=lambda x: x["total"], reverse=True)

print("\n----- STUDENT RESULT -----")

rank = 1
previous_total = None

for student in students:

    # Same marks = same rank
    if previous_total is not None and student["total"] != previous_total:
        rank = students.index(student) + 1

    print("Rank:", rank)
    print("Roll No:", student["roll_no"])
    print("Name:", student["name"])
    print("Total:", student["total"])
    print("Percentage:", student["percentage"])
    print("Grade:", student["grade"])
    print()

    previous_total = student["total"]