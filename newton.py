import numpy as np
import matplotlib.pyplot as plt


def diff_table(x, y):
    '''
    calculate differences table
    '''
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = round(coef[i + 1][j - 1] - coef[i][j - 1], 5)

    return coef


def newton_poly():
    '''
    x_data: interpolation points
    newton interpolate polynomial at x
    '''
    return


x = np.arange(0.15, 0.61, 0.05)
print(x)
y = np.array([  0.860,
                0.818,
                0.778,
                0.740,
                0.704,
                0.670,
                0.637,
                0.606,
                0.576,
                0.548,])

a = diff_table(x, y)#[0, :]
print(a)

fig, ax = plt.subplots()
ax.scatter(x, y)
plt.show()
