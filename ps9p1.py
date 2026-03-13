# Borhan Vishlaghi – 03/13/2026

def forecast_sales(month, sales):

    if month in ["Jan","Feb","Mar"]:
        percent = 0.10
    elif month in ["Apr","May","Jun"]:
        percent = 0.15
    elif month in ["Jul","Aug","Sep"]:
        percent = 0.20
    else:
        percent = 0.25

    next_sales = sales * (1 + percent)
    return next_sales

choice = "Yes"

while choice == "Yes":

    lname = input("Enter last name: ")
    month = input("Enter month: ")
    sales = float(input("Enter sales: "))

    result = forecast_sales(month, sales)

    print("Next month forecast:", result)

    choice = input("Continue? (Yes/No): ")