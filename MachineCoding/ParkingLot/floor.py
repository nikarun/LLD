import math
from datetime import datetime

from parking_spot import ParkingSpot
from constants import ParkingRatesPerSeconds


class Floor:

    def __init__(self, floor_num, parking_spots=None, num_spots=5):
        self.floor_num = floor_num
        self.num_spots = num_spots
        self.spots = parking_spots if parking_spots else [ParkingSpot(i) for i in range(num_spots)]

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if not spot.is_vehicle_parked and spot.vehicle_type == vehicle.type:
                spot.park_vehicle(vehicle)
                print(f'Successfully parked vehicle with license_number: {vehicle.license_number} on spot: {spot.spot_id} on floor: {self.floor_num}')
                return True
        print(f'Failed to park vehicle as there is not spot which supports type: {vehicle.type} or there is no any empty spot')
        return False

    def unpark_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.is_vehicle_parked and spot.vehicle == vehicle:
                spot.unpark_vehicle()
                print(f'Successfully unparked vehicle with license_number: {vehicle.license_number} on spot: {spot.spot_id} on floor: {self.floor_num}')
                parking_duration = math.ceil((datetime.utcnow() - vehicle.arrived_at).total_seconds())
                base_parking_cost = ParkingRatesPerSeconds[vehicle.type]
                print(f'Vehicle was parked for seconds: {parking_duration}')
                print(f'Please pay the bill amount of : {parking_duration*base_parking_cost} for your vehicle with license number: {vehicle.license_number}')
                return True
        return False

    def display_availablity(self):
        print(f'Displaying availablity for floor: {self.floor_num}')
        for spot in self.spots:
            if not spot.is_vehicle_parked:
                print(f'Spot with id: {spot.spot_id} is available for vehicle type: {spot.vehicle_type}')

