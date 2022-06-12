import numpy as np

def cost(x, y, w):
    c = 0
    for i in range(len(x)):
        h = w * x[i] - y[i]
        c += h**2

    return c / len(x)

x = [1, 2, 3]
y = [1, 2, 3]

print(cost(x, y, w=2))

def gradient_descent(x, y, w):
    c = 0
    for i in range(len(x)):
        hx = w * x[i]
        c += (hx - y[i]) * x[i]

    return c / len(x)

def show_gradient():
    x = [1, 2, 3]
    y = [1, 2, 3]

    w = 5
    for i in range(10):
        g = gradient_descent(x, y, w)
        w -= 0.1 * g
        print(i, w)