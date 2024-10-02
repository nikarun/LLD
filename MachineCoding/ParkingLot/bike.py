from vehicle import Vehicle
from constants import VehicleTypeEnum


class Bike(Vehicle):
    """
    bike_id, car_owner, entry_time,
    """
    def __init__(self, license_number):
        super().__init__(license_number, VehicleTypeEnum.BIKE.value)
        self.license_number = license_number

