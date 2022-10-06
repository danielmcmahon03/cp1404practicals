# Do this Now (Length)

# from random import randint
#
# length = int(input("Length: "))
# width = randint(1, length)
# area = length * width
# print(f"Area of {length} x {width} is {area:2}.")


# Do this now (Print Grid)

# def print_grid(number_of_rows, number_of_columns):
#     # Version 1
#     for i in range(number_of_rows):
#         for j in range(number_of_columns):
#             print('*', end="")
#         print()
#
#     # Version 2
#     for i in range(number_of_rows):
#         print('*' * number_of_columns)
#
#     # Version 3
#     print(f"{'*' * number_of_columns}\n" * number_of_rows)
#
#
# print_grid(3, 7)
# print_grid(2, 50)
#
#
# # Get Multiple Variables
#
# def get_limits():
#     low = int(input("Low: "))
#     high = int(input("High: "))
#     return low, high
#

# def run_tests():
#     low, high = get_limits()
#     print(low, high)
#     print(type(low))
#
#
# run_tests()

password = input("Password: ")
MINIMUM = 10
while len(int(password)) <= MINIMUM:
    print(f"Password must contain characters longer or equal to {MINIMUM}.")
    password = input("Password: ")
print("*" * len(int(password)))
