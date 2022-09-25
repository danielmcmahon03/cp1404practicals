"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = "C - Convert Celsius to Fahrenheit\n" \
       "F - Convert Fahrenheit to Celsius\n" \
       "Q - Quit"


def main():
    """Program for Converting Celsius to Fahrenheit and Vice-Versa"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_celsius(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = calculate_fahrenheit(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_celsius(celsius):
    """Calculate Fahrenheit from Celsius"""
    return celsius * 9.0 / 5 + 32


def calculate_fahrenheit(fahrenheit):
    """Calculate Celsius from Fahrenheit"""
    return (fahrenheit - 32) * 5 / 9


main()

