"""
Unreliable Car Test
"""

from unreliable_car import UnreliableCar

good_car = UnreliableCar(name="Good", fuel=100, reliability=99)
print(f"{good_car.name} drove {good_car.drive(70)}km.")

bad_car = UnreliableCar(name="Bad", fuel=100, reliability=1)
print(f"{bad_car.name} drove {bad_car.drive(50)}km.")
