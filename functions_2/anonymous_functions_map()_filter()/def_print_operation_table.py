"""The print_operation_table() function takes three arguments in the following order:

operation - a function characterizing some binary operation
rows — natural number
cols - natural number

The function creates and displays a table of 'rows' of rows and 'cols' of columns,
in which the element with row 'n' and column 'm' has the value operation(n, m)."""

from typing import Callable


def print_operation_table(operation: Callable, rows: int, cols: int) -> None:
    for i in range(1, rows + 1):
        arr = []
        for j in range(1, cols + 1):
            arr.append(str(operation(i, j)))
        print('\t'.join(arr))
