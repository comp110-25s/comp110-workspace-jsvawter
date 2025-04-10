"""File to define Bear class."""

__author__: str = "730597830"


class Bear:
    """Defining the Bear Class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializer for the Bear class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Effects of one day passing on any instance of Bear."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Effects of eating any number of fish."""
        self.hunger_score += num_fish
        return None
