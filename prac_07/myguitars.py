"""
CP1404 - Practical 7
My Guitars
"""

from prac_06.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read guitar.csv file, display the file contents, add new guitars and save them to a file."""
    guitars = []
    in_file = open(FILENAME, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    display_guitars(guitars)
    add_guitar(guitars)
    save_guitars(guitars)

    display_guitars(guitars)


def display_guitars(guitars):
    """Display guitars in list."""
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def add_guitar(guitars):
    """Add another guitar to guitars."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(f"{name} ({year}) : ${cost:,.2f}\n")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Name: ")


def save_guitars(guitars):
    """Write guitars to an outfile"""
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}",
                  file=out_file)


main()
