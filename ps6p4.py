# Borhan Vishlaghi – 02/15/2026

loop_answer = input('Do you want to run this program? (Enter "Yes" to continue): ')

employee_count = 0
total_grosspay = 0.0

while loop_answer == "Yes":
    employee_lastname = input("Enter employee last name: ")
    hours_worked = float(input("Enter hours worked: "))
    pay_rate = float(input("Enter rate of pay: "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
    else:
        gross_pay = hours_worked * pay_rate

    print("Employee last name:", employee_lastname)
    print("Gross pay:", gross_pay)

    total_grosspay = total_grosspay + gross_pay
    employee_count = employee_count + 1

    loop_answer = input('Do you want to enter another employee? (Enter "Yes" to continue): ')

if employee_count > 0:
    average_pay = total_grosspay / employee_count
else:
    average_pay = 0.0

print("Total gross pay:", total_grosspay)
print("Number of employees:", employee_count)
print("Average pay:", average_pay)