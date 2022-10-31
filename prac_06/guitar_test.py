"""
Practical 6 - Guitar Test
"""

from prac_06.guitar import Guitar


print(f"Gibson L-5 CES get_age() - Expected 100. Got {Guitar('G', 1922, 1).get_age()}")
print(f"Another Guitar get_age() - Expected 9. Got {Guitar('A', 2013, 1).get_age()}")
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {Guitar('G', 1922, 1).is_vintage()}")
print(f"Another Guitar is_vintage() - Expected False. Got {Guitar('A', 2013, 1).is_vintage()}")

