import numpy as np
import scikits.bvp1lg.colnew as colnew
from scipy.integrate import simps, trapz

"""
Opt2 Example 5 of optimal control tutorial.
     minimize J = .5* int_0^T u^2 dt
     subject to: x1' = x2, x2' = u with conditions
     x1(0) = 1, x2(0) = 2, x1(T) = 3.
"""

def fsub(t, z):
    """ ODE's for states and costates """
    x1, x2, p1, p2, T = z
    u = -p2
    zero = np.zeros_like(t)
    return [ T*x2, T*u, zero, -T*p1, zero]

def gsub(z):
    """ The boundary conditions """
    x1, x2, p1, p2, T = z
    # x1(0) = 1., x2(0) = 2., x1(T) = 3, x2(T) = 0.
    # p1(T)*x2(T) - 0.5*p2(T)**2 = 0.
    return [x1[0]-1., x2[1]-2., x1[2]-3., \
            x2[3], p2[4]]
    #       x2[3], p1[4]*x2[4] - .5*p2[4]**2]

def guess(t):
    x1 = 2*np.ones_like(t) 
    x2 = 3*np.ones_like(t) 
    p1 = 1*np.ones_like(t) 
    p2 = 1*np.ones_like(t) 
    T  = 2*np.ones_like(t) 
    z = np.array([x1,x2,p1,p2,T])
    dm = fsub(t,z)
    return z, dm 

# Initial guess for the solution
N = 11
degrees = [1, 1, 1, 1, 1]
boundary_points = [0, 0, 1, 1, 1]
tin = np.linspace(0, 1, N)

# solve the boundary value problem
tol = [1e-6, 1e-6, 1e-6, 1e-6, 1e-6]
solution = colnew.solve(
    boundary_points, degrees, fsub, gsub,
    dfsub=None, dgsub=None,
    is_linear=False, tolerances=tol, initial_guess=guess,
    collocation_points=4, initial_mesh=tin,
    vectorized=True, maximum_mesh_size=50, verbosity=3)

t = solution.mesh
x1 = solution(t)[:,0]
x2 = solution(t)[:,1]
p1 = solution(t)[:,2]
p2 = solution(t)[:,3]
T  = solution(t)[-1,4]


print('p1, p2', p1[-1], p2[-1])
# Calculate u(t) from x,p
u = -p2
# Calculate the cost
J = T*simps(u*u,x=t)/2

print('p1, T', p1[-1], T)
print('J', J)

import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(T*t, x1,'-', label='$x_1(t)$')
plt.plot(T*t, x2,'-', label='$x_2(t)$')
plt.plot(T*t, u,'r:', label='$u(t)$')
plt.text(1.22,2.34,'$x_1(t)$')
plt.text(1.22,0.80,'$x_2(t)$')
plt.text(1.22,-.64, 'u(t)')
s = 'Final cost is: J = '+str(round(J,6))
plt.text(1.41,1.52,s)
plt.xlabel('time')
plt.ylabel('states')
plt.grid()
plt.legend(framealpha=1, shadow=True)
plt.title('Colnew: Optimal control problem 2')
#plt.savefig('opt2.eps',bbox_inches='tight')
plt.show()
