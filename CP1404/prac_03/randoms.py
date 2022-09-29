"""
CP1404 - Practical 3
Random Numbers
"""

# LINE 1
# 19 ; 12 ; 14
# Smallest: 5
# Largest: 20

# LINE 2
# 9 ; 9 ; 7
# Smallest: 3
# Largest: 9
# It can not produce a 4 because the function is in 'steps of 2.
# The only valid answers would be 3, 5, 7, and 9.

# LINE 3
# 3.3035592237933167 ; 2.884411550145366 ; 5.156296299153061
# Smallest: 2.5
# Largest: 5.5
# random.uniform gives a value between the two values,
# inclusive of the first value and exclusive of the last value
# (but could be inclusive depending on rounding)

import random
random_number = random.randint(1, 100)
