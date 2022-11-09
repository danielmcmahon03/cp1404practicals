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
            load_projects(file_name)
        elif choice == "S":
            save_projects(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid decision.")
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_projects(file_name):
    """Load projects from list."""
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
    """Write projects to an outfile"""
    with open("projects.txt", "w") as out_file:
        for project in projects:
            print(f"{project.name}  {project.start_date}    {project.priority}  {project.cost}  {project.completion}",
                  file=out_file)


def display_projects(projects):
    """Displays all projects sorted by priority."""
    print("Incomplete projects:")
    projects.sort()
    for project in projects:
        if not project.is_complete():
            print("\t", project)
    print("Completed projects:")
    for project in projects:
        if project.is_complete():
            print("\t", project)


def filter_projects_by_date(projects):
    """Filter projects to show projects after specified date."""
    date = (input("Show projects that start after date (dd/mm/yy): "))
    date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    projects.sort()
    for project in projects:
        if project.start_date > date:
            print(project)


def add_new_project(projects):
    """Add a new project to project list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: $")
    completion = input("Percent complete: ")
    project = Project(name, start_date, priority, cost, completion)
    projects.append(project)


def update_project(projects):
    """Update a current project."""
    for i, project in enumerate(projects, 0):
        print(f"({i}) {project}")
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    if projects[project_choice].is_complete():
        print("Already completed")
    else:
        new_percentage = float(input("New percentage: "))
        projects[project_choice][4] = new_percentage
        new_priority = int(input("New priority: "))
        projects[project_choice][2] = new_priority


main()
