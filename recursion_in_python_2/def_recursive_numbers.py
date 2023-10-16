"""The program takes the number 'n' as input and
subtracts the number 5 from it until it is no longer
positive, and then adds the number 5 to it until it
becomes equal to 'n' again."""


def recursive_numbers(n: int) -> None:
    if n < 0:
        print(n)
    else:
        print(n)
        if n != 0:
            recursive_numbers(n - 5)
            print(n)


recursive_numbers(int(input()))
