def calculate_result(student):

    # ==========================================
    # CALCULATE TOTAL
    # ==========================================

    student["total"] = (
        student["subject1"]
        + student["subject2"]
        + student["subject3"]
        + student["subject4"]
        + student["subject5"]
    )


    # ==========================================
    # CALCULATE PERCENTAGE
    # ==========================================

    student["percentage"] = student["total"] / 5


    # ==========================================
    # CALCULATE GRADE
    # ==========================================

    if student["percentage"] >= 90:

        student["grade"] = "A+"

    elif student["percentage"] >= 80:

        student["grade"] = "A"

    elif student["percentage"] >= 70:

        student["grade"] = "B"

    elif student["percentage"] >= 60:

        student["grade"] = "C"

    elif student["percentage"] >= 50:

        student["grade"] = "D"

    else:

        student["grade"] = "F"


def add_rank(students):

    # ==========================================
    # ASSIGN RANK
    # ==========================================

    for i in range(len(students)):

        if (
            i > 0
            and students[i]["total"] == students[i - 1]["total"]
        ):

            students[i]["rank"] = students[i - 1]["rank"]

        else:

            students[i]["rank"] = i + 1


def display_result(students):

    # ==========================================
    # DISPLAY RESULT
    # ==========================================

    print()

    print("=" * 90)

    print("                         STUDENT RESULT")

    print("=" * 90)


    # ==========================================
    # HEADING
    # ==========================================

    print(
        f"{'Rank':<8}"
        f"{'Roll No':<12}"
        f"{'Name':<20}"
        f"{'Total':<12}"
        f"{'Percentage':<15}"
        f"{'Grade'}"
    )

    print("-" * 90)


    # ==========================================
    # DISPLAY STUDENTS
    # ==========================================

    for student in students:

        print(
            f"{student['rank']:<8}"
            f"{student['roll_no']:<12}"
            f"{student['name']:<20}"
            f"{student['total']:<12.2f}"
            f"{student['percentage']:<15.2f}"
            f"{student['grade']}"
        )


    print("=" * 90)
