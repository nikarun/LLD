class ParkingLot:
    _instance = None

    def __init__(self):
        if ParkingLot._instance is not None:
            raise ValueError('This is singleton cannot create instance again')
        else:
            ParkingLot._instance = self
            self.floors = []

    def get_instance(self):
        if self._instance is None:
            return ParkingLot()
        return self._instance

    def add_floor(self, floor):
        self.floors.append(floor)

    def park_vehicle(self, vehicle):
        for floor in self.floors:
            if floor.park_vehicle(vehicle):
                return True

        return False

    def unpark_vehicle(self, vehicle):
        for floor in self.floors:
            if floor.unpark_vehicle(vehicle):
                return True

        return False

    def display_availablity(self):
        for floor in self.floors:
            floor.display_availablity()
