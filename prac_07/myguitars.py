"""
CP1404 - Practical 7
My Guitars
"""

import csv
# from collections import namedtuple
# from language_file_reader import using_csv


from prac_06.guitar import Guitar


def main():
    """."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
