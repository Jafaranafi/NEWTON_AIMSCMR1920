import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def fcn(t,u):
    return [u[0]*(1-0.5*u[1]),
            u[1]*( 0.25*u[0]-0.75)]

te = 20
Tspan = [0.,te]
method = 'RK23'

I = [2,2]
sol1 = solve_ivp(fcn, Tspan, I, \
        method, dense_output=True, rtol=1.e-6)
I = [2.6,2.0]
sol2 = solve_ivp(fcn, Tspan, I, 
        method, dense_output=True, rtol=1.e-6)

plt.figure(1)
plt.plot(sol1.y[0], sol1.y[1], 'b-', linewidth=1.0)
plt.plot(sol2.y[0], sol2.y[1], 'b-', linewidth=1.0)
plt.title('solve_ivp: RK23; limit cycle')
plt.grid(True)
plt.show()

