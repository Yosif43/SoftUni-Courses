from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Ironman", 100, 50.5, 400.5)

    def test_init(self):
        self.assertEqual("Ironman", self.hero.username)
        self.assertEqual(100, self.hero.level)
        self.assertEqual(50.5, self.hero.health)
        self.assertEqual(400.5, self.hero.damage)

    def test_attributes_types(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_battle_with_same_name(self):
        enemy = Hero(self.hero.username, self.hero.level, self.hero.health, self.hero.damage)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_less_or_equal_than_zero(self):
        self.hero.health = 0
        enemy = Hero("Superman", self.hero.level, self.hero.health, self.hero.damage)

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

        self.hero.health -= 1
        with self.assertRaises(ValueError) as ve2:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve2.exception))

    def test_enemy_health_not_enough(self):
        enemy = Hero("Superman", self.hero.level, 0, self.hero.damage)
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Superman. He needs to rest", str(ve.exception))

        enemy.health -= 1
        with self.assertRaises(ValueError) as ve2:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Superman. He needs to rest", str(ve2.exception))

    def test_draw(self):
        enemy = Hero("Superman", self.hero.level, self.hero.health, self.hero.damage)
        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(self.hero.level, self.hero.level)
        self.assertEqual(-39999.5, self.hero.health)
        self.assertEqual(self.hero.damage, self.hero.damage)

    def test_hero_wins(self):
        enemy = Hero("Superman", 1, 1, 1)
        result = self.hero.battle(enemy)
        self.assertEqual("You win", result)
        self.assertEqual(101, self.hero.level)
        self.assertEqual(54.5, self.hero.health)
        self.assertEqual(405.5, self.hero.damage)

    def test_hero_loses(self):
        self.hero.health = 10
        self.hero.damage = 1

        enemy = Hero("Superman", 150, 200.5, 450.5)
        result = self.hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(151, enemy.level)
        self.assertEqual(105.5, enemy.health)
        self.assertEqual(455.5, enemy.damage)

    def test_str(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                   f"Health: {self.hero.health}\n" \
                   f"Damage: {self.hero.damage}\n"
        self.assertEqual(expected, str(self.hero))


if __name__ == "__main__":
    main()
