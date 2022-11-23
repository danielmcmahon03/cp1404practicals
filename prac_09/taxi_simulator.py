"""
Taxi Simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_cost = 0.00

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":

        if choice == "C":
            print("Taxis available")
            display_taxis(taxis)
            current_taxi = get_valid_taxi(taxis)

        elif choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive.")
            else:
                total_cost = calculate_fare(current_taxi, total_cost)

        else:
            print("Invalid Option")

        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Total trip cost: ${total_cost}")
    print("Taxis are now: ")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi.__str__()}")


def get_valid_taxi(taxis):
    taxi_choice = int(input("Choose taxi: "))
    if taxi_choice < 0 or taxi_choice >= len(taxis):
        print("Invalid taxi choice")
        return None
    return taxis[taxi_choice]


def calculate_fare(current_taxi, total_cost):
    distance = float(input("Drive how far? "))
    current_taxi.drive(distance)
    trip_cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    total_cost += trip_cost
    return total_cost


main()