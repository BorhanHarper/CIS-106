# Borhan Vishlaghi – 03/07/2026

def compute_total(qty, price):
    total = qty * price
    if total > 10000:
        total = total * 0.90   # 10% discount
    return total

total_sum = 0

choice = "Yes"

while choice == "Yes":

    qty = float(input("Enter quantity: "))
    price = float(input("Enter price: "))

    total = compute_total(qty, price)

    print("Quantity:", qty)
    print("Price:", price)
    print("Total:", total)

    total_sum = total_sum + total

    choice = input("Do you want to continue? (Yes/No): ")

print("Total of all extended prices:", total_sum)