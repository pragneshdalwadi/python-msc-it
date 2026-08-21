def calculate_result(student):

    total = (
        student["subject1"]
        + student["subject2"]
        + student["subject3"]
        + student["subject4"]
        + student["subject5"]
    )

    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    student["total"] = total
    student["percentage"] = percentage
    student["grade"] = grade