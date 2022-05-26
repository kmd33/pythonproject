class Vehicle:
# this is a vehicle class
    def __init__(self,type,name,speed=0):
        self.speed = speed
        self.type = type
        self.name = name

    def vehicle_name(self):
        return self.name

    def vehicle_type(self):
        return self.type
       # print("The vehicle type of " + self.name +" is : " + self.type)

    def vehicle_accelerate(self,x):
        self.speed = self.speed+x

    def vehicle_speed(self):
        print("The speed of " + self.type + " " + self.name + " is : "+ str(self.speed) + " kmph")