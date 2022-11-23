class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty instrument collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Musician."""
        return f"{self.name} ({self.musicians})"

    def __repr__(self):
        """Return a string representation of a Musician, showing the variables."""
        return f"{self}"

    def add(self, musician):
        """Add an instrument to musician's collection."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the instrument playing their first (or no) instrument."""
        if not self.musicians:
            return f"{self.name} needs an instrument!"
        return f"{self.name} is playing: {self.musicians[0]}"


# if __name__ == '__main__':
#     from musician import Musician
#
#     band = Band()
#     assert not band.name
#     assert not band.bands
#
#     print(band)
#     print(band.play())
