"""
Silver Service Taxi Class
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fare costs."""
    price_per_km = 1.23
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        return super().get_fare() + self.flagfall
