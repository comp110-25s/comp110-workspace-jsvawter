"""File to define Bear class."""

__author__: str = "730597830"


class Bear:
    age: int
    hunger_score: int

    def __init__(self, age: int, hunger_score: int):
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        self.hungerscore += num_fish
        return None
