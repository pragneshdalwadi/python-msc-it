from student import get_student
from result import calculate_result, add_rank, display_result


# ==========================================
# EMPTY LIST
# ==========================================

students = []


# ==========================================
# ASK HOW MANY STUDENTS
# ==========================================

while True:

    try:

        number_of_students = int(
            input("How many student data do you want to enter:")
        )

        if number_of_students <= 0:

            print("Please enter a number greater than 0.")

        else:

            break

    except ValueError:

        print("Please enter a valid number.")


# ==========================================
# GET STUDENT DATA
# ==========================================

for i in range(number_of_students):

    print()

    print("=" * 40)

    print("Student", i + 1)

    print("=" * 40)

    student = get_student()

    students.append(student)


# ==========================================
# CALCULATE RESULT
# ==========================================

for student in students:

    calculate_result(student)


# ==========================================
# SORT BY TOTAL MARKS
# HIGHEST MARKS FIRST
# ==========================================

for i in range(len(students)):

    for j in range(i + 1, len(students)):

        if students[i]["total"] < students[j]["total"]:

            temp = students[i]

            students[i] = students[j]

            students[j] = temp


# ==========================================
# ASSIGN RANK
# ==========================================

add_rank(students)


# ==========================================
# DISPLAY RESULT
# ==========================================

display_result(students)
