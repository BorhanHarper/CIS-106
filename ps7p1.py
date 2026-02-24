# Borhan Vishlaghi – 02/24/2026

principle_amount = float(input("Enter principle amount: "))
interest_rate = float(input("Enter interest rate: "))

total_interest = 0

print("Year   Beginning Balance   Ending Balance")

for year in range(1,6):

    beginning_balance = principle_amount

    interest = principle_amount * interest_rate

    ending_balance = principle_amount + interest

    total_interest = total_interest + interest

    print(year, beginning_balance, ending_balance)

    principle_amount = ending_balance

print("Total Interest:", total_interest)