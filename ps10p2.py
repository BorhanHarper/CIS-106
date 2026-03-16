# Borhan Vishlaghi
# 02/15/2026

def compute_scores(score_one, score_two, score_three):

    total_points = score_one + score_two + score_three
    average_score = total_points / 3

    return total_points, average_score


student_lastname = input("Enter student last name: ")

score_one = float(input("Enter exam score 1: "))
score_two = float(input("Enter exam score 2: "))
score_three = float(input("Enter exam score 3: "))

total_points, average_score = compute_scores(score_one, score_two, score_three)

print("Student:", student_lastname)
print("Total Points:", total_points)
print("Average Score:", average_score)