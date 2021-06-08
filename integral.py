import numpy as np
import matplotlib.pyplot as plt


def function(x):
    return x ** 2 # some function


def left_rectangle(a, b) -> float:
    n = 10000          # how many rectangles to sum up
    area = 0         # start area equals to 0
    dx = (b - a) / n # step of argument x

    for i in range(n):
        # print(f'{i}\t{a + i * dx}\t{function(a + i * dx)}')
        area += function(a + i * dx)

    area *= dx
    print(area)

    return round(area, 5)


def right_rectangle(a, b) -> float:
    n = 10000
    area = 0
    dx = (b - a) / n

    for i in range(1, n + 1):
        # print(f'{i}\t{a + i * dx}\t{function(a + i * dx)}')
        area += function(a + i * dx)

    area *= dx
    print(area)

    return round(area, 5)


def middle_rectange(a, b) -> float:
    n = 10000
    area = 0
    dx = (b - a) / n

    for i in range(n):
        # print(f'{i}\t{a + i * dx + dx / 2}\t{function(a + i * dx + dx / 2)}')
        area += function(a + i * dx + dx / 2)

    area *= dx
    print(area)

    return round(area, 5)


def trapezoid(a, b) -> float:
    '''trapezoid method'''
    n = 10000
    area = 0
    dx = (b - a) / n

    for i in range(n):
        # print(f'{i}\t{a + i * dx}\t{function(a + i * dx)}')
        area += (function(a + i * dx)
               + function(a + (i + 1) * dx)) / 2

    area *= dx
    print(area)
    return round(area, 5)


def simpson(a, b) -> float:
    '''simpson method'''
    n = 10000
    dx = (b - a) / n
    x_int = np.arange(a, b, dx)

    evens = odds = 0

    for i in range(1, n, 2):
        odds += function(x_int[i])

    for i in range(2, n - 1, 2):
        evens += function(x_int[i])

    area = (dx / 3) * (function(x_int[0])
            + 4 * odds + 2 * evens + function(x_int[-1]))

    print(area)
    return area


# left_rectangle(1, 2)
# right_rectangle(1, 2)
# middle_rectange(1, 2)
# trapezoid(1, 2)
# simpson(1, 2)
