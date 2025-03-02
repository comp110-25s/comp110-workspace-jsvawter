"""John's Wordle Game"""

__author__: str = "730597830"

"""Unicode for Emojified Boxes"""


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(secret: str, character: str) -> bool:
    """Checking to see if a character is in the key word"""
    assert len(character) == 1, f"len('{character}') is not 1"
    idx = 0
    while idx < len(secret):
        if character == secret[idx]:
            return True
        else:
            idx = idx + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Emojified Answers"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    idx = 0
    box_string: str = ""
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            box_string = box_string + GREEN_BOX
        elif contains_char(secret, guess[idx]):
            box_string = box_string + YELLOW_BOX
        else:
            box_string = box_string + WHITE_BOX
        idx = idx + 1
    return f"{box_string}"


def input_guess(expected_length: int) -> str:
    """Function to Allow User Input"""
    word = input(f"Enter a {expected_length} character word:")
    while expected_length != len(word):
        word = input(f"That wasn't {expected_length} chars! Try again:")
    return word


def main(secret: str) -> None:
    """The entry point of the program and maingame loop."""
    turn = 1
    max_attempts = 6
    won = False
    while turn <= max_attempts and not won:
        print(f"=== Turn {turn}/6 ===")
        word = input_guess(len(secret))
        if word == secret:
            print(f"{emojified(word, secret)}")
            print(f"You won in {turn}/6 turns!")
            won = True
        else:
            print(f"{emojified(word, secret)}")
        turn = turn + 1
    if won is False:
        print("X/6 - sorry try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
