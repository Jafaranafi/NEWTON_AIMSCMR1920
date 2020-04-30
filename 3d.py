from mpl_toolkits import mplot3d
#matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
#def f(x, y):
#    return np.sin(np.sqrt(x ** 2 + y ** 2))

#x = np.linspace(-6, 6, 30)
#y = np.linspace(-6, 6, 30)

#X, Y = np.meshgrid(x, y)
#Z = f(X, Y)

#fig = plt.figure()
#ax = plt.axes(projection='3d')
#ax.contour3D(X, Y, Z, 50, cmap='binary')
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z');


from mpl_toolkits.mplot3d import Axes3D
def f(x, y):
    return pow(x,2)+pow(y,2)-1

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none',alpha=.5)
ax.scatter(0,0,0, c="r", alpha=1)
ax.set_title('surface')
plt.show()

