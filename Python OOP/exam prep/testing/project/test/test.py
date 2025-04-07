import unittest
from project.robot import Robot


class TestRobot(unittest.TestCase):

    def setUp(self):
        self.robot = Robot("R123", "Education", 100, 1000.0)

    def test_constructor(self):
        self.assertEqual(self.robot.robot_id, "R123")
        self.assertEqual(self.robot.category, "Education")
        self.assertEqual(self.robot.available_capacity, 100)
        self.assertEqual(self.robot.price, 1000.0)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

    def test_category_setter_getter(self):
        self.robot.category = "Military"
        self.assertEqual(self.robot.category, "Military")
        with self.assertRaises(ValueError):
            self.robot.category = "Invalid"

    def test_price_setter_getter(self):
        self.robot.price = 1500.0
        self.assertEqual(self.robot.price, 1500.0)
        with self.assertRaises(ValueError):
            self.robot.price = -100

    def test_upgrade(self):
        self.assertEqual(self.robot.upgrade("Camera", 200.0), "Robot R123 was upgraded with Camera.")
        self.assertEqual(self.robot.price, 1300.0)  # 1000 + 200 * 1.5
        self.assertEqual(self.robot.upgrade("Camera", 200.0), "Robot R123 was not upgraded.")

    def test_update(self):
        self.assertEqual(self.robot.update(1.1, 20), "Robot R123 was updated to version 1.1.")
        self.assertEqual(self.robot.available_capacity, 80)  # 100 - 20
        self.assertEqual(self.robot.update(1.1, 20), "Robot R123 was not updated.")
        self.assertEqual(self.robot.update(1.2, 90), "Robot R123 was not updated.")

    def test_comparison(self):
        other_robot = Robot("R456", "Entertainment", 80, 1200.0)
        self.assertEqual(self.robot.__gt__(other_robot), "Robot with ID R123 is cheaper than Robot with ID R456.")
        other_robot.price = 1000.0
        self.assertEqual(self.robot.__gt__(other_robot), "Robot with ID R123 costs equal to Robot with ID R456.")
        other_robot.price = 800.0
        self.assertEqual(self.robot.__gt__(other_robot), "Robot with ID R123 is more expensive than Robot with ID R456.")


if __name__ == '__main__':
    unittest.main()
