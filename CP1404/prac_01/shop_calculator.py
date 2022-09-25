"""
CP1404 - Practical 1
Shop Calculator
"""

number_of_items = int(input("Number of items: "))
total_price = 0
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for item in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > 100:
    total_price -= (total_price * 0.1)
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
