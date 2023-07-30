"""The function returns a string obtained by concatenating
the appropriate noun from the declensions tuple
and the amount in the following format:
<number> <noun>"""


def choose_plural(amount: int, declensions: tuple) -> str:
    for _ in declensions:
        if amount % 10 == 1 and amount % 100 != 11:
            return f"{str(amount)} {declensions[0]}"
        if amount % 10 in (2, 3, 4) and amount % 100 not in (12, 13, 14):
            return f"{str(amount)} {declensions[1]}"
        return f"{str(amount)} {declensions[2]}"
