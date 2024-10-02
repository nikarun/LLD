import time

from parking_lot import ParkingLot
from floor import Floor
from car import Car
from truck import Truck
from bike import Bike
from parking_spot import ParkingSpot
from constants import VehicleTypeEnum


class ParkingLotDemo:

    @staticmethod
    def execute():
        parking_lot_inst = ParkingLot()
        # on first floor create 3 spots one for each
        # on second floor create spots for car only
        spot1 = ParkingSpot(0, VehicleTypeEnum.BIKE.value)
        spot2 = ParkingSpot(1)
        spot3 = ParkingSpot(2, VehicleTypeEnum.TRUCK.value)
        parking_lot_inst.add_floor(Floor(1, [spot1, spot2, spot3], 3))
        parking_lot_inst.add_floor(Floor(2))

        car = Car("123")
        bike = Bike("234")
        truck = Truck("345")

        parking_lot_inst.park_vehicle(car)
        parking_lot_inst.park_vehicle(bike)
        parking_lot_inst.park_vehicle(truck)

        time.sleep(5)
        parking_lot_inst.unpark_vehicle(truck)

        parking_lot_inst.display_availablity()

        # implement a functionality which will display the price at the time of unparking.


if __name__ == "__main__":
    ParkingLotDemo.execute()
