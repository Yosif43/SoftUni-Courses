from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from typing import List
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in ["FreeDiver", "ScubaDiver"]:
            return f"{diver_type} is not allowed in our competition."

        if any(diver.name == diver_name for diver in self.divers):
            return f"{diver_name} is already a participant."

        diver = FreeDiver(diver_name) if diver_type == "FreeDiver" else ScubaDiver(diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in ["PredatoryFish", "DeepSeaFish"]:
            return f"{fish_type} is forbidden for chasing in our competition."

        if any(fish.name == fish_name for fish in self.fish_list):
            return f"{fish_name} is already permitted."

        fish = PredatoryFish(fish_name, points) if fish_type == "PredatoryFish" else DeepSeaFish(fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((diver for diver in self.divers if diver.name == diver_name), None)
        if not diver:
            return f"{diver_name} is not registered for the competition."

        fish = next((fish for fish in self.fish_list if fish.name == fish_name), None)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch and not is_lucky:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."

        diver.hit(fish)
        if diver.oxygen_level == 0:
            diver.has_health_issue = True
        return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        recovered_count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.renew_oxy()
                recovered_count += 1
        return f"Divers recovered: {recovered_count}"

    def diver_catch_report(self, diver_name: str):
        diver = next((diver for diver in self.divers if diver.name == diver_name), None)
        if diver:
            report = f"**{diver_name} Catch Report**\n"
            report += "\n".join(fish.fish_details() for fish in diver.catch)
            return report
        return f"No report available for {diver_name}."

    def competition_statistics(self):
        healthy_divers = [diver for diver in self.divers if not diver.has_health_issue]
        sorted_divers = sorted(healthy_divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        return "**Nautical Catch Challenge Statistics**\n" + "\n".join(str(diver) for diver in sorted_divers)
