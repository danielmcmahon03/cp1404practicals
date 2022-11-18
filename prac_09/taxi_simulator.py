"""
Taxi Simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("Choose a taxi")
        elif choice == "D":
            print("Drive a taxi")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("QUIT")

