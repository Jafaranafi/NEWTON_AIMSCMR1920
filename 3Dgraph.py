import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.linalg import solve
def f(x):
	x,y=z
	f1=x**3+y-1
	f2=y**3-x+1
	return np.array([f1,f1])
def g(x):
	x,y=z
	g1=[3*x**2,1]
	g2=[-1,3*y**2]
	return np.array([g1,g2])
z=np.array([0.5,-1])
p=np.zeros(2)
for i in range(20):
	F=-f(z)
	G=g(z)
	p=solve(G,F)
	z=z+p

def f(x, y):
    return pow(x,3)+y-1
def g(x,y):
    return pow(y,3)-x+1
x = np.linspace(-34, 6, 30)
y = np.linspace(-34, 6, 30)
print(z)
X, Y = np.meshgrid(x, y)
X1, Y1 = np.meshgrid(x, y)
Z = f(X, Y)
Z1=g(X1,Y1)
fig = plt.figure()

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='Reds', edgecolor='none',alpha=.5)
ax.plot_surface(X1, Y1, Z1, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none',alpha=.5)

ax.scatter(z[0],z[1],f(z[0],z[1]), c="r", alpha=1)
ax.set_title('surface')
plt.show()
