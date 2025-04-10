"""File to define River class."""

__author__: str = "730597830"


# from exercises.ex04.fish import Fish
# from exercises.ex04.bear import Bear
from exercises.ex04.river import River


"""Functionality tests."""

my_river: River = River(10, 2)

print(my_river.view_river())

print(my_river.one_river_day())
