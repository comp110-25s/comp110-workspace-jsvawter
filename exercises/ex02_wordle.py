"""John's Wordle Game"""

__author__: str = "730597830"

"""Unicode for Emojified Boxes"""


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


"""Checking to see if a character is in the key word"""


def contains_char(secret: str, character: str, idx: int = 0) -> bool:
    assert len(character) == 1, f"len('{character}') is not 1"
    while idx < len(secret):
        if character == secret[idx]:
            return True
        else:
            idx = idx + 1
    return False


"""Emojified Answers"""


def emojified(secret: str, guess: str, idx: int = 0) -> str:
    assert len(guess) == len(secret), "Guess must be same length as secret"
    BOX_STRING: str = ""
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            BOX_STRING = BOX_STRING + GREEN_BOX
        elif contains_char(secret, guess[idx]):
            BOX_STRING = BOX_STRING + YELLOW_BOX
        else:
            BOX_STRING = BOX_STRING + WHITE_BOX
        idx = idx + 1
    return f"{BOX_STRING}"
