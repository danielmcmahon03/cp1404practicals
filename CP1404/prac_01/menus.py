"""
CP1404 - Practical 1
Menus
"""

MENU = "(H)ello\n" \
       "(G)oodbye\n" \
       "(Q)uit"

name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid Choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished")
