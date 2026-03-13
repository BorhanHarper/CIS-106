# Borhan Vishlaghi – 03/13/2026

def ticket_price(miles):

    if miles >= 30:
        price = 12
    elif miles >= 20:
        price = 10
    elif miles >= 10:
        price = 8
    else:
        price = 5

    return price

total_price = 0

choice = "Yes"

while choice == "Yes":

    lname = input("Enter last name: ")
    miles = int(input("Enter miles from Chicago: "))

    price = ticket_price(miles)

    print("Ticket price:", price)

    total_price += price

    choice = input("Continue? (Yes/No): ")

print("Total ticket price:", total_price)