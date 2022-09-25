"""
CP1404 Practical
Score Menu
"""

MENU = "(P) Print Score\n" \
       "(*) Print Stars\n" \
       "(Q) Quit"


def main():
    """Displays a Menu and gets a choice"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "P":
            score = get_valid_score()
            result = evaluate_score(score)
            print(f"The score {score} is {result}.\n")
        elif choice == "*":
            score = get_valid_score()
            print_stars(score)
        else:
            print("Invalid Choice\n")
        print(MENU)
        choice = input(">>> ").upper()
    print("Done")


def get_valid_score():
    """Returns a valid score between 0 and 100"""
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
    """Print the number of stars"""
    print("*" * int(score))
    print()


main()


