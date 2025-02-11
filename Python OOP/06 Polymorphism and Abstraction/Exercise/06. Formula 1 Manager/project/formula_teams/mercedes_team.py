from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        expenses = 200000
        sponsors = {"Petronas": {1: 1000000, 3: 500000},
                    "TeamViewer": {5: 100000, 7: 50000}}

        for positions in sponsors.values():
            for position, money in positions.items():
                if race_pos <= position:
                    revenue += money
                    break

        revenue -= expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
