import numpy as np
import matplotlib.pyplot as plt


# for euler method
fprime1 = lambda x, y: x + np.sin(y / 3)
# for euler-cauchy method
fprime2 = lambda x, y: x + np.cos(y / np.sqrt(5))


def euler():
    a = 1.6; b = 2.6; h = 0.1
    x0 = 1.6; y0 = 4.6

    x = np.arange(a, b + h, h)
    table = np.zeros([len(x), 3])
    table[:, 0] = np.array([i for i in range(11)])
    table[:, 1] = x
    table[0, 2] = y0

    for i in range(1, len(x)):
        table[i, 2] = table[i - 1, 2] \
                    + h * fprime1(table[i - 1, 1], table[i - 1, 2])

    print(table)
    return table


def euler_cauchy():

    a = 1.8; b = 2.8; h = 0.1
    x0 = 1.8; y0 = 2.6

    x = np.arange(a, b + h, h)
    table = np.zeros([len(x), 3])
    table[:, 0] = np.array([i for i in range(11)])
    table[:, 1] = x
    table[0, 2] = y0

    for i in range(1, len(x)):
        table[i, 2] = table[i - 1, 2] + (h / 2) \
                    * ( fprime2(table[i - 1, 1], table[i - 1, 2]) \
                    +   fprime2(table[i - 1, 1] + h,  table[i - 1, 2] \
                    + h*fprime2(table[i - 1, 1], table[i - 1, 2])))

    print(table)

    return table


table = euler_cauchy()

x = table[:, 1]
y = table[:, 2]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.scatter(x, y)
plt.show()
