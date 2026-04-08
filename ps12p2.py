
# Borhan Vishlaghi
# 04/07/2026
# Session 12 Problem 2

names = ["Smith","Brown","Taylor","Anderson","Thomas","Jackson","White","Harris","Martin","Thompson"]

scores = [88,92,75,90,84,79,91,86,95,87]


def display_data(name_list, score_list):

    for i in range(len(name_list)):
        print(name_list[i], score_list[i])


def display_reverse(name_list, score_list):

    for i in range(len(name_list)-1, -1, -1):
        print(name_list[i], score_list[i])


print("Names and Scores:")
display_data(names, scores)

print("\nReverse Order:")
display_reverse(names, scores)
