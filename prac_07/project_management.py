"""
CP1404 - Practical 7
Project Management
Estimate: 45 minutes
Time:
"""

from project import Project
import datetime

MENU = "(L)oad projects\n(S)ave projects\n" \
       "(D)isplay projects\n(F)ilter projects by date\n" \
       "(A)dd new project\n(U)pdate project\n(Q)uit"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects()
            print(projects)
        elif choice == "S":
            save_projects()
        elif choice == "D":
            display_projects()
        elif choice == "F":
            filter_projects_by_date()
        elif choice == "A":
            add_new_project()
        elif choice == "U":
            update_project()
        else:
            print("Invalid decision.")
        choice = input(">>> ").upper()


def load_projects():
    projects = []
    file_name = input("Filename: ")
    in_file = open(file_name, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
        project = Project(parts[0], start_date, int(parts[2]), float(parts[3]), parts[4])
        projects.append(project)
    in_file.close()
    return projects


def save_projects():
    pass


def display_projects():
    pass


def filter_projects_by_date():
    pass


def add_new_project():
    pass


def update_project():
    pass

main()