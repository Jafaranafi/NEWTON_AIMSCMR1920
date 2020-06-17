import numpy as np
from scipy.integrate import solve_bvp, simps

"""
Opt2 Example 5 of optimal control tutorial.
     minimize J = .5* int_0^T u^2 dt
     subject to: x1' = x2, x2' = u with conditions
     x1(0) = 1, x2(0) = 2, x1(T) = 3.
"""

def ode(t, y, p):
    """ ODE's for states and costates """
    p1, T = p
    u =  -y[2]
    return [ T*y[1], T*u, -T*p1*np.ones(len(u))]

def bc(ya, yb, p):
    """ The boundary conditions """
    # p1, T = p
    # x1(0) = 1., x2(0) = 2., x1(T) = 3, x2(T) = 0.
    # p1(T)*x2(T) - 0.5*p2(T)**2 = 0.
    return [ya[0]-1., ya[1]-2., yb[0]-3., \
            yb[1], -.5*yb[2]**2]

# Initial guess for the solution
N = 11
xin = np.linspace(0, 1, N)
yin = np.zeros((3,N))
yin[0,:] = 2
yin[1,:] = 3
yin[2,:] = 1

# solve the boundary value problem
sol = solve_bvp(ode, bc, xin, yin, p = [1.,2.], tol=1e-6)
t = sol.x
y1 = sol.y[0]
y2 = sol.y[1]
p2 = sol.y[2]
p1, T = sol.p

print('p1, p2', p1, p2[-1])
# Calculate u(t) from x,p
u = -p2
# Calculate the cost
J = T*simps(u*u,x=t)/2

print('p1, T', sol.p)
print('J', J)

import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(T*sol.x, y1,'-', label='$x_1(t)$')
plt.plot(T*sol.x, y2,'-', label='$x_2(t)$')
plt.plot(T*sol.x, u,'r:', label='$u(t)$')
plt.text(1.22,2.34,'$x_1(t)$')
plt.text(1.22,0.80,'$x_2(t)$')
plt.text(1.22,-.64, 'u(t)')
s = 'Final cost is: J = '+str(round(J,6))
plt.text(1.41,1.52,s)
plt.xlabel('time')
plt.ylabel('states')
plt.grid()
plt.legend(framealpha=1, shadow=True)
plt.title('Optimal control problem 2')
plt.savefig('opt2.pdf',bbox_inches='tight')
plt.show()
