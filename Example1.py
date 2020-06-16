import numpy as np
from newton import newton

def fcn(z1):
    x, y ,z=z1
    return np.array([x+y+z-3,x**2+y**2+z**2-5,np.exp(x)+x*y-x*z-1])

def dfcn(z1):
    x, y ,z=z1
    J = np.array([[1,1,1],[2*x,2*y,2*z],[np.exp(x)+y-z,x,-x]])
    return J


x0 = np.array([1,2,3.5])

# execute Newton method for the extended system
print('Newton method')
print('initial guess',x0)
   
x = newton(fcn, dfcn, x0) 

print('The solution', x)

print('')
print('The function', fcn(x))

