"""The program displays an image of an hourglass
made up of the numbers 1, 2, 3, 4."""

counter = 16


def sand(h):
    global counter
    if h < 5:
        print((str(h) * counter).center(16))
        counter -= 4
        sand(h + 1)
        counter += 4
        if h != 4:
            print((str(h) * counter).center(16))


sand(1)
