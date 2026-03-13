# Borhan Vishlaghi – 03/13/2026

def car_price(msrp, make, model, ev):

    if make == "Honda" and model == "Accord":
        percent = 0.10
    elif make == "Toyota" and model == "Rav4":
        percent = 0.15
    elif ev == "Y":
        percent = 0.30
    else:
        percent = 0.05

    discount = msrp * percent
    price = msrp - discount
    tax = price * 0.07

    total = price + tax

    return total

total_msrp = 0
total_sales = 0

choice = "Yes"

while choice == "Yes":

    make = input("Enter make: ")
    model = input("Enter model: ")
    ev = input("Electric vehicle (Y/N): ")
    msrp = float(input("Enter MSRP: "))

    total = car_price(msrp, make, model, ev)

    print("Out the door price:", total)

    total_msrp += msrp
    total_sales += total

    choice = input("Continue? (Yes/No): ")

print("Total MSRP:", total_msrp)
print("Total Sales:", total_sales)