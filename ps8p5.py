# Borhan Vishlaghi – 03/07/2026

def compute_tuition(credits, district):

    if district == "I":
        return credits * 250
    else:
        return credits * 550

total_tuition = 0
choice = "Yes"

while choice == "Yes":

    lname = input("Enter student last name: ")
    credits = float(input("Enter credit hours: "))
    district = input("Enter district code (I/O): ")

    tuition = compute_tuition(credits, district)

    print("Student:", lname)
    print("Tuition Owed:", tuition)

    total_tuition = total_tuition + tuition

    choice = input("Do you want to continue? (Yes/No): ")

print("Total Tuition Owed:", total_tuition)