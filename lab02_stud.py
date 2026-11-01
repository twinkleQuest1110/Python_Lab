
# Student Result Data Validator

# attendance requirement
MIN_ATTENDANCE = 75

# ip student details
name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

# ip marks in five subjects
subjects = ["Python", "Maths", "Englsih", "Physics", "Chemistry"]
marks = []

valid_input = True

for subject in subjects:
    try:
        mark = float(input(f"Enter marks in {subject}: "))

        # checj  marks
        if mark < 0 or mark > 100:
            print("Invalid marks! Marks must be between 0 and 100.")
            valid_input = False
            break

        marks.append(mark)

    except ValueError:
        print("Invalid input! Please enter a nuneric value.")
        valid_input = False
        break

# Taking attendance
if valid_input:
    try:
        attendance = float(input("Enter attendance percentage: "))

        if attendance < 0 or attendance > 100:
            print("Invalid attendance! Enter a value between 0 and 100.")
            valid_input = False

    except ValueError:
        print("Invalid input! Attendance must be numeric.")
        valid_input = False

# Calculating and displaying result
if valid_input:

    total = sum(marks)
    average = total / 5
    percentage = (total / 500) * 100

    # Checking attendance eligibility
    if attendance >= MIN_ATTENDANCE:
        eligibility = "Eligible"
    else:
        eligibility = "Not Eligible"

    print("\n=======---> STUDENT RESULT ==========")
    print("Student Name:  ", name)
    print("Roll Number:   ", roll_number)
    print("Total Marks:", f"{total:.2f} / 500")
    print("Average Marks: ", f"{average:.2f}")
    print("Percentage:", f"{percentage:.2f}%")
    print("Attendance:", f"{attendance:.2f}%")
    print("Attendance Eligibility:", eligibility)

else:
    print("\nStudent record rejected due to invalid input.")
