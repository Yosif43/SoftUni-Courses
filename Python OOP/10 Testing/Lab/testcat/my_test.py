from unittest import TestCase, main
from CarManager.car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Nissan", "GT-R", 10, 50)

    def test_constructor(self):
        self.assertEqual(self.car.make, "Nissan")
        self.assertEqual(self.car.model, "GT-R")
        self.assertEqual(self.car.fuel_consumption, 10)
        self.assertEqual(self.car.fuel_capacity, 50)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_property(self):
        self.car.make = "Honda"
        self.assertEqual(self.car.make, "Honda")

        with self.assertRaises(Exception):
            self.car.make = ""

    def test_model_property(self):
        self.car.model = "Accord"
        self.assertEqual(self.car.model, "Accord")

        with self.assertRaises(Exception):
            self.car.model = ""

    def test_fuel_consumption_property(self):
        self.car.fuel_consumption = 12
        self.assertEqual(self.car.fuel_consumption, 12)

        with self.assertRaises(Exception):
            self.car.fuel_consumption = 0

    def test_fuel_capacity_property(self):
        self.car.fuel_capacity = 60
        self.assertEqual(self.car.fuel_capacity, 60)

        with self.assertRaises(Exception):
            self.car.fuel_capacity = 0

    def test_fuel_amount_property(self):
        self.car.fuel_amount = 20
        self.assertEqual(self.car.fuel_amount, 20)

        with self.assertRaises(Exception):
            self.car.fuel_amount = -5

    def test_refuel(self):
        self.car.refuel(30)
        self.assertEqual(self.car.fuel_amount, 30)

        with self.assertRaises(Exception):
            self.car.refuel(0)

    def test_drive(self):
        self.car.refuel(30)
        self.car.drive(200)
        self.assertEqual(self.car.fuel_amount, 10)

        with self.assertRaises(Exception):
            self.car.drive(600)


if __name__ == '__main__':
    main()
