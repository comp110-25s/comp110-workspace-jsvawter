"""File to define Fish class."""

__author__: str = "730597830"


class Fish:
    age: int

    """Initializer for the Fish class"""

    def __init__(self):
        self.age = 0
        return None

    """Effects of one day passing on any instance of Fish"""

    def one_day(self):
        self.age += 1
        return None
