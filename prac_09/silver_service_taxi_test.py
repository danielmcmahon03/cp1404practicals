"""
Silver Service Taxi Test
"""

from silver_service_taxi import SilverServiceTaxi

sst = SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)
print(sst)

silver = SilverServiceTaxi(name="Silver Taxi", fuel=200, fanciness=2)
print(silver)
silver.drive(18)
print(f"Total fare: {silver.get_fare():.2f}")
