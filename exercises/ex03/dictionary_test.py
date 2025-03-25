from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import bin_len

"""John's Dictionary Test Cases"""

__author__: str = "730597830"


def test_invert() -> None:
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_count() -> None:
    assert count(["a", "b", "c", "a", "b", "b", "c"]) == {"a": 2, "b": 3, "c": 2}


def test_favorite_color() -> None:
    assert True


def test_bin_len() -> None:
    assert True
