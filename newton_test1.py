import numpy as np
from scipy.linalg import norm
from newton import *
from vec_print import *

def f_circle(n, x):
    fx = np.zeros(n-1)
    fx[0] = x[0]**2 + x[1]**2 - 1.
    return fx

def fp_circle(n, x):
    fpx = np.zeros((n-1, n))
    fpx[0,:] = 2.0*x
    return fpx

print ' ' 
print 'NEWTON_TEST\n' 
print '  Demonstrate the NEWTON function for continuation.\n' 

n = 2
x0 = np.array([0.5,-2.0])
p = 0
tol = 1.e-5

vec_print( n, x0, '  Starting X0:' )
fx_norm = norm( f_circle ( n, x0 ), 1 )
print '   ||F(X0)|| = %8f\n'  % fx_norm

status, x = newton ( n, x0, p, f_circle, fp_circle, tol )


vec_print( n, x, '  Starting X:' )
fx_norm = norm( f_circle ( n, x ), 1 )
print '   ||F(X)|| = %8f\n'  % fx_norm


