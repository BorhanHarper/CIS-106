# Borhan Vishlaghi – 03/07/2026

def batting_average(hits, at_bats):
    return hits / at_bats

count = 0
choice = "Yes"

while choice == "Yes":

    lname = input("Enter player last name: ")
    hits = float(input("Enter number of hits: "))
    at_bats = float(input("Enter number of at bats: "))

    avg = batting_average(hits, at_bats)

    print("Last Name:", lname)
    print("Batting Average:", avg)

    count = count + 1

    choice = input("Do you want to continue? (Yes/No): ")

print("Number of players entered:", count)