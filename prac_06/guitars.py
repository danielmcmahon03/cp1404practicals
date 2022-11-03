"""
CP1404 - Practical 6
Guitars
"""

from prac_06.guitar import Guitar

guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    print(f"{name} ({year}) : ${cost:,.2f}\n")
    guitar_data = Guitar(name, year, cost)
    guitars.append(guitar_data)
    name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("\n... snip ...\n")

print("These are my guitars.")
length_of_string = ""

for i, guitar in enumerate(guitars, 1):
    vintage_string = ""
    print(f"Guitar {i}: {guitar.name:>15} ({guitar.year}), worth ${guitar.cost:10,.2f}"
          f"{' (vintage)' if guitar.is_vintage() else ''}")
    # CHECK THIS WITH EMMA TOMORROW
