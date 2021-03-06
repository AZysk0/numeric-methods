import numpy as np
import matplotlib.pyplot as plt

eps = 0.0001

# some function
f = lambda x: x ** 3 + 2 * x ** 2 - 4 * x + 1
# derivative definition
derivative = lambda x: (f(x + eps) - f(x)) / eps
# 2nd order derivative
derivative2 = lambda x: (f(x + eps) - 2 * f(x) + f(x - eps)) / (eps ** 2)

def find_extrema(x):
    '''
    finding local minima/maxima
    of given function(f(x))
    '''
    extrema = [x[0]]

    for i in range(1, len(x) - 1):
        if (f(x[i - 1]) > f(x[i]) < f(x[i + 1])) or \
           (f(x[i - 1]) < f(x[i]) > f(x[i + 1])):
           extrema += [x[i]]
    extrema += [x[-1]]
    return extrema


def bisection(low, high):
    '''
    bisection method
    finding equation roots
    '''
    # 2 values have the same sign
    if f(low) * f(high) > 0: return None
    else:
        eps = 0.001     # root finding precision
        # found = False   # finding condition
        while (high-low)/2 > eps:
            mid = round((high+low)/2, 5)
            print(f'{low}\t{high}\t{mid}')
            if abs(f(mid)) < eps:
                return mid
            elif f(low)*f(mid) < 0:
                high = mid
            else:
                low = mid
        return mid


def newton(a, b):
    '''
    tangent line method
    '''
    if f(a) * f(b) > 0: return None
    else:
        eps = 0.0001 # root precision

        x0 = b if f(a) > f(b) else a
        x1 = x0 - f(x0) / derivative(x0)
        while abs(f(x1)) > eps:
            x0 = x1
            x1 = x0 - f(x0) / derivative(x0)
        return x1


def biroots(extr):
    root = []
    for i in range(len(extr) - 1):
        x0 = bisection(extr[i], extr[i + 1])
        if x0 != None:
            root += [x0]

    return root


def newroots(extr):
    root = []
    for i in range(len(extr) - 1):
        x0 = newton(extr[i], extr[i + 1])
        if x0 != None:
            root += [x0]
    return root

x = np.arange(-4, 2, 0.01)
y = f(x)

# find local min-max
extr = find_extrema(x)
print(extr)
#
print(biroots(extr))
print(newroots(extr))

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid(True)
plt.show()
