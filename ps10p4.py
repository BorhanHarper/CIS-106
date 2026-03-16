# Borhan Vishlaghi
# 02/15/2026

def compute_bowling_scores(score_one, score_two, score_three, handicap_value):

    average_score = (score_one + score_two + score_three) / 3
    handicap_average = average_score + handicap_value

    return average_score, handicap_average


bowler_lastname = input("Enter bowler last name: ")

score_one = float(input("Enter game score 1: "))
score_two = float(input("Enter game score 2: "))
score_three = float(input("Enter game score 3: "))
handicap_value = float(input("Enter handicap: "))

average_score, handicap_average = compute_bowling_scores(
    score_one, score_two, score_three, handicap_value
)

print("Bowler:", bowler_lastname)
print("Average Score:", average_score)
print("Average with Handicap:", handicap_average)