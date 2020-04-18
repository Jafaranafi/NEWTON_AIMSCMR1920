import numpy as np
from scipy.linalg import norm, solve


def newton( n, x0, p, f, fp, tol ):
   
    verbose = 0
    alpha = x0[p]
    x   = x0
    fx  = np.zeros(n)
    fpx = np.zeros((n,n))

    it = 0
    it_max = 10

    while True: 

        if it_max < it:
            status = 1
            return status, x

        fx[0:-1] = f ( n, x )
        fx[-1] = x[p] - alpha

        fx_norm = norm( fx , 1 )

        if verbose == 1:
            print "   %d:   %10f"  % ( it, fx_norm )

        if fx_norm <= tol:
            status = 0
            return status, x

        it += 1

        fpx[:-1,:] = fp ( n, x )    # put the Jacobian in the first n-1 rows
        fpx[-1,:] = 0.              # put zeros in the last row of fpx
        fpx[-1,p]   = 1.            # put a one into the p-th column

        dx = - solve(fpx,fx)
        x0 = x
        x = x0 + dx
    return status, x
