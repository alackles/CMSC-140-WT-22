# Calculating Grades 

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.


# create a dictionary where:
#  the key is the student name
#  the value is the average of the student's three exam scores
students = {}

with open("/home/acacia/Documents/grades.csv") as f:
    next(f)
    for line in f.readlines:
        name, exam1, exam2, exam3 = line.split()
    student_grades = [exam1, exam2, exam3]
    avg = sum(student_grades)/len(student_grades)
    students["name"] = avg


# create another dictionary where:
#  the key is the student name
#  the value is the student's letter grade 
grades = {}

for student, avg in students.items():
    # this should follow the grading scheme outlined above:
        # 90+	A
        # 80-89	B
        # 70-79	C
        # 60-69	D
        # 0-59	F
    if avg >= 90:
        letter_grade = "A"
    if avg >= 80
        letter_grade = "B"
    if avg >= 69:
        letter_grade = "C'
    if avg <= 69: 
        letter_grade = "D"
    else:
        letter_grade = "F"
    grades[student] = letter_grade

for student, grade in grades.items():

    print("Student: " + student)
    # print the average exam score 
    print("Exam Average: " + students[avg])
    # print the letter grade
    print("Grade: " + grade)

    with open("result.txt", 'w') as f:
        if letter_grade == "F":
            f.write(student, "is failing.")
        else:
            f.write(student, "is passing.")
    