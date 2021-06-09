from scipy.interpolate import lagrange
import numpy as np
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt

# givens ##########
x = np.array([-1, 0, 1, 2])
y = np.array([-20, -5, 6, 25])
###################

poly = lagrange(x, y)
coefs = Polynomial(poly).coef
print(coefs)


# func = lambda x: coefs[0] * x ** 3 + coefs[1] * x ** 2  + coefs[2] * x + coefs[3]
def func(x):
    res = 0
    power = len(coefs) - 1
    for coef in coefs:
        res += coef * x ** power
        power -= 1

    return res

# answers #########
x_ans = np.array([-0.5, 0.5, 1.5, 2.5]) # answer arguments
y_ans = func(x_ans)                     # answer function value
###################

print(y_ans)

fig, ax = plt.subplots()

arg = np.linspace(-2, 3, 50)

ax.plot(arg, func(arg))
ax.scatter(x, y)            # blue
ax.scatter(x_ans, y_ans)    # orange
plt.show()
