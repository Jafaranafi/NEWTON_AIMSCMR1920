import numpy as np
import scikits.bvp1lg.colnew as colnew
from scipy.integrate import simps, trapz 

""" 
Opt1: Example 1 of optimal control tutorial.
      min.:   J = int_0^1 (u-x)**2 dt
      sub to: x' = u;  x(0) = 1
      The minimum principle gives the bvp problem:
      x' = u; p' = 2*(u-x); with x(0) = 1, p(1) = 0
      where u = x - p/2. 
      Note: lambda is renamed as p!
"""

def fsub(t, z):
    u =  z[0] - z[1]/2.
    return [u, 2*(u-z[0])]

def gsub(z):
    x, p = z
    return [x[0]-1, p[1]]

# Initial guess for the solution
N = 5
degrees = [1, 1]
boundary_points = [0, 1]
tin = np.linspace(0, 1, N)

# solve the boundary value problem
tol = [1e-5, 1e-5]
solution = colnew.solve(
    boundary_points, degrees, fsub, gsub,
    dfsub=None, dgsub=None,
    is_linear=False, tolerances=tol, initial_guess=None,
    collocation_points=3, initial_mesh=tin,
    vectorized=True, maximum_mesh_size=30, verbosity=0)

t = solution.mesh
x = solution(t)[:,0]
p = solution(t)[:,1]

# Calculate u(t) from x,p
u = x - p/2.
# Calculate the cost
w = (u-x)**2
J = trapz(w,x=t)

import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(t, x,'-', label='$x(t)$')
plt.plot(t, p,'-', label='$p(t)$')
plt.plot(t, u,'r:',    label='$u(t)$')
plt.text(.23,1.1,'x(t)')
plt.text(.33,1.2, 'u(t)')
plt.text(.23,0.1,'p(t)')
s = 'Final cost is: J='+str(round(J,5))
plt.text(0.41,.8,s)
plt.xlabel('time')
plt.ylabel('states')
plt.grid()
plt.legend(framealpha=1, shadow=True)
plt.title('colnew: Optimal control 1')
#plt.savefig('opt1.eps')
plt.show()


