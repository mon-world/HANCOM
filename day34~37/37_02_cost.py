import numpy as np

def cost(x, y, w):
    c = 0
    for i in range(len(x)):
        h = w * x[i] - y[i]
        c += h**2

    return c / len(x)

x = [1, 2, 3]
y = [1, 2, 3]

print(cost(x,y,w=2))
