

# Borhan Vishlaghi
# 03/25/2026

def get_input():
    return input("Enter a line of text: ")

def clean_spaces(text):
    return " ".join(text.strip().split())

def reverse_text(text):
    return text[::-1]

def display_output(result):
    print(result)


text = get_input()
cleaned = clean_spaces(text)
reversed_text = reverse_text(cleaned)
display_output(reversed_text)