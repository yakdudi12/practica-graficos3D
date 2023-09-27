import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import  cm



#modifica esto, y listo, tambien podes modificar el dominio de la funcion
#modifique el codigo para poder aceptar "z"

def f(x,y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


x = np.linspace(-10,10,30)
y = np.linspace(-10,10,30)

x, y = np.meshgrid(x, y)

z = f(x, y)

vals = np.c_[x.ravel(), y.ravel()]
#z = np.reshape([f(val) for val in vals],(100,100))



"""figure_3d = plt.figure(figsize=(8,6))
ax = plt.axes(projection="3d")
ax.plot_surface(x_ax, y_ax,, fx, cmap=cm.coolwarm)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")"""

fig = plt.figure(figsize=(8,6))
ax = plt.axes(projection="3d")
ax.contour3D(x, y, z,80, cmap='viridis', edgecolor='none')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()

