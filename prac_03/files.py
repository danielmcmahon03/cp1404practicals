# Q1.
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# Q2.
name = input("Name: ")
with open("name.txt", "w") as out_file:
    print(f"Your name is {name}", file=out_file)

# Q3.
total = 0
with open("numbers.txt", "r") as in_file:
    total += float(in_file.readline())
    total += float(in_file.readline())
print(total)

# Q4.
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += float(line)
print(total)
