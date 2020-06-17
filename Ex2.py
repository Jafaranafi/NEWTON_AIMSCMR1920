import numpy as np
import matplotlib.pyplot as plt
from IVP import Heun

def fcn(u,t):
    dx = u[0] + u[1] - u[0]*(u[0]**2+u[1]**2)
    dy =-u[0] + u[1] - u[1]*(u[0]**2+u[1]**2)
    return np.stack((dx,dy))

Nt = 150
Tspan = [0,10]

I1 = np.stack((1.0,1.0))
I2 = np.stack((0.1,0.1))

u, t = Heun(fcn, Tspan, I1, Nt)
v, t = Heun(fcn, Tspan, I2, Nt)

plt.figure(1)
plt.plot(1,1,'r^',u[:,0],u[:,1],'r-',linewidth=1.0)
plt.plot(.1,.1,'b^',v[:,0],v[:,1],'b-',linewidth=1.0)
plt.title('Heun: limit cycle')
plt.axis('square')
plt.grid(True)
plt.show()

