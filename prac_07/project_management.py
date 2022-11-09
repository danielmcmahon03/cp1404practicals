"""
CP1404 - Practical 7
Project Management
Estimate: 1 hour
Time:
"""

from project import Project
import datetime

MENU = "(L)oad projects\n(S)ave projects\n" \
       "(D)isplay projects\n(F)ilter projects by date\n" \
       "(A)dd new project\n(U)pdate project\n(Q)uit"


def main():
    print(MENU)
    projects = load_projects("projects.txt")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            file_name = input("Filename: ")
            projects = load_projects(file_name)
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date()
        elif choice == "A":
            add_new_project()
        elif choice == "U":
            update_project()
        else:
            print("Invalid decision.")
        choice = input(">>> ").upper()


def load_projects(file_name):
    projects = []
    in_file = open(file_name, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
        project = Project(parts[0], start_date, int(parts[2]), float(parts[3]), parts[4])
        projects.append(project)
    in_file.close()
    return projects


def save_projects(projects):
    """Write guitars to an outfile"""
    with open("projects.txt", "w") as out_file:
        for project in projects:
            print(f"{project.name}  {project.start_date}    {project.priority}  {project.cost}  {project.completion}",
                  file=out_file)


def display_projects(projects):
    print("Incomplete projects:")
    projects.sort()
    for project in projects:
        if not project.is_complete():
            print("\t", project)
    print("Completed projects:")
    for project in projects:
        if project.is_complete():
            print("\t", project)


def filter_projects_by_date():
    pass


def add_new_project():
    pass


def update_project():
    pass


main()
