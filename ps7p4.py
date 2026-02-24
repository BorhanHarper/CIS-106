# Borhan Vishlaghi – 02/24/2026

file = open("orders.txt","r")

total = 0
count = 0

while True:

    item = file.readline().strip()

    if item == "":
        break

    quantity = int(file.readline())
    price = float(file.readline())

    extended = quantity * price

    total = total + extended
    count = count + 1

    print(item, quantity, price, extended)

file.close()

average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)