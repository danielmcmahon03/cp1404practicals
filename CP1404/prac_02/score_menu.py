"""
CP1404 Practical
Score Menu
"""

MENU = "(P) Print Score\n" \
       "(S) Print Stars\n" \
       "(Q) Quit"


def main():
    """"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        score = get_valid_score()
        if choice == "P":
            result = evaluate_score(score)
            print(f"The score {score} is {result}.\n")
        elif choice == "S":
            print_stars(score)
        else:
            "Invalid Choice"
        print(MENU)
        choice = input(">>> ").upper()
    print("Done")


def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = float(input("Enter score: "))
    return score


def evaluate_score(score):
    """Return a Score Evaluation"""
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


def print_stars(score):
    print("*" * int(score))
    print()


main()


