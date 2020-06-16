import numpy as np
from newton import newton

def fcn(z):
    x, y = z
    return np.array([x - y + 1., x**2 + y**2 - 4.])

def dfcn(z):
    x, y = z
    J = np.array([[1, -1.],[2*x, 2*y]])
    return J


#x0 = np.array([0.8,1.8])
x0 = np.array([1.8,0.8])

# execute Newton method for the extended system
print('Newton method')
print('initial guess',x0)
   
x = newton(fcn, dfcn, x0) 

print('The solution', x)

u = .5*(np.sqrt(7)-1)
v = np.array([u,1+u])
print('exa solution',v)
print('')
print('The function', fcn(x))

