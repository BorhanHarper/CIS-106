
# Borhan Vishlaghi
# 03/25/2026

def get_input():
    text = input("Enter text: ")
    chars = int(input("Characters per line: "))
    lines = int(input("Number of lines: "))
    direction = input("Direction (left/right): ")
    return text, chars, lines, direction

def prepare_text(text, chars):
    while len(text) < chars:
        text += text
    return text[:chars]

def shift_left(text):
    return text[1:] + text[0]

def shift_right(text):
    return text[-1] + text[:-1]

def display_output(text, lines, direction):

    for i in range(lines):
        print(text)

        if direction == "left":
            text = shift_left(text)
        else:
            text = shift_right(text)


text, chars, lines, direction = get_input()
text = prepare_text(text, chars)
display_output(text, lines, direction)