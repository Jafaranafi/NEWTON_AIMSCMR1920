import numpy as np
from scipy.linalg import norm, solve

def tangent ( n, x, t1, p, fp ):
    fpx = np.zeros((n,n))
    fpx[:-1,:] = fp( n, x )
    #fpx[-1,:]  = 0.0
    fpx[-1,p]  = 1.0

    b = np.zeros(n)
    b[-1] = 1.0
    t2 = solve(fpx,b)

    t2_norm = norm ( t2, 2 )
    t2 = t2 / t2_norm;
    p2 = 0; tmp = np.abs ( t2[0] )
    for i in range(1,n):
        if np.abs( t2[i] ) > tmp:
            p2 = i; tmp = np.abs ( t2[i] )

    #  Especially when switching parameters, we need to make sure
    #  the sign of the tangent is chosen correctly.  In general,
    #  it should have a POSITIVE projection on the previous tangent.
    
    if  np.dot(t2, t1) < 0.0:
        t2 = -t2
    
    return t2, p2
