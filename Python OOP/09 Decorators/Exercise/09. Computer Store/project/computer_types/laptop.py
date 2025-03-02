from project.computer_types.computer import Computer


class Laptop(Computer):

    @property
    def available_processors(self):
        return {
            "AMD Ryzen 7 5700G": 900,
            "Intel Core i5-12600K": 1050,
            "Apple M1 Max": 1200
        }

    @property
    def max_ram(self):
        return 64

    def __str__(self):
        return "laptop"
