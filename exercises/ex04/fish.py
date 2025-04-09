"""File to define Fish class."""

__author__: str = "730597830"


class Fish:
    age: int

    def __init__(self, age: int):
        self.age = 0
        return None

    def one_day(self):
        self.age += 1
        return None
