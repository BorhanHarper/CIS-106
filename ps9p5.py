# Borhan Vishlaghi – 03/13/2026

def assessed_value(county, market):

    if county == "Cook":
        percent = 0.90
    elif county == "DuPage":
        percent = 0.80
    elif county == "McHenry":
        percent = 0.75
    elif county == "Kane":
        percent = 0.60
    else:
        percent = 0.70

    assessed = market * percent

    return assessed

total_market = 0
total_assessed = 0

choice = "Yes"

while choice == "Yes":

    county = input("Enter county: ")
    market = float(input("Enter market value: "))

    value = assessed_value(county, market)

    print("Assessed value:", value)

    total_market += market
    total_assessed += value

    choice = input("Continue? (Yes/No): ")

print("Total Market Value:", total_market)
print("Total Assessed Value:", total_assessed)