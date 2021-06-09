import numpy as np


a = 0.5; b = 2
h = 0.25

def horner(poly, x):
    n = len(poly)
    result = poly[0]
    arr = [result]

    for i in range(1, n):
        result = result * x + poly[i]
        arr.append(result)

    return np.array(arr)


# 0.374x^5 + 0.242x^4 - 1.413x^3 + 0.764x^2 +3.183x - 0.678
poly = [0.374, 0.242, -1.413, 0.764, 3.183, -0.678]
x = np.arange(a, b + 0.1, h)

for i in x:
    print(f'{i}\t{horner(poly, i)}')
