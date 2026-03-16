# Borhan Vishlaghi
# 02/15/2026

def compute_discount(price_amount, discount_rate):

    discount_amount = price_amount * discount_rate
    discounted_price = price_amount - discount_amount

    return discount_amount, discounted_price


quantity_value = int(input("Enter quantity: "))
price_amount = float(input("Enter price: "))
discount_rate = float(input("Enter discount rate: "))

discount_amount, discounted_price = compute_discount(price_amount, discount_rate)

print("Quantity:", quantity_value)
print("Price:", price_amount)
print("Discount Amount:", discount_amount)
print("Discounted Price:", discounted_price)