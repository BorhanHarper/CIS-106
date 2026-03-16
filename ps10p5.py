# Borhan Vishlaghi
# 02/15/2026

total_amount = 0
tax_amount = 0


def compute_total_and_tax(quantity_value, unit_price):

    global total_amount
    global tax_amount

    total_amount = quantity_value * unit_price
    tax_amount = total_amount * 0.07


quantity_value = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))

compute_total_and_tax(quantity_value, unit_price)

print("Total:", total_amount)
print("Tax:", tax_amount)