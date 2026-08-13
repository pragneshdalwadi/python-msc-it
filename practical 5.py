students = []

for i in range(3):

    print("\nStudent", i + 1)

    name = input("Enter Name: ")

    subject1 = int(input("Enter Subject 1 Marks: "))
    subject2 = int(input("Enter Subject 2 Marks: "))
    subject3 = int(input("Enter Subject 3 Marks: "))
    subject4 = int(input("Enter Subject 4 Marks: "))
    subject5 = int(input("Enter Subject 5 Marks: "))

    total = subject1 + subject2 + subject3 + subject4 + subject5

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

    students = students + [[0, name, total, percentage, grade]]


# Sort students for total marks
for i in range(3):
    for j in range(i + 1, 3):

        if students[i][2] < students[j][2]:

            temp = students[i]
            students[i] = students[j]
            students[j] = temp


# Assign ranks
for i in range(3):

    if i > 0 and students[i][2] == students[i - 1][2]:
        students[i][0] = students[i - 1][0]
    else:
        students[i][0] = i + 1


# Display result
print(f"\n{'Rank':<8}{'Name':<15}{'Total':<10}{'Percentage':<15}{'Grade'}")
print("-" * 65)

for student in students:
    print(f"{student[0]:<8}{student[1]:<15}{student[2]:<10}{student[3]:<15.2f}{student[4]}")
