from constants import VehicleTypeEnum


class Vehicle:
    def __init__(self, license_number, type=VehicleTypeEnum.CAR.value):
        self.license_number = license_number
        self.type = type
