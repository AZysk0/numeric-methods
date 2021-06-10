import numpy as np

# some func
f = lambda x: x ** 2 + 2 * np.exp(-0.65 * x)
# golden ratio
phi = 1.618


def min_value():
    # precision
    eps = 0.01
    # bounds
    a = -5; b = 5

    while True:
        x1 = b - (b - a) / phi
        x2 = a + (b - a) / phi

        fx1 = f(x1)
        fx2 = f(x2)
        # print(f'{a}\t{b}\t{x1}\t{x2}\t{fx1}\t{fx2}')

        if abs(a - b) < eps:
            break
        if fx1 < fx2: b = x2
        else:         a = x1

    return 0.5 * (a + b)


def max_value():
    eps = 0.01
    a = -5; b = 5

    while True:
        x1 = b - (b - a) / phi
        x2 = a + (b - a) / phi

        fx1 = f(x1)
        fx2 = f(x2)
        # print(f'{a}\t{b}\t{x1}\t{x2}\t{fx1}\t{fx2}')
        if abs(a - b) < eps:
            break
        if fx1 > fx2: b = x2
        else:         a = x1

    return 0.5 * (a + b)


# print(min_value())
# print(max_value())
