# Borhan Vishlaghi
# 02/15/2026

def compute_sales_report(sales_amount):

    if sales_amount > 100000:
        commission_amount = sales_amount * 0.10
    else:
        commission_amount = sales_amount * 0.05

    next_year_target = sales_amount * 0.05

    return commission_amount, next_year_target


salesperson_name = input("Enter salesperson last name: ")
sales_amount = float(input("Enter sales amount: "))

commission_amount, next_year_target = compute_sales_report(sales_amount)

print("Salesperson:", salesperson_name)
print("Commission:", commission_amount)
print("Next Year Target:", next_year_target)