import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

""" Brusselator example """

A = 1.
B = 3.

def fcn(t,u):
    dx = A + u[0]*(u[0]*u[1] - (B+1))
    dy = u[0]*( B - u[0]*u[1])
    return [dx, dy]

Tspan = [0,10]

I1 = [3.8,.1]
I2 = [0.,0.]
I3 = [1.1,2.9]
sol1 = solve_ivp(fcn, Tspan, I1, 
            method='RK45', rtol=1.e-7)
sol2 = solve_ivp(fcn, Tspan, I2,
            method='RK45', rtol=1.e-7)
sol3 = solve_ivp(fcn, Tspan, I3,
            method='RK45', rtol=1.e-7)

plt.figure()
plt.plot(1,3,'k^')
plt.plot(sol1.y[0],sol1.y[1],'r-')
plt.plot(sol2.y[0],sol2.y[1],'b-')
plt.plot(sol3.y[0],sol3.y[1],'c-')
plt.title('RK45: Brusselator, limit cycle')
plt.axis([0,4,0,5])
plt.xlabel('y_1')
plt.ylabel('y_2')
plt.grid(True)
plt.savefig('limit2.eps',bbox_inches='tight')
plt.show()

