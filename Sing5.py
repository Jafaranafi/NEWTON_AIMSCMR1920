import numpy as np
from scipy.linalg import norm, solve
from Second import check, Second
"""
 solve BVPs with a homogeneous second order
 ODE -c2 u" + c0 u  = 0 for 0 < x < 1, c2 > 0!
 for given Dirichlet boundary values 
"""

Nx = 20     # Nx = number of grid cells, 
            # Nx+1 = number of grid points
a =  0.     # a = left end of the domain
b = +1.     # b = right end of the domain
ua = 1.     # boundary value left side
ub = -.5    # boundary value right side 
eps = 5e-3
"""
 c2 u" + c1 u' + c0 u = 0 for a < x < b
 where c2, c1, c0 = coeff, c2 > 0!
"""
    
coeff = [eps,-1.,1.]
r, s = check(coeff, a, b, ua, ub)
print('eigenvalues: ', r)

def exact(x):
    if norm(r) == 0:
        return ua + (ub-ua)*x/(b-a)
    else:
        return s[0]*np.exp(r[0]*x) + s[1]*np.exp(r[1]*x)
   
import matplotlib.pyplot as plt
xx = np.linspace(a,b, 201)
sol = exact(xx)

method = 'upwind'    
u,x = Second(coeff, a, b, ua, ub, Nx, method=method)

# generate a plot of the solution
plt.plot(x,u,'bo-', linewidth=.5, label='numerical')
plt.plot(xx,sol,'r-', label='exact sol.')
plt.title(method + ' difference scheme, ' + r'$\epsilon=%g$' % eps)
plt.grid()
plt.legend(loc='best')
stem = 'sing_%s_%d_%s' % (method, Nx, str(eps).replace('.','_'))
plt.savefig(stem + '.eps',bbox_inches='tight')
plt.show()
