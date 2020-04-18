import numpy as np
from newton import *
from tangent import *
from vec_print import *

def step ( n, x0, t0, p0, f, fp, h, tol ):

    verbose = 0

    t2, p2 = tangent ( n, x0, t0, p0, fp )
  
    x1 = x0 + h * t2

    if verbose == 1:
        print ' ' 
        print '  Will hold X(%d) fixed at %5g\n'  % ( p0, x1[p0] )
        vec_print ( n, x1, '  STEP: Initial point X1:' )

    status, x2 = newton ( n, x1, p0, f, fp, tol )

    return status, x2, t2, p2
