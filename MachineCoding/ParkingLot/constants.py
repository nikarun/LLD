from enum import Enum


class VehicleTypeEnum(Enum):
    CAR = 'car'
    BIKE = 'bike'
    TRUCK = 'truck'


ParkingRatesPerSeconds = {
    VehicleTypeEnum.CAR.value: 100,
    VehicleTypeEnum.TRUCK.value: 500,
    VehicleTypeEnum.BIKE.value: 50
}
