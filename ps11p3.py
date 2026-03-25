
# Borhan Vishlaghi
# 03/25/2026


def get_input():
    return input("Enter comma-separated values: ")

def process_csv(line):
    items = line.split(",")
    cleaned_items = []

    for item in items:
        cleaned_items.append(item.strip())

    return cleaned_items

def display_output(items):
    for item in items:
        print(item)


line = get_input()
items = process_csv(line)
display_output(items)