def get_student():

    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")

    marks = []

    for i in range(5):
        mark = float(input("Enter Subject Marks: "))
        marks.append(mark)

    student = {
        "roll_no": roll_no,
        "name": name,
        "subject1": marks[0],
        "subject2": marks[1],
        "subject3": marks[2],
        "subject4": marks[3],
        "subject5": marks[4]
    }

    return student