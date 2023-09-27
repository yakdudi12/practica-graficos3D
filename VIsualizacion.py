import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def funcion_prueba(x):
    res = np.sqrt(x[0]**2 + x[1]**2)
    return res

x = np.linspace(-100,100,1000)
y = np.linspace(-100,100,1000)


x_ax, y_ax = np.meshgrid(x,y)
vals = np.c_[x_ax.ravel(), y_ax.ravel()]
fx = np.reshape([funcion_prueba(val) for val in vals], (1000,1000))

figure_3d = plt.figure(figsize=(8,6))
ax = plt.axes(projection="3d")
ax.plot_surface(x_ax, y_ax, fx, cmap=cm.coolwarm)
ax.set_xlabel("x")
ax.set_xlabel("y")
ax.set_xlabel("f(x,y")

plt.show()