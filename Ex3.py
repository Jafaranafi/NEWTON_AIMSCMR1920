import numpy as np
import matplotlib.pyplot as plt
from IVP import RK4

A = 1.
B = 3.

def fcn(u,t):
    dx = A + u[0]*(u[0]*u[1] - (B+1))
    dy = u[0]*( B - u[0]*u[1])
    return [dx, dy]

Nt = 600
Tspan = [0,10]

u, x = RK4(fcn, Tspan, [3.8,.1],  Nt)
v, x = RK4(fcn, Tspan, [0.0,0.0], Nt)
w, x = RK4(fcn, Tspan, [1.2,2.9], Nt)

plt.figure()
plt.plot(3.8,.1,'r^',u[:,0],u[:,1],'r-')
plt.plot(0.02,0.02,'b^',v[:,0],v[:,1],'b-')
plt.plot(1.2,2.9,'c^',w[:,0],w[:,1],'c-')
plt.title('RK4: Brusselator, limit cycle')
plt.axis([0,4,0,5])
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.show()

