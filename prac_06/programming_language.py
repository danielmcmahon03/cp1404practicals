"""
CP1404 - Programming Language Class
"""


class ProgrammingLanguage:
    """."""

    def __init__(self, field, typing, reflection, year):
        """."""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def __repr__(self):
        return f"{self.field} {self.typing} {self.reflection} {self.year}"

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return f"{self.field}"
