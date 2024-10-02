from datetime import datetime

from constants import VehicleTypeEnum


class ParkingSpot:

    def __init__(self, spot_id, vehicle_type=None):
        self.spot_id = spot_id
        self.is_vehicle_parked = False
        self.vehicle = None
        self.vehicle_type = vehicle_type if vehicle_type else VehicleTypeEnum.CAR.value

    def park_vehicle(self, vehicle):
        if not self.is_vehicle_parked and self.vehicle_type == vehicle.type:
            self.is_vehicle_parked = True
            self.vehicle = vehicle
            vehicle.arrived_at = datetime.utcnow()
        else:
            raise ValueError(f"Vehicle is already parked at spot_id:{self.spot_id}")

    def unpark_vehicle(self):
        self.is_vehicle_parked = False
        self.vehicle = None

    def is_available(self):
        return not self.is_vehicle_parked

    def get_vehicle(self):
        return self.vehicle

    def get_spot_number(self):
        return self.spot_id

    def get_vehicle_type(self):
        return self.vehicle_type




