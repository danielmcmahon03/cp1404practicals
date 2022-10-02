"""
CP1404/CP5632 - Practical
Answer the following questions:

1. When will a ValueError occur?

A ValueError will occur when the input for a numerator or denominator are not integers,
and are inputted as strings that can not be changed to an integer. E.g "s50s"

2. When will a ZeroDivisionError occur?

A ZeroDivision Error will occur when the input for the denominator is equal to 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

To avoid the ZeroDivisionError, use an error checking pattern so that the value of 0 cannot be inputted.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Invalid denominator.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
