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


def newton_inter(x):
    '''
    x_data: interpolation points
    newton interpolate polynomial at x
    '''
    h = 0.005


    return


x = np.arange(0.101, 0.156, 0.005)
print(x)
y = np.array([  1.2618,
                1.2764,
                1.2912,
                1.3061,
                1.3213,
                1.3366,
                1.3520,
                1.3677,
                1.3835,
                1.3995,
                1.4157,])

a = diff_table(x, y)#[0, :]
print(a)
print(newton_inter(0.104))
print(newton_inter(0.133))

fig, ax = plt.subplots()
ax.scatter(x, y)
plt.show()
