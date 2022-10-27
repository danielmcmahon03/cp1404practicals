"""
CP1404 Practical 5
Hex Colours
"""

COLOUR_TO_CODE = {"absolutezero": "#0048ba", "aliceblue": "#f0f8ff", "amethyst": "#9966cc", "aqua": "#00ffff",
                  "bittersweet": "#fe6f5e", "carnelian": "#b31b1b", "cobalt": "#0047ab", "marigold": "#eaa221",
                  "razzmatazz": "#e3256b", "volt": "#ceff00"}

colour = input("Colour: ").lower()
while colour != "":
    while colour not in COLOUR_TO_CODE:
        print("Invalid Choice")
        colour = input("Colour: ").lower()
    print(f"{colour} is {COLOUR_TO_CODE[colour]}")
    colour = input("Colour: ").lower()
