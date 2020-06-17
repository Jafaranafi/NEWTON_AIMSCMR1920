import numpy as np
from scipy.integrate import solve_ivp

def pend(t, y):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

# parrameters
b = 0.25
c = 5.0

Tspan = [0, 10]
y0 = [np.pi-0.1,0.0]
sol = solve_ivp(pend, Tspan, y0, method='RK23')

import matplotlib.pyplot as plt
plt.plot(sol.t, sol.y[0], 'b', label='theta(t)')
plt.plot(sol.t, sol.y[1], 'g', label='omaga(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid(True)
plt.show()

