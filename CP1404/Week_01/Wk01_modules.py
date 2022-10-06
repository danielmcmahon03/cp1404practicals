"""
First demos for CP1404
"""

# name = input("What is your name? ")
# print("Hello", name)

# Do this now
# get monthly cost
# yearly cost = monthly cost * 12
# print yearly cost

# monthly_cost = float(input("Monthly Cost: $"))
# yearly_cost = monthly_cost * 12
# print(f"The yearly cost: ${yearly_cost:.2f}")


# Do this now
# get gross pay
# get tax rate
# calculate net pay = gross pay - (gross pay * (tax rate / 100))
# display net pay

# gross_pay = float(input("Gross Pay: $"))
# tax_rate = float(input("Tax Rate (%): "))
# net_pay = gross_pay - (gross_pay * (tax_rate / 100))
# print(net_pay)


# Do this now - Age

age = int(input("Age: "))
if age <= 4:
    print("You are a baby")
elif age <= 17:
    print("You are a child")
elif age <= 65:
    print("You are an adult")
else:
    print("You are old")
