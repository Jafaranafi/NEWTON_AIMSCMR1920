import numpy as np
from tangent import *
from vec_print import *

def fp_circle(n, x):
    fpx = np.zeros((n-1, n))

    fpx[0,0] = 2.0*x[0]
    fpx[0,1] = 2.0*x[1]
    return fpx


def tangent_test ( ):

    print ' ' 
    print 'TANGENT_TEST' 
    print '  Demonstrate the TANGENT function for continuation.' 
    print '  At a point X, using continuation parameter P,' 
    print '  compute the tangent vector of unit norm.' 

    n = 2
    temp = -np.sqrt(3.0)/2.0
    x = [ 0.5, temp ]
    t = np.zeros(n)
    p = 0

    print ' '
    print '  Index of current continuation parameter P = %2d' % p  
    
    vec_print( n, x,' Current point X:')

    t2, p2 = tangent ( n, x, t, p, fp_circle )

    vec_print( n, t2,'  Unit tangent vector T2:')

    print ' ' 
    print '  Index of next continuation parameter P2 = %2d' % p2  

    return

if __name__ == "__main__": 
    tangent_test()

