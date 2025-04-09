"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish(age=0))
        for _ in range(0, num_bears):
            self.bears.append(Bear(age=0, hunger_score=0))

    def check_ages(self, bears, fish):
        bear_population: list[Bear] = self.bears
        fish_population: list[Fish] = self.fish
        i: int = 0
        while i <= len(bears):
            if bears[i][0] > 5:
                bear_population.pop(i)
            i += 1
        i = 0
        while i <= len(fish):
            if fish[i] > 3:
                fish_population.pop(i)
            i += 1
        self.bears = bear_population
        self.fish = fish_population
        return None

    def remove_fish(self, amount: int):
        i: int = 0
        while i < amount:
            self.fish.pop(i)
            i += 1
        return None

    def bears_eating(self):
        i: int = 0
        while i < len(self.bears):
            if len(self.fish) > 4:
                self.bears[i].eat(3)
                self.remove_fish(3)
            i += 1
        return None

    def check_hunger(self):
        return None

    def repopulate_fish(self):
        return None

    def repopulate_bears(self):
        return None

    def view_river(self):
        print(
            f"~~~ Day {self.day}: ~~~ \
Fish population: {len(self.fish)} \
Bear population: {len(self.bears)}"
        )
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages([], [])
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        i: int = 0
        while i < 7:
            self.one_river_day
            i += 1
        return None
