import matplotlib.pyplot as plt

import numpy as np


l = 0
r = np.pi / 2
N = 10


plt.figure(figsize=(5,5))
plt.axes()
plt.grid()
f = lambda x: np.cos(x)
print("Введитие размер разибения")

n = int(input())

print("""Выберите оснащение:
1 - левое
2 - центральное
3 - правое""")

t = int(input())
if not 0 < t <= 3:
    raise ValueError()
x = np.linspace(l, r, n + 1)
y = f(x)

X = np.arange(l, r, 0.01)
Y = f(X)


if t == 1:
    x_data = x[:-1]
    y_data = y[:-1]
    plt.bar(x_data, y_data, width=(r - l) / n, alpha=0.2, edgecolor='b',
            align='edge')

if t == 2:
    x_data = (x[1:] + x[:-1]) / 2
    y_data = f(x_data)
    plt.bar(x_data, y_data, width=(r - l) / n, alpha=0.2, edgecolor='b',
            align='center')

if t == 3:
    x_data = x[1:]
    y_data = y[1:]
    plt.bar(x_data, y_data, width=-(r - l) / n, alpha=0.2, edgecolor='b',
            align='edge')
plt.plot(X, Y)

I = np.sum(y_data  * np.pi / 2 / n)
plt.text(0.65, 0.85, f"I = {I}", fontsize=12)
plt.show()