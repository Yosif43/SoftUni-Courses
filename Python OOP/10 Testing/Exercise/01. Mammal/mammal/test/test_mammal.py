from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Wolf", "Mammal", "Wooo")

    def test_init(self):
        self.assertEqual("Wolf", self.mammal.name)
        self.assertEqual("Mammal", self.mammal.type)
        self.assertEqual("Wooo", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Wolf makes Wooo", result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual("Wolf is of type Mammal", result)

if __name__ == "__main__":
    main()
