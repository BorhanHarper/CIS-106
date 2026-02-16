# Borhan Vishlaghi – 02/15/2026

start_value = int(input("Enter start value: "))
stop_value = int(input("Enter stop value: "))
increment_value = int(input("Enter increment value: "))

current_value = start_value

while current_value <= stop_value:
    print(current_value)
    current_value = current_value + increment_value