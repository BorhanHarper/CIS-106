
# Borhan Vishlaghi
# 04/07/2026
# Session 12 Problem 5

names = []
averages = []


def load_file():

    file = open("players.txt")

    for line in file:
        data = line.split()
        names.append(data[0])
        averages.append(float(data[1]))

    file.close()


def search_player(player):

    found = False

    for i in range(len(names)):

        if names[i] == player:
            print(names[i], averages[i])
            found = True

    if not found:
        print("Name not found")


load_file()

while True:

    player = input("Enter last name (or quit): ")

    if player == "quit":
        break

    search_player(player)
