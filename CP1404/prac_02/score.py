"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    """Receive a Score, Evaluate the Score and Generates a Random Score"""
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(f"The score {score} is {result}.")
    random_score = random.randint(0, 100)
    random_result = evaluate_score(random_score)
    print(f"The score {random_score} is {random_result}.")


def evaluate_score(score):
    """Return a Score Evaluation"""
    if score < 0 or score > 100:
        return "Invalid"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()




