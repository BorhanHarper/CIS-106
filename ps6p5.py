# Borhan Vishlaghi – 02/15/2026

loop_answer = input('Do you want to run this program? (Enter "Yes" to continue): ')

total_discounts = 0.0

while loop_answer == "Yes":
    quantity_value = float(input("Enter quantity: "))
    price_value = float(input("Enter price: "))

    extended_price = quantity_value * price_value

    if extended_price > 10000:
        discount_rate = 0.25
    else:
        discount_rate = 0.10

    discount_amount = extended_price * discount_rate
    total_amount = extended_price - discount_amount

    print("Extended price:", extended_price)
    print("Discount amount:", discount_amount)
    print("Total amount:", total_amount)

    total_discounts = total_discounts + discount_amount
    loop_answer = input('Do you want to enter another order? (Enter "Yes" to continue): ')

print("Total of all discounts:", total_discounts)