"""The range_sum() function takes three arguments in the following order:

numbers — list of integers
start — non-negative integer
end — non-negative integer

The function sums all numbers from the list numbers from numbers[start]
to numbers[end] inclusive and returns the resulting result."""


def range_sum(numbers: list, start: int, end: int) -> int:
    if start == end:
        return numbers[start]
    return numbers[start] + range_sum(numbers, start + 1, end)
