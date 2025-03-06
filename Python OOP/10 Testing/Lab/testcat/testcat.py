from unittest import TestCase, main
from test_cat import Cat


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Pancho")

    def test_feed_cat_expect_fed_and_sleepy_cat_with_increased_size(self):
        expected_result = 1
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_result, self.cat.size)

    def test_cat_feed_twice(self):
        self.cat.eat()
        self.cat.fed = False
        self.cat.eat()
        self.assertEqual(2, self.cat.size)

    def test_feed_cat_when_cat_is_fed_raises_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_sleeping_cat_when_cat_is_fed_makes_cat_not_sleepy(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

    def test_sleeping_cat_when_cat_is_hungry_raises_exception(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as ex:
            self.cat.sleepy()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))


if __name__ == "__main__":
    main()
