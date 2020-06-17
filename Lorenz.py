import numpy as np
import matplotlib.pyplot as plt
import IVP as IVP

def lorenz(u,t):
    x, y, z = u
    # dx = 10*(y-x)
    # dy = x*(27-z)-y
    # dz = x*y - 8/3*z
    return [10*(y-x), x*(27-z)-y, x*y - 8/3*z]

Nt = 10000
Tspan = [0.,100]

I = [1,0.01,0.01]
u, t = IVP.RK4(lorenz, Tspan, I, Nt)

plt.figure()
plt.plot(u[:,0],u[:,2],'b-',linewidth=1.0)
plt.title('RK4 method, Lorenz system')
plt.axis([-20,20,0,55])
plt.xlabel('x')
plt.ylabel('z')
plt.grid(True)
plt.show()

