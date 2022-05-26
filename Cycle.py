from Vehicle import Vehicle


class Cycle(Vehicle):

    # def __int__(self,type,name,speed=0):
    #     super().__init__(type,name,speed=0)
    #
    def vehicle_accelerate(self):
        Vehicle.vehicle_accelerate(self)
        print('Cycle is Started Pedalling')