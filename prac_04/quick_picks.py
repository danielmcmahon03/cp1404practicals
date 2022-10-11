"""
CP1404 Practical 4
Quick Picks
"""

import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6

number_of_quick_picks = int(input("Number of quick picks? "))
while number_of_quick_picks <= 0:
    print("Invalid number. Try again.")
    number_of_quick_picks = int(input("Number of quick picks? "))

for i in range(number_of_quick_picks):
    quick_picks = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_picks:
            number = random.randint(MINIMUM, MAXIMUM)
        quick_picks.append(number)
    print(" ".join(sorted(f"{number:2}" for number in quick_picks)))
