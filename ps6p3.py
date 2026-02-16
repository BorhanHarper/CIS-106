# Borhan Vishlaghi – 02/15/2026

loop_answer = input('Do you want to run this program? (Enter "Yes" to continue): ')

student_count = 0

while loop_answer == "Yes":
    student_lastname = input("Enter student last name: ")
    exam_score1 = float(input("Enter exam 1 score: "))
    exam_score2 = float(input("Enter exam 2 score: "))

    average_score = (exam_score1 + exam_score2) / 2

    print("Student last name:", student_lastname)
    print("Average score:", average_score)

    student_count = student_count + 1
    loop_answer = input('Do you want to enter another student? (Enter "Yes" to continue): ')

print("Total number of students:", student_count)