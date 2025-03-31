from abc import ABC, abstractmethod


class BaseVehicle(ABC):
    def __init__(self, brand, model, license_plate_number, max_mileage):
        self.brand = brand.strip()
        self.model = model.strip()
        self.license_plate_number = license_plate_number.strip()
        self.max_mileage = max_mileage
        self.battery_level = 100
        self.is_damaged = False

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not value.strip():
            raise ValueError("Brand cannot be empty!")
        self._brand = value.strip()

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model cannot be empty!")
        self._model = value.strip()

    @property
    def license_plate_number(self):
        return self._license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, value):
        if not value.strip():
            raise ValueError("License plate number is required!")
        self._license_plate_number = value.strip()

    @abstractmethod
    def drive(self, mileage: float):
        pass

    def recharge(self):
        self.battery_level = 100

    def change_status(self):
        self.is_damaged = not self.is_damaged

    def __str__(self):
        status = "OK" if not self.is_damaged else "Damaged"
        return (f"{self.brand} {self.model} License plate: {self.license_plate_number} Battery: {self.battery_level}% "
                f"Status: {status}")
