import numpy as np
import matplotlib.pyplot as plt


def function(x):
    return x ** 2 # some function


def left_rectangle(a, b) -> float:
    n = 10000          # how many rectangles to sum up
    area = 0         # start area equals to 0
    dx = (b - a) / n # step of argument x

    for i in range(n):
        area += function(a + i * dx)

    area *= dx
    print(area)

    return area


def right_rectangle(a, b) -> float:
    n = 10000
    area = 0
    dx = (b - a) / n

    for i in range(1, n + 1):
        area += function(a + i * dx)

    area *= dx
    print(area)

    return area


def middle_rectange(a, b) -> float:
    n = 10000
    area = 0
    dx = (b - a) / n

    for i in range(n):
        area += function(a + i * dx + dx / 2)

    area *= dx
    print(area)

    return area


def trapezoid(a, b) -> float:
    '''trapezoid method'''
    n = 10000
    dx = (b - a) / n
    

    pass


def simpson(a, b) -> float:
    '''simpson method'''
    pass


left_rectangle(1, 2)
right_rectangle(1, 2)
middle_rectange(1, 2)
