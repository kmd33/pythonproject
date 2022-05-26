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
bike1.vehicle_accelerate(6)
bike1.vehicle_speed()
bike1.vehicle_accelerate(20)
bike1.vehicle_speed()
# car1.vehicle_type()
# bus1.vehicle_type()
# bike1.vehicle_accelerate()
# bike1.vehicle_speed()
# cycle1.vehicle_type()
# cycle1.vehicle_accelerate()
print(type(bike1))    # it is an instance of vehicle class
print(type(Vehicle)) # it is a clas object
print(type(bike1.vehicle_type())) # the output is string

