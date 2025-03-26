import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

"""John's Dictionary Test Cases"""

__author__: str = "730597830"

"""Testing the invert function"""


def test_invert_with_nonempty_dictionary() -> None:
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_with_one_entry() -> None:
    assert invert({"Solomon": "red"}) == {"red": "Solomon"}


""""Testing invert with an empty dictionary edge case"""


def test_invert_with_empty_dictionary() -> None:
    assert invert({}) == {}


"""Testing invert for repeat keys error"""


def test_invert_for_repeat_keys_error() -> None:
    with pytest.raises(KeyError):
        invert({"a": "z", "b": "z"})


"""Testing the count function"""


def test_count_with_nonempty_list() -> None:
    assert count(["a", "b", "c", "a", "b", "b", "c"]) == {"a": 2, "b": 3, "c": 2}


def test_count_with_one_entry() -> None:
    assert count(["Solomon"]) == {"Solomon": 1}


"""Testing count with an empty list edge case"""


def test_count_with_empty_list() -> None:
    assert count([]) == {}


"""Testing the favorite_color function"""


def test_favorite_color_with_nonempty_dictionary() -> None:
    assert (
        favorite_color(
            {
                "Solomon": "red",
                "chad": "green",
                "Emma": "red",
                "Mom": "yellow",
                "Finn": "green",
            }
        )
        == "red"
    )


def test_favorite_color_with_one_entry() -> None:
    assert favorite_color({"Solomon": "red"}) == "red"


"""Testing favorite_color with an empty dictionary edge case"""


def test_favorite_color_with_empty_dictionary() -> None:
    assert favorite_color({}) == ""


"""Testing the bin_len function"""


def test_bin_len_with_nonempty_list() -> None:
    assert bin_len(["the", "quick", "fox"]) == {3: {"fox", "the"}, 5: {"quick"}}


def test_bin_len_with_one_entry() -> None:
    assert bin_len(["Solomon"]) == {7: {"Solomon"}}


"""Testing bin_len with empty list edge case"""


def test_bin_len_with_empty_list() -> None:
    assert bin_len([]) == {}
