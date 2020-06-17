import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def fcn(t,u):
    dx = u[0] + u[1] - u[0]*(u[0]**2+u[1]**2)
    dy =-u[0] + u[1] - u[1]*(u[0]**2+u[1]**2)
    return [dx, dy]

Tspan = [0,10]
I1 = [1.0,1.0]
I2 = [0.1,0.1]

sol1 = solve_ivp(fcn, Tspan, I1,    
            method='RK23', rtol=1.e-6)
sol2 = solve_ivp(fcn, Tspan, I2, 
            method='RK23', rtol=1.e-6)

plt.figure()
plt.plot(1,1,'r^',sol1.y[0],sol1.y[1],'r-',linewidth=1.0)
plt.plot(.1,.1,'b^',sol2.y[0],sol2.y[1],'b-',linewidth=1.0)
plt.title('RK23 method, numerical solution')
plt.axis('square')
plt.grid(True)
plt.savefig('limit1.eps',bbox_inches='tight')
plt.show()

