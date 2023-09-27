import numpy as np
import matplotlib.pyplot as plt
from    mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def Practicas_uno(x):
    numerador = np.sin(1/x[0])
    denominador = np.sqrt(x[1]**2)
    funcion = numerador/denominador
    return funcion

x = np.linspace(-100,100,1000)
y = np.linspace(-100,100,1000)

x, y = np.meshgrid(x,y)
vals = np.c_[x.ravel(), y.ravel()]
fx = np.reshape([Practicas_uno(val) for val in vals], (1000,1000))

figure_3d = plt.figure(figsize=(8,6))
ax = plt.axes(projection="3d")
ax.contour3D(x, y , fx, 80, cmap="viridis", edgecolor="none")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("fx(x,y)")

plt.show()

