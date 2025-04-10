"""File to define Bear class."""

__author__: str = "730597830"


class Bear:
    age: int
    hunger_score: int

    """Initializer for the Bear class"""

    def __init__(self):
        self.age = 0
        self.hunger_score = 0
        return None

    """Effects of one day passing on any instance of Bear"""

    def one_day(self):
        self.age += 1
        self.hunger_score -= 1
        return None

    """Effects of eating any number of fish"""

    def eat(self, num_fish: int):
        self.hunger_score += num_fish
        return None
