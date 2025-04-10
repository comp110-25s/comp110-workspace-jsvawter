"""File to define River class."""

__author__: str = "730597830"


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
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

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
        i: int = 0
        bear_population: list[Bear] = self.bears
        while i < len(bear_population):
            if bear_population[i].hunger_score < 0:
                bear_population.pop(i)
            i += 1
        self.bears = bear_population
        return None

    def repopulate_fish(self):
        new_fish: Fish = Fish()
        amount_new_fish: int = len(self.fish) // 2
        i: int = 0
        while i < amount_new_fish:
            j: int = 0
            while j < 4:
                self.fish.append(new_fish)
                j += 1
            i += 1
        return None

    def repopulate_bears(self):
        new_bear: Bear = Bear()
        amount_new_bears: int = len(self.bears) // 2
        i: int = 0
        while i < amount_new_bears:
            self.bears.append(new_bear)
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
        while self.day < 8:
            self.one_river_day
            self.day += 1
        return None
