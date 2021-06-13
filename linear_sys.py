import numpy as np
import matplotlib.pyplot as plt


def iteration():
    '''
    iteration method
    for solving linear equation systems
    '''
    eps = 0.001
    # x1 + x2 + x3 + x4
    x = np.array([ [0.05, -0.06, -0.12, 0.14, ],
                    [0.04, -0.12,  0.08, 0.11, ],
                    [0.34, 0.08, -0.06, 0.14, ],
                    [0.11, 0.12, 0, -0.03, ], ])
    print(x)
    # check convergence (coefficients sum must be < 1)
    if max([sum(x[i, 0:4]) for i in range(len(x))]) > 1:
        return

    # const
    x0 = np.array([-2.17, 1.4, -2.1, -0.8])

    table = [x0]
    table += [np.array([ np.dot(x[i], x0) + x0[i]  for i in range(len(x))])]

    for k in range(100):
        # stop condition
        if (abs(table[k][0] - table[k + 1][0]) < eps and \
            abs(table[k][1] - table[k + 1][1]) < eps and \
            abs(table[k][2] - table[k + 1][2]) < eps and \
            abs(table[k][3] - table[k + 1][3]) < eps):
            break

        # append new values to array
        table += [np.array([np.dot(x[i], table[k + 1]) + x0[i] for i in range(len(x))])]

    print(table)


iteration()
