
# Borhan Vishlaghi
# 04/07/2026
# Session 12 Problem 1

names = ["Smith","Brown","Taylor","Anderson","Thomas","Jackson","White","Harris","Martin","Thompson"]

def display_names(name_list):
    for name in name_list:
        print(name)

def display_reverse(name_list):
    for name in reversed(name_list):
        print(name)


print("Names:")
display_names(names)

print("\nNames in Reverse:")
display_reverse(names)