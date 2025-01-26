"""John's tea party planning and budgeting"""

__author__: str = "730597830"


def main_planner(guests: int) -> None:
    """Entrypoint of program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """How many tea bags will we need for everyone"""
    return people * 2


def treats(people: int) -> int:
    """How many treats will we need for everyone"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of party calcualtion"""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
