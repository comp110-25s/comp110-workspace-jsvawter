"""File to define Fish class."""

__author__: str = "730597830"


class Fish:
    age: int

    def __init__(self):
        """Initializer for the Fish class"""
        self.age = 0
        return None

    def one_day(self):
        """Effects of one day passing on any instance of Fish"""
        self.age += 1
        return None
