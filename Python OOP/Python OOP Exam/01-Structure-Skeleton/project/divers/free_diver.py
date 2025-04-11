from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, 120)

    def miss(self, time_to_catch: int):
        reduction = round(0.6 * time_to_catch)
        self.oxygen_level = max(self.oxygen_level - reduction, 0)

    def renew_oxy(self):
        self.oxygen_level = 120
