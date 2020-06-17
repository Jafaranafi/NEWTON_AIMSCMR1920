import numpy as np
import matplotlib.pyplot as plt
from IVP import *

""" Van der Pol's equation """

mu = 4000

def fcn(u,t):
    dx = u[1]
    dy = mu*((1-u[0]**2)*u[1] - u[0])
    return [dx,dy]

Nt = 1000
Tspan = [0,6]
I = [2,0]
u, t = RK4(fcn, Tspan, I, Nt)

plt.figure()
plt.plot(t, u[:,0], 'r-')
plt.title("Van der Pol's equation")
plt.xlabel('t')
plt.ylabel('y')
plt.grid(True)
plt.savefig('Pol2.eps',bbox_inches='tight')
plt.show()

