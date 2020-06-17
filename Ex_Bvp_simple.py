import numpy as np
from Bvp_simple import Bvp

Nx = 20 # Nx = number of grid cells, 
        # Nx+1 = number of grid points
a = -1. # a = left end of the domain
b = +1. # b = right end of the domain
ua =-.5 # boundary value left side
ub = .5 # boundary value right side 

def fcn(x):
    return 5*x

def exact(x):
    return x*(-5*x**2 + 8)/6

u,x = Bvp(fcn, a, b, ua, ub, Nx)

# compute the error norm
from scipy.linalg import norm
print('approximation error', abs(norm(u-exact(x))))

xx = np.linspace(a,b)
sol = exact(xx)
 
# generate a plot of the solution
import matplotlib.pyplot as plt
plt.plot(x,u,'bo-', linewidth=.8)
plt.plot(xx,sol,'r-')
plt.title('numerical solution, \
    $-u^{\prime\prime} = f(x),\; u(-1)=-.5, u(1)=.5$')
plt.grid()
plt.legend(['numerical', 'exact'])
plt.show()

