"""John's Dictionary Functions"""

__author__: str = "730597830"


def invert(A: dict[str, str]) -> dict[str, str]:
    I: dict[str, str] = dict()
    for key in A:
        if A[key] in I:
            raise KeyError("repeat keys")
        I[A[key]] = key
    return I


def count(B: list[str]) -> dict[str, int]:
    P: dict[str, int] = {}
    Q: int = 0
    while Q < len(B):
        if B[Q] in P:
            P[B[Q]] = P[B[Q]] + 1
        else:
            P[B[Q]] = 1
        Q += 1
    return P


def favorite_color(C: dict[str, str]) -> str:
    colors: list[str] = []
    fav: str = ""
    for key in C:
        colors.append(C[key])
    Rank: dict[str, int] = count(colors)
    for key in Rank:
        if fav == "":
            fav = key
        if Rank[fav] < Rank[key]:
            fav = key
    return fav


def bin_len(strings: list[str]) -> dict[int, set]:
    i: int = 0
    count: dict[int, set[str]] = {}
    while i < len(strings):
        string_length: int = len(strings[i])
        print(string_length)
        print(count)
        if string_length not in count:
            count[string_length] = {strings[i]}
        else:
            count[string_length].add(strings[i])
        print(count)
        i += 1
    return count
