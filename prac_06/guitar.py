"""
CP1404 - Guitar Class
"""

CURRENT_YEAR = 2022


class Guitar:
    """Class for Guitar names, the year it was made and its cost."""

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        """Determine current age of a guitar."""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Return if a guitar is older than 50 years old, and therefore vintage"""
        return self.get_age() >= 50
