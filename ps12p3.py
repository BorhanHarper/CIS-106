
# Borhan Vishlaghi
# 04/07/2026
# Session 12 Problem 3

names = ["Smith","Brown","Taylor","Anderson","Thomas","Jackson","White","Harris","Martin","Thompson"]

scores = [88,92,75,90,84,79,91,86,95,87]


def find_highest(name_list, score_list):

    high_var = 0
    high_index = 0

    for i in range(len(score_list)):
        if score_list[i] > high_var:
            high_var = score_list[i]
            high_index = i

    print("Highest Score:", name_list[high_index], high_var)


def find_lowest(name_list, score_list):

    low_var = 999
    low_index = 0

    for i in range(len(score_list)):
        if score_list[i] < low_var:
            low_var = score_list[i]
            low_index = i

    print("Lowest Score:", name_list[low_index], low_var)


find_highest(names, scores)
find_lowest(names, scores)
