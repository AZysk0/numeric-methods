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

func = lambda x: coefs[0] * x ** 3 + coefs[1] * x ** 2  + coefs[2] * x + coefs[3]

# answers #########
x_ans = np.array([-0.5, 0.5, 1.5, 2.5])
y_ans = func(x_ans)
###################

print(y_ans)

fig, ax = plt.subplots()

arg = np.linspace(-2, 3, 50)

ax.plot(arg, func(arg))
ax.scatter(x, y)            # blue
ax.scatter(x_ans, y_ans)    # orange
plt.show()
