from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    fuel = 3.5
    horse_power = 115.5
    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_attributes_types(self):
        self.assertTrue(isinstance(self.vehicle.fuel, float))
        self.assertTrue(isinstance(self.vehicle.capacity, float))
        self.assertTrue(isinstance(self.vehicle.horse_power, float))
        self.assertTrue(isinstance(self.vehicle.fuel_consumption, float))
        self.assertTrue(isinstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float))

    def test_drive_successful(self):
        self.vehicle.drive(2)
        self.assertEqual(1, self.vehicle.fuel)

    def test_drive_unsuccessful_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(3)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_successful(self):
        self.vehicle.fuel = 1
        self.vehicle.refuel(1.5)
        self.assertEqual(2.5, self.vehicle.fuel)

    def test_refuel_too_many_fuel_raises_exception(self):
        self.vehicle.fuel = 5
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(6)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_method(self):
        self.vehicle.fuel = 2.5
        expected = f"The vehicle has 115.5 " \
                   f"horse power with 2.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, str(self.vehicle))




if __name__ == "__main__":
    main()