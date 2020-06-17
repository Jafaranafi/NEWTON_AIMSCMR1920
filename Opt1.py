import numpy as np
from scipy.integrate import solve_bvp, simps, trapz 

""" 
Opt1: Example 1 of optimal control tutorial.
      min.:   J = int_0^1 (u-x)**2 dt
      sub to: x' = u;  x(0) = 1
      The minimum principle gives the bvp problem:
      x' = u; p' = 2*(u-x); with x(0) = 1, p(1) = 0
      where u = x - p/2. 
      Note: lambda is renamed as p!
"""

def ode(t, y):
    u =  y[0] - y[1]/2.
    return [u, 2*(u-y[0])]

def bc(ya, yb):
    return [ya[0]-1, yb[1]]

# Initial guess for the solution
N = 11
xin = np.linspace(0, 1, N)
yin = np.zeros((2,N))   # trivial guess

# solve the boundary value problem
sol = solve_bvp(ode, bc, xin, yin)
x = sol.x
y = sol.y[0]
p = sol.y[1]

# Calculate u(t) from x,p
u = y - p/2.
# Calculate the cost
w = (u-y)**2
J = trapz(w,x=x)

import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(x, y,'-', label='$y(t)$')
plt.plot(x, p,'-', label='$p(t)$')
plt.plot(x, u,'r:',    label='$u(t)$')
plt.text(.23,1.1,'x(t)')
plt.text(.33,1.2, 'u(t)')
plt.text(.23,0.1,'p(t)')
s = 'Final cost is: J='+str(J)
plt.text(.41,.8,s)
plt.xlabel('time')
plt.ylabel('states')
plt.grid()
plt.legend(framealpha=1, shadow=True)
plt.title('Optimal control 1')
plt.savefig('opt1.eps')
plt.show()


