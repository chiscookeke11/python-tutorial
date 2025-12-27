# Task 1
input_price = int(input("Please enter the item price:" ))
input_discount = int(input("Please enter the stated percentage discount:" ))

def calculate_discount(price, discount_percent):
    if (discount_percent/100) > (20/100): return price - (price * 20/100)

    return price

print(calculate_discount(input_price, input_discount))



