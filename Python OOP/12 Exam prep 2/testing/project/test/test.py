from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("Toyota", "Sedan", 200, 15000.0)

    def test_init(self):
        car = SecondHandCar("Toyota", "Sedan", 200, 15000.0)
        self.assertEqual(car.model, "Toyota")
        self.assertEqual(car.car_type, "Sedan")
        self.assertEqual(car.mileage, 200)
        self.assertEqual(car.price, 15000.0)
        self.assertEqual(car.repairs, [])
        self.assertListEqual(car.repairs, [])

    def test_price_less_than_1_or_equal_raises(self):
        with self.assertRaises(ValueError) as ex:
            car = SecondHandCar("Toyota", "Sedan", 200, 0.9)
        self.assertEqual(str(ex.exception), "Price should be greater than 1.0!")

    def test_mileage_less_then_200_or_equals_raises(self):
        with self.assertRaises(ValueError) as ex:
            car = SecondHandCar("Toyota", "Sedan", 100, 15000.0)
        self.assertEqual(str(ex.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

        with self.assertRaises(ValueError) as ex:
            car = SecondHandCar("Toyota", "Sedan", 98, 15000.0)
        self.assertEqual(str(ex.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_set_promotional_price_higher_than_current_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(15000.0)
        self.assertEqual(str(ex.exception), 'You are supposed to decrease the price!')

        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(15001.0)
        self.assertEqual(str(ex.exception), 'You are supposed to decrease the price!')

    def test_set_promotional_price(self):
        self.assertEqual(self.car.price, 15000.0)
        result = self.car.set_promotional_price(10000)
        self.assertEqual(self.car.price, 10000)
        self.assertEqual(result, 'The promotional price has been successfully set.')

    def test_repair_price_to0_high_raises(self):
        self.assertEqual(self.car.price, 15000)
        self.assertEqual(self.car.repairs, [])
        half_price = self.car.price / 2
        result = self.car.need_repair(half_price+1, "Test repair")
        self.assertEqual(result, 'Repair is impossible!')
        self.assertEqual(self.car.price, 15000)
        self.assertEqual(self.car.repairs, [])

    def test_repair(self):
        self.assertEqual(self.car.price, 15000)
        self.assertEqual(self.car.repairs, [])
        half_price = self.car.price / 2
        current_price = self.car.price
        result = self.car.need_repair(half_price, "Test repair")
        self.assertEqual(result, 'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, current_price+half_price)
        self.assertEqual(self.car.repairs, ["Test repair"])

    def test_repair_less_half_price(self):
        self.assertEqual(self.car.price, 15000)
        self.assertEqual(self.car.repairs, [])
        half_price = self.car.price / 2 - 1
        current_price = self.car.price
        result = self.car.need_repair(half_price, "Test repair")
        self.assertEqual(result, 'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, current_price+half_price)
        self.assertEqual(self.car.repairs, ["Test repair"])

    def test_compare_different_types_impossible(self):
        car2 = SecondHandCar("WV", "Combi", 9000, 10000)
        result = car2 > self.car
        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

    def test_compare(self):
        car2 = SecondHandCar("WV", self.car.car_type, 9000, 10000)
        result = car2 > self.car
        self.assertFalse(result)

    def test_string(self):
        self.assertEqual(str(self.car), """Model Toyota | Type Sedan | Milage 200km
Current price: 15000.00 | Number of Repairs: 0""")


if __name__ == '__main__':
    main()
