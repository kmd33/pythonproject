from Cycle import Cycle
from Vehicle import Vehicle

bike1 = Vehicle("Bike", "CBR")
car1 = Vehicle("Car", "Ferrari")
bus1 = Vehicle("Bus", "Indra")
cycle1 = Cycle("Cycle","Gear Cycle")


print("The type of vehicle " + bike1.vehicle_name() + " is : " + bike1.vehicle_type())
print("The type of vehicle " + car1.vehicle_name() + " is : " + car1.vehicle_type())
print("The type of vehicle " + bus1.vehicle_name() + " is : " + bus1.vehicle_type())
print("The type of vehicle " + cycle1.vehicle_name() + " is : " + cycle1.vehicle_type())
# car1.vehicle_type()
# bus1.vehicle_type()
# bike1.vehicle_accelerate()
# bike1.vehicle_speed()
# cycle1.vehicle_type()
# cycle1.vehicle_accelerate()
