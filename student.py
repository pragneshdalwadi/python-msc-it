def get_student():

    # ==========================================
    # ROLL NUMBER
    # ==========================================

    while True:
        try:
            roll_no = int(input("Enter Roll Number: "))

            if roll_no <= 0:
                print("Roll Number must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid Roll Number.")


    # ==========================================
    # NAME
    # ==========================================

    while True:
        name = input("Enter Name: ").strip()

        if name == "":
            print("Name cannot be empty.")
        else:
            break


    # ==========================================
    # SUBJECT MARKS
    # ==========================================

    subject_marks = []

    for i in range(1, 6):

        while True:
            try:
                marks = float(input(f"Enter Subject {i} Marks: "))

                if marks < 0 or marks > 100:
                    print("Marks must be between 0 and 100.")

                else:
                    subject_marks.append(marks)
                    break

            except ValueError:
                print("Please enter valid marks.")


    # ==========================================
    # CREATE STUDENT
    # ==========================================

    student = {

        "roll_no": roll_no,

        "rank": 0,

        "name": name,

        "subject1": subject_marks[0],

        "subject2": subject_marks[1],

        "subject3": subject_marks[2],

        "subject4": subject_marks[3],

        "subject5": subject_marks[4],

        "total": 0,

        "percentage": 0,

        "grade": ""

    }

    return student
