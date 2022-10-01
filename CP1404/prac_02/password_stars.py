"""
CP1404 - Practical 2
Password Stars
"""

MINIMUM = 10


def main():
    """Function docstring"""
    password = get_password()
    print_stars(password)


def get_password():
    password = input("Password: ")
    while len(password) < MINIMUM:
        print(f"Password must have a length greater or equal to {MINIMUM}.")
        password = input("Password: ")
    return password


def print_stars(password):
    print("*" * len(password))


main()