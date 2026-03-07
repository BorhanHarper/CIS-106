# Borhan Vishlaghi – 03/07/2026

def get_rate(job_code):

    if job_code == "L":
        return 25
    elif job_code == "A":
        return 30
    elif job_code == "J":
        return 50

total_gross = 0
choice = "Yes"

while choice == "Yes":

    lname = input("Enter last name: ")
    job_code = input("Enter job code (L/A/J): ")
    hours = float(input("Enter hours worked: "))

    rate = get_rate(job_code)

    if hours > 40:
        gross = (40 * rate) + ((hours - 40) * rate * 1.5)
    else:
        gross = hours * rate

    print("Last Name:", lname)
    print("Gross Pay:", gross)

    total_gross = total_gross + gross

    choice = input("Do you want to continue? (Yes/No): ")

print("Total Gross Pay:", total_gross)