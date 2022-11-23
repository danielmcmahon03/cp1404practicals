"""
Unreliable Car Class
"""

import random
from car import Car


class UnreliableCar(Car):

    def __init__(self, reliability: float, **kwargs):
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(1, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0


