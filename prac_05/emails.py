"""
Emails
Estimate: 20 minutes
Actual:   xx minutes
"""

email_to_name = {}
email = input("Email: ")
while email != "":
    first_part = email.split("@")[0]
    names = first_part.split(".")
    name = " ".join(names).title()
    correct_name = input(f"Is your name {name}? (Y/n) ").upper()
    if correct_name != "Y" and correct_name != "":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
