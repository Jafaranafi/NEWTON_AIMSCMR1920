import numpy as np
from scipy.linalg import norm
from step import *
from vec_print import *

def f_circle(n, x):
    fx = np.zeros(n-1)
    fx[0] = x[0]**2 + x[1]**2 - 1.
    return fx

def fp_circle(n, x):
    fpx = np.zeros((n-1, n))

    fpx[0,0] = 2.0 * x[0]
    fpx[0,1] = 2.0 * x[1]
    fpx[0,:] = 2.0*x
    return fpx


def step_test ( ):

    print ' ' 
    print 'STEP_TEST' 
    print '  Demonstrate the STEP function for continuation.' 

    n = 2;
    temp = -np.sqrt ( 3.0 ) / 2.0
    x0 = np.array([ 0.5, temp ])
    t0 = np.zeros( n )
    p = 0
    tol = 1.0e-05

    vec_print ( n, x0, '  Starting X0:' )
    fx_norm = norm ( f_circle ( n, x0 ), 1 )
    print "  ||F(X0)|| = %8g"  % fx_norm

    h = 0.1
    print ' ' 
    print "  Suggested stepsize H = %4f\n"  % h

    status, x2, t2, p2 = step ( n, x0, t0, p, f_circle, fp_circle, h, tol )

    if status == True:
        print ' ' 
        print '  STEP failed.\n' 
    else:
        vec_print ( n, x2, '  Solution X2:' )
        fx_norm = norm ( f_circle ( n, x2 ), 1 )
        print "  ||F(X)|| = %8g"  %  fx_norm 

    return

if __name__ == "__main__":
    step_test()
