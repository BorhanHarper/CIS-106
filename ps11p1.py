
# Borhan Vishlaghi
# 03/25/2026

def get_input():
    return input("Enter first and last name: ")

def process_name(full_name):
    full_name = full_name.strip()

    parts = full_name.split()

    if len(parts) != 2:
        return None

    first = parts[0]
    last = parts[1]

    result = last + ", " + first[0].upper() + "."
    return result

def display_output(result):
    if result is None:
        print("Invalid input")
    else:
        print(result)


name = get_input()
result = process_name(name)
display_output(result)