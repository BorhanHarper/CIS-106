# Borhan Vishlaghi – 03/13/2026

def square_footage(length, width, height):

    sqft = (2 * length * width) + (2 * length * height) + (2 * width * height)

    return sqft

choice = "Yes"

while choice == "Yes":

    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    sqft = square_footage(length,width,height)

    gallons = sqft / 50

    print("Gallons needed:", gallons)

    choice = input("Continue? (Yes/No): ")