from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from typing import List


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if any(u.driving_license_number == driving_license_number for u in self.users):
            return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ['PassengerCar', 'CargoVan']:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if any(v.license_plate_number == license_plate_number for v in self.vehicles):
            return f"{license_plate_number} belongs to another vehicle."

        if vehicle_type == 'PassengerCar':
            vehicle = PassengerCar(brand, model, license_plate_number)
        else:
            vehicle = CargoVan(brand, model, license_plate_number)

        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1
        existing_route = next((r for r in self.routes if r.start_point == start_point and r.end_point == end_point),
                              None)

        if existing_route:
            if existing_route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif existing_route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            else:
                existing_route.is_locked = True

        route = Route(start_point, end_point, length, route_id)
        self.routes.append(route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = next((u for u in self.users if u.driving_license_number == driving_license_number), None)
        vehicle = next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)
        route = next((r for r in self.routes if r.route_id == route_id), None)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return (f"{vehicle.brand} {vehicle.model} License plate: {license_plate_number} Battery: "
                f"{vehicle.battery_level}% Status: {'OK' if not vehicle.is_damaged else 'Damaged'}")

    def repair_vehicles(self, count: int):
        damaged_vehicles = sorted(
            [v for v in self.vehicles if v.is_damaged],
            key=lambda v: (v.brand, v.model)
        )
        repaired_vehicles = damaged_vehicles[:count]

        for vehicle in repaired_vehicles:
            vehicle.is_damaged = False
            vehicle.recharge()

        return f"{len(repaired_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda u: u.rating, reverse=True)
        report = "*** E-Drive-Rent ***\n" + "\n".join(str(u) for u in sorted_users)
        return report
