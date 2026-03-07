# Borhan Vishlaghi – 03/07/2026

def compute_mpg(miles, gallons):
    return miles / gallons

count = 0
choice = "Yes"

while choice == "Yes":

    city = input("Enter destination city: ")
    miles = float(input("Enter miles travelled: "))
    gallons = float(input("Enter gallons used: "))

    mpg = compute_mpg(miles, gallons)

    print("City:", city)
    print("Miles:", miles)
    print("MPG:", mpg)

    count = count + 1

    choice = input("Do you want to continue? (Yes/No): ")

print("Number of trips:", count)