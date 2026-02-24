# Borhan Vishlaghi – 02/24/2026

file = open("students.txt","r")

total_tuition = 0
count_students = 0

while True:

    name = file.readline().strip()

    if name == "":
        break

    district = file.readline().strip()

    credits = int(file.readline())

    if district == "I":
        rate = 250

    else:
        rate = 500

    tuition = credits * rate

    total_tuition = total_tuition + tuition
    count_students = count_students + 1

    print(name, credits, tuition)

file.close()

print("Total Tuition:", total_tuition)
print("Number Students:", count_students)