import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

""" Van der Pol's equation """

mu = 100

def fcn(t,u):
    dx = u[1]
    dy = mu*(( 1 - u[0]**2)*u[1] - u[0])
    return [dx, dy]

Tspan = [0,6]
I = [2,0]
sol = solve_ivp(fcn, Tspan, I, 
            method='RK45', rtol=1.e-3)

print ('Number of function evaluations', sol.nfev)

plt.figure()
plt.plot(1,3,'k^')
plt.plot(sol.t,sol.y[0],'r-')
plt.title('RK45: VanderPol equation')
plt.axis([0,6,-2.2,2.2])
plt.xlabel('t')
plt.ylabel('y')
plt.grid(True)
plt.savefig('VanderPol.eps',bbox_inches='tight')
plt.show()

