from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.station = RailwayStation("Central")

    def test_initialization(self):
        self.assertEqual(self.station.name, "Central")
        self.assertEqual(len(self.station.arrival_trains), 0)
        self.assertEqual(len(self.station.departure_trains), 0)

    def test_name(self):
        self.assertEqual(self.station.name, "Central")

    def test_name_is_less_than_3_chars_raises(self):
        with self.assertRaises(ValueError)as ve:
            self.station.name = "Ce"
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board("Train1")
        self.assertEqual(len(self.station.arrival_trains), 1)
        self.assertIn("Train1", self.station.arrival_trains)

    def test_train_has_arrived(self):
        self.station.new_arrival_on_board("Train1")
        result = self.station.train_has_arrived("Train1")
        self.assertEqual(result, "Train1 is on the platform and will leave in 5 minutes.")
        self.assertEqual(len(self.station.departure_trains), 1)

        self.station.new_arrival_on_board("Train2")
        result = self.station.train_has_arrived("Train3")
        self.assertEqual(result, "There are other trains to arrive before Train3.")

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board("Train A")
        self.assertEqual(self.station.arrival_trains[-1], "Train A")

    def test_train_has_left(self):
        self.station.new_arrival_on_board("Train1")
        self.station.train_has_arrived("Train1")
        self.assertTrue(self.station.train_has_left("Train1"))
        self.assertFalse(self.station.train_has_left("Train2"))

    def test_train_has_left_not_first_or_empty_queue(self):
        result = self.station.train_has_left("Train A")
        self.assertFalse(result)

    def test_train_has_arrived_next_in_queue(self):
        self.station.new_arrival_on_board("Train A")
        response = self.station.train_has_arrived("Train A")
        self.assertIn("Train A is on the platform", response)
        self.assertEqual(len(self.station.departure_trains), 1)

    def test_arrival_queue_with_multiple_trains(self):
        self.station.new_arrival_on_board("Train1")
        self.station.new_arrival_on_board("Train2")
        self.assertEqual(len(self.station.arrival_trains), 2)
        self.assertEqual(self.station.arrival_trains[0], "Train1")
        self.assertEqual(self.station.arrival_trains[1], "Train2")

    def test_train_has_arrived_not_next_in_queue(self):
        self.station.new_arrival_on_board("Train A")
        self.station.new_arrival_on_board("Train B")
        response = self.station.train_has_arrived("Train B")
        self.assertIn("other trains to arrive before Train B", response)

    def test_train_has_left_first_in_queue(self):
        self.station.new_arrival_on_board("Train A")
        self.station.train_has_arrived("Train A")
        result = self.station.train_has_left("Train A")
        self.assertTrue(result)
        self.assertEqual(len(self.station.departure_trains), 0)

    def test_departure_without_arrival(self):
        self.assertFalse(self.station.train_has_left("Train1"))

    def test_departure_queue_empty(self):
        self.station.new_arrival_on_board("Train1")
        self.station.train_has_arrived("Train1")
        self.station.train_has_left("Train1")
        self.assertFalse(self.station.train_has_left("Train1"))

    def test_empty_station(self):
        self.assertEqual(len(self.station.arrival_trains), 0)
        self.assertEqual(len(self.station.departure_trains), 0)

    def test_multiple_trains(self):
        self.station.new_arrival_on_board("Train A")
        self.station.new_arrival_on_board("Train B")
        self.assertEqual(len(self.station.arrival_trains), 2)

    def test_multiple_train_arrivals_and_departures(self):
        for train in ["Train1", "Train2", "Train3"]:
            self.station.new_arrival_on_board(train)

        for train in ["Train1", "Train2", "Train3"]:
            self.station.train_has_arrived(train)
            self.assertTrue(self.station.train_has_left(train))


if __name__ == '__main__':
    main()
