from Vehicle import Vehicle


class Cycle(Vehicle):

    def vehicle_accelerate(self):
        Vehicle.vehicle_accelerate(self)
        print('Cycle is Started Pedalling')