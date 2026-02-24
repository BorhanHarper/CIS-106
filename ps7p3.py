# Borhan Vishlaghi – 02/24/2026

file = open("employees.txt","r")

total_bonus = 0

while True:

    name = file.readline().strip()

    if name == "":
        break

    salary = float(file.readline())

    if salary >= 100000:
        rate = 0.20

    elif salary >= 50000:
        rate = 0.15

    else:
        rate = 0.10

    bonus = salary * rate

    total_bonus = total_bonus + bonus

    print(name, salary, bonus)

file.close()

print("Total Bonus:", total_bonus)